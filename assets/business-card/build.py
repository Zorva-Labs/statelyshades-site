#!/usr/bin/env python3
"""
Stately Shades — business card production build.

Renders two sides at 300 DPI (1050×600 trim, 1125×675 bleed), composites into
a print-ready PDF. Embodies the "Threshold Light" philosophy: calibrated
restraint, brass as gold leaf, hairlines that whisper.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.pagesizes import portrait
from reportlab.lib.units import inch
from pathlib import Path
import math, random

ROOT = Path(__file__).parent
FONTS = ROOT / "fonts"
SKILL_FONTS = Path("/Users/jamesblair/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/86d15da6-ad6b-4f0a-918b-ea21d51041c2/8ca67834-e0ee-470f-8624-9fa3615686ea/skills/canvas-design/canvas-fonts")

# ── Card geometry (300 DPI) ──────────────────────────────────────────────
DPI = 300
TRIM_W = int(3.5 * DPI)      # 1050
TRIM_H = int(2.0 * DPI)      # 600
BLEED  = int(0.125 * DPI)    # 38 px each side
BLEED_W = TRIM_W + 2 * BLEED # 1126
BLEED_H = TRIM_H + 2 * BLEED # 676

# ── Brand palette (verbatim from styles.css) ─────────────────────────────
CREAM       = (0xF7, 0xF2, 0xEA)
CREAM_2     = (0xEF, 0xE8, 0xDB)
CREAM_3     = (0xE5, 0xDC, 0xC9)
INK         = (0x14, 0x11, 0x0D)
INK_2       = (0x1F, 0x1A, 0x14)
INK_SOFT    = (0x56, 0x49, 0x3C)
BRASS       = (0x9D, 0x7A, 0x3E)
BRASS_HOT   = (0xC9, 0xA1, 0x58)
CHAMPAGNE   = (0xD4, 0xB8, 0x96)
LINE        = (0xD9, 0xCF, 0xBB)

# ── Type loaders ─────────────────────────────────────────────────────────
def F(name, size):
    path = FONTS / name
    if not path.exists():
        path = SKILL_FONTS / name
    return ImageFont.truetype(str(path), size)

CG_REG  = "CormorantGaramond-Regular.ttf"
CG_MED  = "CormorantGaramond-Medium.ttf"
CG_SB   = "CormorantGaramond-SemiBold.ttf"
CG_IT   = "CormorantGaramond-Italic.ttf"
CG_MIT  = "CormorantGaramond-MediumItalic.ttf"
MONO    = "IBMPlexMono-Regular.ttf"
MONO_B  = "IBMPlexMono-Bold.ttf"

# ── Helpers ──────────────────────────────────────────────────────────────
def draw_tracked(draw, xy, text, font, color, tracking_em=0.0, anchor="lt"):
    """Render text with letter-spacing (tracking).

    anchor uses Pillow's two-char anchor codes ("lt"=left-top, "lm"=left-middle,
    "ls"=left-baseline, etc.). The per-char drawing internally uses left-top so
    that characters with different heights (like periods, commas) still sit on
    a consistent baseline derived from the font's metrics rather than from each
    glyph's bounding box.

    tracking_em is in font-size em units (typographic norm).
    """
    x, y = xy
    spacing_px = int(font.size * tracking_em)
    advances = [draw.textlength(ch, font=font) for ch in text]
    total = sum(advances) + spacing_px * (len(text) - 1) if text else 0

    # Horizontal alignment from the supplied anchor
    h_anchor = anchor[0] if anchor else "l"
    if h_anchor == "m":
        x = x - total // 2
    elif h_anchor == "r":
        x = x - total

    # Critical: derive a single common baseline-reference top-y from font ascent.
    # Pillow per-glyph anchor "lt" puts each glyph at the TOP of its own bbox,
    # which makes dots/commas float to cap-height. Instead, use font.getmetrics()
    # to compute an ascent-based top, so every glyph in the line sits on the
    # same baseline.
    ascent, descent = font.getmetrics()
    v_anchor = anchor[1] if len(anchor) > 1 else "t"
    if v_anchor == "t" or v_anchor == "a":
        line_top = y                       # caller wanted top-of-line
        baseline = y + ascent
    elif v_anchor == "m":
        line_top = y - (ascent + descent) // 2 + (ascent + descent) // 2 - ascent // 2  # noqa
        line_top = y - ascent // 2
        baseline = line_top + ascent
    elif v_anchor == "s" or v_anchor == "b":
        baseline = y
        line_top = baseline - ascent
    else:
        line_top = y; baseline = y + ascent

    cur = x
    for ch, w in zip(text, advances):
        # Pillow's anchor "ls" = left-baseline → glyph sits on baseline
        draw.text((cur, baseline), ch, font=font, fill=color, anchor="ls")
        cur += w + spacing_px
    return total

def measure_tracked(draw, text, font, tracking_em):
    if not text: return 0
    spacing_px = int(font.size * tracking_em)
    total = sum(draw.textlength(c, font=font) for c in text) + spacing_px * (len(text) - 1)
    return total

def add_paper_grain(img, intensity=4, seed=42):
    """Adds a very subtle warm-tone noise to simulate uncoated paper.
    intensity = max channel delta (out of 255). Tiny."""
    random.seed(seed)
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            n = random.randint(-intensity, intensity)
            r, g, b = px[x, y][:3]
            px[x, y] = (max(0, min(255, r+n)),
                        max(0, min(255, g+n)),
                        max(0, min(255, b+n)))
    return img

def add_paper_grain_fast(img, intensity=3, seed=42):
    """Vectorised noise — far faster than per-pixel."""
    import numpy as np
    arr = __import__('numpy').asarray(img).astype('int16')
    rng = __import__('numpy').random.default_rng(seed)
    noise = rng.integers(-intensity, intensity+1, arr.shape[:2])
    for c in range(3):
        arr[:,:,c] = arr[:,:,c] + noise
    arr = __import__('numpy').clip(arr, 0, 255).astype('uint8')
    return Image.fromarray(arr)

# ── Monogram: hand-laid "S" + subscript "S" ──────────────────────────────
def draw_monogram(draw, cx, cy, big_size, color):
    """Render the SS lockup at a logical center (cx, cy).

    Uses left-baseline anchoring so both S's share a known baseline. The
    subscript S sits below the big-S baseline by ~22% of its own size, which
    is what gives the "subscript" feel. Returns the cluster's visible
    bounding box (top is big-S cap-top, bottom is subscript-S baseline).
    """
    big_font = F(CG_MED, big_size)
    small_size = int(big_size * 0.55)
    small_font = F(CG_MED, small_size)

    big_w = draw.textlength("S", font=big_font)
    sub_w = draw.textlength("S", font=small_font)

    # Approximate cap-height of the big "S"
    big_ascent, _ = big_font.getmetrics()
    big_cap_h = int(big_ascent * 0.70)

    # Subscript tucks under the right side of big S
    overlap_x = int(big_w * 0.22)
    cluster_w = big_w - overlap_x + sub_w

    # Subscript baseline drops below big-S baseline by sub_offset
    sub_offset = int(small_size * 0.22)

    # Center cluster around (cx, cy):
    #   visible top   = baseline_y - big_cap_h
    #   visible bot   = baseline_y + sub_offset
    #   visible center= baseline_y - (big_cap_h - sub_offset) / 2
    #   want center == cy → baseline_y = cy + (big_cap_h - sub_offset) // 2
    baseline_y = cy + (big_cap_h - sub_offset) // 2

    big_x = cx - cluster_w // 2
    draw.text((big_x, baseline_y), "S", font=big_font, fill=color, anchor="ls")

    sub_x = big_x + big_w - overlap_x
    draw.text((sub_x, baseline_y + sub_offset), "S", font=small_font, fill=color, anchor="ls")

    visible_top = baseline_y - big_cap_h
    visible_bottom = baseline_y + sub_offset
    return (big_x, visible_top, big_x + cluster_w, visible_bottom)

# ── Slat motif ────────────────────────────────────────────────────────────
def draw_slats(draw, x0, y0, x1, y1, n=6, color=BRASS, alpha=0.10):
    """Faint horizontal slat lines as a venetian-blind echo."""
    overlay = Image.new("RGBA", (x1 - x0, y1 - y0), (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    step = (y1 - y0) / (n + 1)
    rgba = color + (int(255 * alpha),)
    for i in range(1, n + 1):
        yy = int(step * i)
        od.rectangle([(0, yy), (x1 - x0, yy + 1)], fill=rgba)
    return overlay

# ── FRONT (cream side) ───────────────────────────────────────────────────
def render_front(with_bleed=True):
    W, H = (BLEED_W, BLEED_H) if with_bleed else (TRIM_W, TRIM_H)
    img = Image.new("RGB", (W, H), CREAM)

    # Warm gradient
    grad = Image.new("RGBA", (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(grad)
    for y in range(H):
        t = y / H
        r = int(CREAM[0] + (CREAM_2[0] - CREAM[0]) * t * 0.45)
        g = int(CREAM[1] + (CREAM_2[1] - CREAM[1]) * t * 0.45)
        b = int(CREAM[2] + (CREAM_2[2] - CREAM[2]) * t * 0.45)
        gd.line([(0, y), (W, y)], fill=(r, g, b, 150))
    img.paste(grad, (0, 0), grad)

    draw = ImageDraw.Draw(img)
    ox = BLEED if with_bleed else 0
    oy = BLEED if with_bleed else 0
    cx = ox + TRIM_W // 2
    optical_cy = oy + int(TRIM_H * 0.35)

    # Monogram (smaller — letting the lockup breathe)
    mono_size = int(TRIM_H * 0.42)
    monogram_box = draw_monogram(draw, cx, optical_cy, mono_size, INK)
    monogram_bottom = monogram_box[3]

    # Wordmark
    wm_font = F(CG_REG, 44)
    wm_text = "STATELY SHADES"
    wm_y = monogram_bottom + 30
    wm_w = measure_tracked(draw, wm_text, wm_font, 0.10)
    draw_tracked(draw, (cx, wm_y), wm_text, wm_font, INK,
                 tracking_em=0.10, anchor="mt")
    wm_ascent, wm_descent = wm_font.getmetrics()
    wm_baseline_y = wm_y + wm_ascent

    # Brass rule
    rule_w = 52
    rule_y = wm_baseline_y + 18
    draw.rectangle([(cx - rule_w // 2, rule_y),
                    (cx + rule_w // 2, rule_y + 1)], fill=BRASS)

    # Tagline (mono caps)
    tg_font = F(MONO, 13)
    tg_text = "BLINDS, SHUTTERS & SHADES"
    tg_y = rule_y + 16
    draw_tracked(draw, (cx, tg_y), tg_text, tg_font, BRASS,
                 tracking_em=0.30, anchor="mt")

    # Slat motif at bottom — more visible
    slat_top = oy + TRIM_H - 56
    slat_overlay = draw_slats(draw, ox + 120, slat_top, ox + TRIM_W - 120, oy + TRIM_H - 22,
                              n=5, color=BRASS, alpha=0.22)
    img.paste(slat_overlay, (ox + 120, slat_top), slat_overlay)

    # Tiny corner stamps
    corner_font = F(MONO, 10)
    corner_y = oy + 30
    draw_tracked(draw, (ox + 38, corner_y), "EST. GALLATIN", corner_font, BRASS,
                 tracking_em=0.32, anchor="lt")
    rt = "TENNESSEE"
    rt_w = measure_tracked(draw, rt, corner_font, 0.32)
    draw_tracked(draw, (ox + TRIM_W - 38, corner_y), rt, corner_font, BRASS,
                 tracking_em=0.32, anchor="rt")

    # Final pass: faint paper grain
    try:
        import numpy as np
        img = add_paper_grain_fast(img, intensity=3, seed=2026)
    except Exception:
        pass

    return img

# ── BACK (espresso side) ─────────────────────────────────────────────────
def render_back(with_bleed=True):
    W, H = (BLEED_W, BLEED_H) if with_bleed else (TRIM_W, TRIM_H)
    img = Image.new("RGB", (W, H), INK)

    # Diagonal subtle warm-gradient (top-left INK_2 → bottom-right INK)
    grad = Image.new("RGBA", (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(grad)
    for y in range(H):
        for x_band_start in range(0, W, 1):  # row-by-row is fine
            pass
    # Faster: do it as a per-row gradient blended with a per-column one
    import numpy as np
    yy, xx = np.indices((H, W))
    # diagonal blend: from top-left (max INK_2) to bottom-right (full INK)
    t = (1.0 - (xx + yy) / (W + H)) * 0.55  # 0..0.55
    rr = INK[0] + (INK_2[0] - INK[0]) * t
    gg = INK[1] + (INK_2[1] - INK[1]) * t
    bb = INK[2] + (INK_2[2] - INK[2]) * t
    arr = np.stack([rr, gg, bb], axis=-1).astype("uint8")
    img = Image.fromarray(arr)

    draw = ImageDraw.Draw(img)
    ox = BLEED if with_bleed else 0
    oy = BLEED if with_bleed else 0

    # Layout: left contact column (60%), right mark column (40%)
    split_x = ox + int(TRIM_W * 0.60)

    # Vertical brass hairline divider
    div_color = BRASS + tuple()  # solid, but we'll layer it semi
    divider_overlay = Image.new("RGBA", (1, TRIM_H - 80), (BRASS[0], BRASS[1], BRASS[2], 130))
    img.paste(divider_overlay, (split_x, oy + 40), divider_overlay)
    # Brass diamond at divider midpoint
    diamond_size = 5
    dx, dy = split_x, oy + TRIM_H // 2
    draw.polygon([(dx, dy - diamond_size), (dx + diamond_size, dy),
                  (dx, dy + diamond_size), (dx - diamond_size, dy)],
                 fill=BRASS_HOT)

    # ── LEFT column: contact info ──
    # Padding from card edge
    left_pad = ox + 48
    inner_w = split_x - left_pad - 28

    # Name
    name_font = F(CG_MED, 44)
    name_text = "MICHAEL BLAIR"
    # Vertical centering: compute total block height first
    role_font = F(CG_MIT, 22)
    role_text = "Sales & Installation"

    # We'll lay it out from top to bottom inside an "info_block"
    # Pulled down ~25 px from the top so the contact stack reads as
    # vertically centered against the monogram on the right column.
    block_top = oy + 96

    # Name (tracked slightly)
    draw_tracked(draw, (left_pad, block_top), name_text, name_font, CHAMPAGNE,
                 tracking_em=0.04, anchor="lt")
    n_bbox = name_font.getbbox(name_text)
    n_h = n_bbox[3] - n_bbox[1]

    # Role
    role_y = block_top + n_h + 14
    draw.text((left_pad, role_y), role_text, font=role_font, fill=BRASS_HOT, anchor="lt")
    r_bbox = role_font.getbbox(role_text)
    r_h = r_bbox[3] - r_bbox[1]

    # Brass rule under role
    rule_y = role_y + r_h + 18
    draw.rectangle([(left_pad, rule_y), (left_pad + 56, rule_y + 1)], fill=BRASS)

    # Contact stack
    phone_font = F(CG_MED, 30)         # phone gets display weight
    detail_font = F(MONO, 15)          # email / web / location in mono

    phone_y = rule_y + 22
    draw.text((left_pad, phone_y), "629.298.8241", font=phone_font, fill=CHAMPAGNE, anchor="lt")
    p_bbox = phone_font.getbbox("629.298.8241")
    p_h = p_bbox[3] - p_bbox[1]

    email_y = phone_y + p_h + 16
    # Email — mono, champagne 80%
    email_color = tuple(int(c * 0.85) for c in CHAMPAGNE)
    draw_tracked(draw, (left_pad, email_y), "HELLO@STATELYSHADES.COM", detail_font, email_color,
                 tracking_em=0.10, anchor="lt")
    e_bbox = detail_font.getbbox("HELLO@STATELYSHADES.COM")
    e_h = e_bbox[3] - e_bbox[1]

    web_y = email_y + e_h + 8
    draw_tracked(draw, (left_pad, web_y), "STATELYSHADES.COM", detail_font, email_color,
                 tracking_em=0.10, anchor="lt")

    # Location stamp at very bottom of left column
    loc_font = F(MONO, 11)
    loc_y = oy + TRIM_H - 56
    loc_color = tuple(int(c * 0.85) for c in BRASS_HOT)
    draw_tracked(draw, (left_pad, loc_y), "GALLATIN · TENNESSEE", loc_font, loc_color,
                 tracking_em=0.30, anchor="lt")

    # ── RIGHT column: mark ──
    right_cx = split_x + (ox + TRIM_W - split_x) // 2
    right_optical_cy = oy + int(TRIM_H * 0.42)

    # Smaller monogram in champagne
    mono_size_back = int(TRIM_H * 0.36)
    mb = draw_monogram(draw, right_cx, right_optical_cy, mono_size_back, CHAMPAGNE)

    # Tiny brass rule below monogram (more breathing room)
    bot_rule_y = mb[3] + 34
    rw = 32
    draw.rectangle([(right_cx - rw // 2, bot_rule_y), (right_cx + rw // 2, bot_rule_y + 1)], fill=BRASS)

    # "STATELY · SHADES" tiny tag below
    tag_font = F(MONO, 9)
    tag_text = "STATELY · SHADES"
    tag_y = bot_rule_y + 14
    draw_tracked(draw, (right_cx, tag_y), tag_text, tag_font, BRASS,
                 tracking_em=0.30, anchor="mt")

    # No top-right slat block — the front carries the motif; back stays quiet

    return img

# ── Build outputs ────────────────────────────────────────────────────────
def main():
    out = ROOT
    # Trim-only PNGs (no bleed) — for web preview
    front_trim = render_front(with_bleed=False)
    back_trim  = render_back(with_bleed=False)
    front_trim.save(out / "card-front.png", "PNG", optimize=True)
    back_trim.save(out / "card-back.png", "PNG", optimize=True)
    print(f"  ✓ card-front.png ({front_trim.size})")
    print(f"  ✓ card-back.png  ({back_trim.size})")

    # Bleed PNGs for print
    front_bleed = render_front(with_bleed=True)
    back_bleed  = render_back(with_bleed=True)
    front_bleed.save(out / "card-front-bleed.png", "PNG", optimize=True)
    back_bleed.save(out / "card-back-bleed.png", "PNG", optimize=True)
    print(f"  ✓ card-front-bleed.png ({front_bleed.size})")
    print(f"  ✓ card-back-bleed.png  ({back_bleed.size})")

    # Combined print PDF — two pages, each at 3.75×2.25 in
    pdf_path = out / "card-print.pdf"
    c = rl_canvas.Canvas(str(pdf_path), pagesize=(3.75 * inch, 2.25 * inch))
    # Page 1 — front
    c.drawImage(str(out / "card-front-bleed.png"), 0, 0,
                width=3.75 * inch, height=2.25 * inch)
    c.showPage()
    # Page 2 — back
    c.drawImage(str(out / "card-back-bleed.png"), 0, 0,
                width=3.75 * inch, height=2.25 * inch)
    c.showPage()
    c.save()
    print(f"  ✓ card-print.pdf (2 pages, 3.75×2.25 in bleed)")

if __name__ == "__main__":
    main()
