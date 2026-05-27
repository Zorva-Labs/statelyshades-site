#!/usr/bin/env python3
"""
Stand-alone SS monogram export — white glyphs, transparent background.

Outputs three sizes for different uses:
- monogram-white-2000.png   2000×2000 — high-res for print, embroidery, etc.
- monogram-white-1024.png   1024×1024 — social avatars, web hero asset
- monogram-white-512.png     512×512  — favicons, signatures, signoff

All have transparent background (alpha=0) outside the glyphs themselves.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).parent
FONTS = ROOT / "fonts"
CG_MED = "CormorantGaramond-Medium.ttf"

WHITE = (255, 255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)

def draw_monogram(draw, cx, cy, size, color):
    """SS lockup matching the site CSS: two same-size S's, the second offset
    -0.44em (overlap) and +0.22em (drop) into the first."""
    font = ImageFont.truetype(str(FONTS / CG_MED), size)
    asc, _ = font.getmetrics()
    cap_h = int(asc * 0.70)
    s_w = draw.textlength("S", font=font)
    em = size

    overlap = int(em * 0.44)
    drop_y  = int(em * 0.22)
    cluster_w = int(s_w * 2 - overlap)
    cluster_h = cap_h + drop_y

    baseline_a = cy + cluster_h // 2 - drop_y
    first_x = int(cx - cluster_w / 2)
    draw.text((first_x, baseline_a), "S", font=font, fill=color, anchor="ls")

    second_x = first_x + int(s_w) - overlap
    baseline_b = baseline_a + drop_y
    draw.text((second_x, baseline_b), "S", font=font, fill=color, anchor="ls")

def render_monogram(canvas_size=2000, glyph_size_ratio=0.70):
    """Render the monogram centered on a transparent canvas.

    `glyph_size_ratio` controls how much of the canvas the cluster fills
    (0.70 = roughly 70% — sensible padding around the mark)."""
    img = Image.new("RGBA", (canvas_size, canvas_size), TRANSPARENT)
    draw = ImageDraw.Draw(img)
    glyph_size = int(canvas_size * glyph_size_ratio)
    cx = cy = canvas_size // 2
    draw_monogram(draw, cx, cy, glyph_size, WHITE)
    return img

def main():
    for size in (2000, 1024, 512):
        img = render_monogram(canvas_size=size)
        out = ROOT / f"monogram-white-{size}.png"
        img.save(out, "PNG", optimize=True)
        print(f"  ✓ {out.name} ({img.size[0]}×{img.size[1]}, transparent)")

if __name__ == "__main__":
    main()
