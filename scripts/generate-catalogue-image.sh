#!/bin/bash
# Hero photo for The Full Catalogue card — showroom samples + materials laid out
set -e
source ~/.env
MODEL="nano-banana-pro"
OUT_DIR="$HOME/statelyshades-site/assets/images/blog"
mkdir -p "$OUT_DIR"

NAME="catalogue-showroom"
PROMPT="Editorial overhead flat-lay of a Stately Shades designer's consultation table at golden hour. Fabric swatches, woven wood samples, faux wood blind slats in white and stained walnut, a small plantation shutter sample with 3.5 inch louvers, a cellular honeycomb shade sample, a brass measuring tape, a leather-bound order book, and a small marble swatch ring catalog — all arranged in a graceful editorial composition on a walnut showroom table. Warm cream and brass palette, soft directional light from the left, no people. Photorealistic Architectural Digest editorial photography, hyper-detailed textile texture, the kind of image that says 'we sell every window treatment'"

echo "[gen] $NAME..."
curl -sS -X POST "$VENICE_API_BASE/image/generate" \
  -H "Authorization: Bearer $VENICE_API_KEY" -H "Content-Type: application/json" \
  -d "$(jq -n --arg m "$MODEL" --arg p "$PROMPT" --argjson w 1280 --argjson h 720 \
    '{model:$m, prompt:$p, width:$w, height:$h, format:"png"}')" \
  -o "/tmp/venice_${NAME}.json"
jq -r '.images[0]' "/tmp/venice_${NAME}.json" | base64 -d > "$OUT_DIR/${NAME}.png"
echo "[gen] $NAME ($(wc -c < "$OUT_DIR/${NAME}.png") bytes)"

cwebp -q 82 -m 6 "$OUT_DIR/${NAME}.png" -o "$OUT_DIR/${NAME}.webp" 2>/dev/null && rm "$OUT_DIR/${NAME}.png"
ls -lh "$OUT_DIR/${NAME}.webp"
