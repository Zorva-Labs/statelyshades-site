#!/bin/bash
# Hero photos for the 4 SEO/AEO/GEO-targeted Journal posts
set -e
source ~/.env
MODEL="nano-banana-pro"
OUT_DIR="$HOME/statelyshades-site/assets/images/blog"
mkdir -p "$OUT_DIR"

generate() {
  local name="$1"; local prompt="$2"; local w="${3:-1280}"; local h="${4:-720}"
  echo "[gen] $name..."
  curl -sS -X POST "$VENICE_API_BASE/image/generate" \
    -H "Authorization: Bearer $VENICE_API_KEY" -H "Content-Type: application/json" \
    -d "$(jq -n --arg m "$MODEL" --arg p "$prompt" --argjson w "$w" --argjson h "$h" \
      '{model:$m, prompt:$p, width:$w, height:$h, format:"png"}')" \
    -o "/tmp/venice_${name}.json"
  jq -r '.images[0]' "/tmp/venice_${name}.json" | base64 -d > "$OUT_DIR/${name}.png"
  echo "[gen] $name ($(wc -c < "$OUT_DIR/${name}.png") bytes)"
}

generate "rental-property-blinds" \
  "Clean modern rental-property apartment living room with crisp white faux wood blinds on three large windows. Neutral oat-toned walls, a simple gray linen couch, walnut floors, no clutter — looks like a freshly-turned-over rental ready for the next tenant. Soft daylight through the half-raised blinds, no people, photorealistic editorial real-estate-photography style, hyper-detailed faux wood slat texture, warm afternoon light, sense of newness and value" \
  1280 720 &

generate "professional-installer-detail" \
  "Editorial close-up of a professional installer's hands working at a Tennessee window, threading a custom blind's hidden lift cord through the headrail with precision. Brass-handled tools, level, measuring tape laid out neatly on a clean canvas drop cloth. Daylight through the open window casing, walnut floor below, no faces visible. Photorealistic hyper-detailed craftsmanship aesthetic, warm cream and brass palette, Architectural Digest editorial styling" \
  1280 720 &

wait
echo "[done] converting to WebP..."
for f in "$OUT_DIR"/rental-property-blinds.png "$OUT_DIR"/professional-installer-detail.png; do
  cwebp -q 82 -m 6 "$f" -o "${f%.png}.webp" 2>/dev/null && rm "$f"
done
ls -lh "$OUT_DIR"/rental-property-blinds.webp "$OUT_DIR"/professional-installer-detail.webp
