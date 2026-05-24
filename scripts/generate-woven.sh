#!/bin/bash
set -e
source ~/.env

OUT_DIR="$HOME/statelyshades-site/assets/images"
NAME="woven-wood-naturals"

PROMPT="Editorial luxury interior photograph of woven wood bamboo shades on a tall arched window in a refined Tennessee sitting room at golden hour. Hand-woven natural bamboo and grass shade rolled halfway down, soft warm light filtering through the woven reeds creating an organic textured glow. Linen-upholstered reading chair in oat with cream throw, walnut side table with ceramic mug, brass arc floor lamp, framed botanical prints on the wall, neutral cream and warm-natural palette, walnut sideboard. Photorealistic interior photography, no people, no text, no captions, no watermarks, no magazine overlays, no logos, no signatures, no UI elements — just the room. Ultra-detailed natural fiber weave texture, shallow depth of field, warm cinematic light, refined luxury residential aesthetic."

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

if command -v cwebp >/dev/null 2>&1; then
  cwebp -q 82 -m 6 "$OUT_DIR/${NAME}.png" -o "$OUT_DIR/${NAME}.webp" 2>/dev/null
  rm "$OUT_DIR/${NAME}.png"
  echo "[done] $OUT_DIR/${NAME}.webp"
fi
