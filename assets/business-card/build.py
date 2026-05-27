#!/usr/bin/env python3
"""
Stately Shades — business card production build (v2).

Rendered at 300 DPI for genuine print legibility:
 - Body type at 7–9 pt (28–36 px)
 - Display type at 18–30 pt (75–125 px)
 - Corner stamps at 7 pt minimum (28 px) — readable, not decorative dust

The monogram now follows the website's actual SS lockup: two SAME-SIZE
glyphs where the second tucks LEFT (−0.44 em overlap) and DOWN (+0.22 em
baseline shift) into the first, forming an SS ligature, not a "subscript".
"""
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.units import inch
from pathlib import Path

ROOT = Path(__file__).parent
FONTS = ROOT / "fonts"
SKILL_FONTS = Path("/Users/jamesblair/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/86d15da6-ad6b-4f0a-918b-ea21d51041c2/8ca67834-e0ee-470f-8624-9fa3615686ea/skills/canvas-design/canvas-fonts")

# ── Geometry @ 300 DPI ──────────────────────────────────────────────────
DPI = 300
TRIM_W = int(3.5 * DPI)        # 1050
TRIM_H = int(2.0 * DPI)        # 600
BLEED  = int(0.125 * DPI)      # 38 px
BLEED_W = TRIM_W + 2 * BLEED   # 1126
BLEED_H = TRIM_H + 2 * BLEED   # 676

# ── Brand palette (exact site CSS variables) ────────────────────────────
CREAM       = (0xF7, 0xF2, 0xEA)
CREAM_2     = (0xEF, 0xE8, 0xDB)
INK         = (0x14, 0x11, 0x0D)
INK_2       = (0x1F, 0x1A, 0x14)
BRASS       = (0x9D, 0x7A, 0x3E)
BRASS_HOT   = (0xC9, 0xA1, 0x58)
CHAMPAGNE   = (0xD4, 0xB8, 0x96)

# ── Font loaders ────────────────────────────────────────────────────────
def F(name, size):
    p = FONTS / name
    if not p.exists():
        p = SKILL_FONTS / name
    return ImageFont.truetype(str(p), size)

CG_REG  = "CormorantGaramond-Regular.ttf"
CG_MED  = "CormorantGaramond-Medium.ttf"
CG_SB   = "CormorantGaramond-SemiBold.ttf"
CG_IT   = "CormorantGaramond-Italic.ttf"
CG_MIT  = "CormorantGaramond-MediumItalic.ttf"
MONO    = "IBMPlexMono-Regular.ttf"
MONO_B  = "IBMPlexMono-Bold.ttf"

# ── Tracked-text helper (baseline-anchored, period dots align correctly) ─
def draw_tracked(draw, xy, text, font, color, tracking_em=0.0, anchor="lt"):
    """Render text with letter-spacing tracking. Always anchors each glyph on
    its baseline (Pillow `ls`) so dots/commas/periods sit at the bottom of
    the line instead of floating up to cap-height.
    Supports horizontal anchors l/m/r and vertical anchors t/m/s/b."""
    x, y = xy
    advances = [draw.textlength(c, font=font) for c in text]
    spacing = int(font.size * tracking_em)
    total = sum(advances) + spacing * (max(0, len(text) - 1))
    if anchor[0] == "m": x -= total // 2
    elif anchor[0] == "r": x -= total
    asc, dsc = font.getmetrics()
    v = anchor[1] if len(anchor) > 1 else "t"
    if v in ("t", "a"):
        baseline = y + asc
    elif v == "m":
        baseline = y + asc // 2 + dsc // 2
    elif v in ("s", "b"):
        baseline = y
    else:
        baseline = y + asc
    cur = x
    for ch, w in zip(text, advances):
        draw.text((cur, baseline), ch, font=font, fill=color, anchor="ls")
        cur += w + spacing
    return total

def measure_tracked(draw, text, font, tracking_em):
    if not text: return 0
    s = int(font.size * tracking_em)
    return sum(draw.textlength(c, font=font) for c in text) + s * (len(text) - 1)

# ── SS monogram (matches the site CSS lockup: two same-size S's, the
#    second offset LEFT −0.44em and DOWN +0.22em into the first) ─────────
def draw_monogram(draw, cx, cy, size, color):
    font = F(CG_MED, size)
    asc, _ = font.getmetrics()
    cap_h = int(asc * 0.70)         # rough cap-height for Cormorant
    s_w = draw.textlength("S", font=font)
    em = size

    # Site-CSS overlap math: letter-spacing -0.1em + margin-left -0.34em = -0.44em
    overlap = int(em * 0.44)
    cluster_w = s_w * 2 - overlap
    drop_y = int(em * 0.22)
    cluster_h = cap_h + drop_y

    # Center cluster around (cx, cy)
    baseline_a = cy + cluster_h // 2 - drop_y          # first-S baseline
    first_x = int(cx - cluster_w / 2)
    draw.text((first_x, baseline_a), "S", font=font, fill=color, anchor="ls")

    second_x = first_x + int(s_w) - overlap
    baseline_b = baseline_a + drop_y                   # second-S baseline (dropped)
    draw.text((second_x, baseline_b), "S", font=font, fill=color, anchor="ls")

    return (first_x, baseline_a - cap_h, first_x + cluster_w, baseline_b)

# ── Slat motif (faint venetian-blind echo) ──────────────────────────────
def slat_band(width, height, n=5, color=BRASS, alpha=0.20):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    step = height / (n + 1)
    rgba = color + (int(255 * alpha),)
    for i in range(1, n + 1):
        y = int(step * i)
        d.rectangle([(0, y), (width, y + 1)], fill=rgba)
    return img

# ── FRONT (cream side — brand + what we do) ─────────────────────────────
def render_front(with_bleed=True):
    W, H = (BLEED_W, BLEED_H) if with_bleed else (TRIM_W, TRIM_H)
    img = Image.new("RGB", (W, H), CREAM)

    # Subtle warm-tone gradient (top cream → bottom slightly deeper)
    import numpy as np
    yy, _ = np.indices((H, W))
    t = (yy / H) * 0.35
    r = CREAM[0] + (CREAM_2[0] - CREAM[0]) * t
    g = CREAM[1] + (CREAM_2[1] - CREAM[1]) * t
    b = CREAM[2] + (CREAM_2[2] - CREAM[2]) * t
    img = Image.fromarray(np.stack([r, g, b], axis=-1).astype("uint8"))

    draw = ImageDraw.Draw(img)
    ox = BLEED if with_bleed else 0
    oy = BLEED if with_bleed else 0
    cx = ox + TRIM_W // 2

    # ── Top stamps (mono caps) — corner identifiers ──
    stamp_font = F(MONO, 22)
    stamp_y = oy + 30
    draw_tracked(draw, (ox + 50, stamp_y), "EST. GALLATIN",
                 stamp_font, BRASS, tracking_em=0.32, anchor="lt")
    draw_tracked(draw, (ox + TRIM_W - 50, stamp_y), "TENNESSEE",
                 stamp_font, BRASS, tracking_em=0.32, anchor="rt")

    # ── Monogram, vertically positioned at ~30% of height ──
    mono_size = int(TRIM_H * 0.38)      # ~228 px
    mono_cy = oy + int(TRIM_H * 0.30)
    mb = draw_monogram(draw, cx, mono_cy, mono_size, INK)
    monogram_bottom = mb[3]

    # ── Wordmark "STATELY SHADES" — DISPLAY size (~24pt printed) ──
    wm_size = 84
    wm_font = F(CG_REG, wm_size)
    wm_text = "STATELY SHADES"
    wm_y = monogram_bottom + 18
    draw_tracked(draw, (cx, wm_y), wm_text, wm_font, INK,
                 tracking_em=0.10, anchor="mt")
    wm_asc, _ = wm_font.getmetrics()
    wm_baseline = wm_y + wm_asc

    # ── Brass rule ──
    rule_w = 90
    rule_y = wm_baseline + 22
    draw.rectangle([(cx - rule_w // 2, rule_y),
                    (cx + rule_w // 2, rule_y + 2)], fill=BRASS)

    # ── SERVICE LINE — what we actually do, italic display ──
    svc_font = F(CG_IT, 36)             # ~10pt printed — readable
    svc_text = "Blinds · Shutters · Motorized Shades"
    svc_y = rule_y + 18
    draw_tracked(draw, (cx, svc_y), svc_text, svc_font, INK,
                 tracking_em=0.04, anchor="mt")
    svc_asc, _ = svc_font.getmetrics()
    svc_baseline = svc_y + svc_asc

    # ── Sub-identifier (mono caps — family-owned positioning) ──
    sub_font = F(MONO, 19)              # ~5.5pt printed — small but legible
    sub_text = "FAMILY-OWNED CUSTOM INSTALLATION · MIDDLE TENNESSEE"
    sub_y = svc_baseline + 18
    draw_tracked(draw, (cx, sub_y), sub_text, sub_font, BRASS,
                 tracking_em=0.28, anchor="mt")

    # ── Slat motif near bottom (more visible than before) ──
    slat = slat_band(TRIM_W - 200, 38, n=5, color=BRASS, alpha=0.20)
    img.paste(slat, (ox + 100, oy + TRIM_H - 60), slat)

    return img

# ── BACK (espresso side — contact + services menu) ──────────────────────
def render_back(with_bleed=True):
    W, H = (BLEED_W, BLEED_H) if with_bleed else (TRIM_W, TRIM_H)
    import numpy as np
    # Diagonal warm-gradient: top-left INK_2 lifted toward INK at bottom-right
    yy, xx = np.indices((H, W))
    t = (1.0 - (xx + yy) / (W + H)) * 0.55
    r = INK[0] + (INK_2[0] - INK[0]) * t
    g = INK[1] + (INK_2[1] - INK[1]) * t
    b = INK[2] + (INK_2[2] - INK[2]) * t
    img = Image.fromarray(np.stack([r, g, b], axis=-1).astype("uint8"))

    draw = ImageDraw.Draw(img)
    ox = BLEED if with_bleed else 0
    oy = BLEED if with_bleed else 0

    # 55/45 column split with a thin brass divider
    split_x = ox + int(TRIM_W * 0.55)
    div = Image.new("RGBA", (1, TRIM_H - 100), (BRASS[0], BRASS[1], BRASS[2], 140))
    img.paste(div, (split_x, oy + 50), div)
    # Brass diamond at divider midpoint
    dx, dy = split_x, oy + TRIM_H // 2
    ds = 6
    draw.polygon([(dx, dy - ds), (dx + ds, dy), (dx, dy + ds), (dx - ds, dy)],
                 fill=BRASS_HOT)

    # ─────────────────── LEFT: name + role + brass rule + contact stack
    L = ox + 56
    top = oy + 76

    # Name — display serif, large for hold-in-hand readability
    name_font = F(CG_MED, 64)           # ~18pt
    draw_tracked(draw, (L, top), "MICHAEL BLAIR", name_font, CHAMPAGNE,
                 tracking_em=0.05, anchor="lt")
    name_asc, _ = name_font.getmetrics()
    name_baseline = top + name_asc

    # Role — italic display
    role_font = F(CG_MIT, 30)           # ~9pt
    role_text = "Sales & Installation"
    role_y = name_baseline + 6
    draw.text((L, role_y), role_text, font=role_font, fill=BRASS_HOT, anchor="lt")
    role_asc, _ = role_font.getmetrics()
    role_baseline = role_y + role_asc

    # Brass rule under role
    rule_y = role_baseline + 22
    draw.rectangle([(L, rule_y), (L + 90, rule_y + 2)], fill=BRASS)

    # Phone — the most-pressed key, given display weight
    phone_font = F(CG_MED, 46)          # ~13pt — biggest contact item
    phone_y = rule_y + 26
    draw.text((L, phone_y), "629.298.8241", font=phone_font, fill=CHAMPAGNE, anchor="lt")
    p_asc, _ = phone_font.getmetrics()
    phone_baseline = phone_y + p_asc

    # Email — mono caps, slightly muted champagne
    detail_font = F(MONO, 22)           # ~6.5pt
    softer = tuple(int(c * 0.92) for c in CHAMPAGNE)
    email_y = phone_baseline + 18
    draw_tracked(draw, (L, email_y), "HELLO@STATELYSHADES.COM",
                 detail_font, softer, tracking_em=0.08, anchor="lt")
    e_asc, _ = detail_font.getmetrics()

    # Web — directly under email
    web_y = email_y + e_asc + 8
    draw_tracked(draw, (L, web_y), "STATELYSHADES.COM",
                 detail_font, softer, tracking_em=0.08, anchor="lt")

    # Location stamp anchored at bottom-left
    loc_font = F(MONO, 18)              # ~5.5pt
    loc_y = oy + TRIM_H - 60
    draw_tracked(draw, (L, loc_y), "GALLATIN · TENNESSEE",
                 loc_font, BRASS, tracking_em=0.30, anchor="lt")

    # ─────────────────── RIGHT: SS monogram + services menu
    R_L = split_x + 50
    R_R = ox + TRIM_W - 50
    rcx = (R_L + R_R) // 2

    # Small champagne monogram
    sm_mono_size = 110
    smb = draw_monogram(draw, rcx, oy + 100, sm_mono_size, CHAMPAGNE)
    smb_bottom = smb[3]

    # "WHAT WE INSTALL" header
    head_font = F(MONO, 16)             # ~4.7pt
    head_y = smb_bottom + 26
    draw_tracked(draw, (rcx, head_y), "WHAT WE INSTALL",
                 head_font, BRASS_HOT, tracking_em=0.34, anchor="mt")
    head_asc, _ = head_font.getmetrics()

    # Tiny rule under header
    sm_rule_y = head_y + head_asc + 10
    sm_rule_w = 32
    draw.rectangle([(rcx - sm_rule_w // 2, sm_rule_y),
                    (rcx + sm_rule_w // 2, sm_rule_y + 1)], fill=BRASS)

    # Services list — italic display, stacked, centered
    svc_list = [
        "Plantation Shutters",
        "Motorized Shades",
        "Custom Drapery",
        "Repair & Install-Only",
    ]
    svc_font2 = F(CG_IT, 26)            # ~7.5pt
    svc_start_y = sm_rule_y + 18
    line_gap = 12
    svc_asc, _ = svc_font2.getmetrics()
    cy_cursor = svc_start_y
    for line in svc_list:
        draw.text((rcx, cy_cursor), line, font=svc_font2, fill=CHAMPAGNE, anchor="mt")
        cy_cursor += svc_asc + line_gap

    return img

# ── Build outputs ───────────────────────────────────────────────────────
def main():
    out = ROOT
    front_trim = render_front(with_bleed=False)
    back_trim  = render_back(with_bleed=False)
    front_trim.save(out / "card-front.png", "PNG", optimize=True)
    back_trim.save(out / "card-back.png", "PNG", optimize=True)
    print(f"  ✓ card-front.png ({front_trim.size})")
    print(f"  ✓ card-back.png  ({back_trim.size})")

    front_bleed = render_front(with_bleed=True)
    back_bleed  = render_back(with_bleed=True)
    front_bleed.save(out / "card-front-bleed.png", "PNG", optimize=True)
    back_bleed.save(out / "card-back-bleed.png", "PNG", optimize=True)
    print(f"  ✓ card-front-bleed.png ({front_bleed.size})")
    print(f"  ✓ card-back-bleed.png  ({back_bleed.size})")

    pdf_path = out / "card-print.pdf"
    c = rl_canvas.Canvas(str(pdf_path), pagesize=(3.75 * inch, 2.25 * inch))
    c.drawImage(str(out / "card-front-bleed.png"), 0, 0,
                width=3.75 * inch, height=2.25 * inch)
    c.showPage()
    c.drawImage(str(out / "card-back-bleed.png"), 0, 0,
                width=3.75 * inch, height=2.25 * inch)
    c.showPage()
    c.save()
    print(f"  ✓ card-print.pdf (2 pages, 3.75×2.25 in with bleed)")

if __name__ == "__main__":
    main()
