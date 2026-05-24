#!/bin/bash
set -e
source ~/.env

OUT_DIR="$HOME/statelyshades-site/assets/images"
NAME="specialty-zebra-shades"

PROMPT="Editorial luxury interior photograph of zebra shades on tall windows in a refined Tennessee dining area at golden hour. Alternating sheer and opaque horizontal fabric bands creating a softly striped light pattern across a walnut dining table. Modern minimalist styling, warm cream and oat-toned walls, brass pendant light, neutral linen-upholstered chairs. Architectural Digest editorial photography, photorealistic, no people, ultra-detailed sheer fabric texture, shallow depth of field, warm cinematic light, Restoration Hardware aesthetic."

echo "[gen] $NAME..."
curl -sS -X POST "$VENICE_API_BASE/image/generate" \
  -H "Authorization: Bearer $VENICE_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg p "$PROMPT" '{model:"nano-banana-pro", prompt:$p, width:1080, height:1080, format:"png"}')" \
  -o "/tmp/venice_${NAME}.json"

jq -r '.images[0]' "/tmp/venice_${NAME}.json" | base64 -d > "$OUT_DIR/${NAME}.png"
SIZE=$(wc -c < "$OUT_DIR/${NAME}.png")
echo "[gen] $NAME -> $OUT_DIR/${NAME}.png ($SIZE bytes)"

if [ "$SIZE" -lt 5000 ]; then
  echo "[ERR] $NAME too small:"
  head -c 500 "/tmp/venice_${NAME}.json"
  exit 1
fi

# Convert to WebP and remove PNG
if command -v cwebp >/dev/null 2>&1; then
  cwebp -q 82 -m 6 "$OUT_DIR/${NAME}.png" -o "$OUT_DIR/${NAME}.webp" 2>/dev/null
  rm "$OUT_DIR/${NAME}.png"
  echo "[done] $OUT_DIR/${NAME}.webp"
fi
