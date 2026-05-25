#!/bin/bash
# Hero photos for affordable + install-only Journal posts
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

generate "affordable-faux-wood" \
  "Bright, welcoming Tennessee kitchen with crisp white 2.5-inch custom faux wood blinds on three windows above a marble subway-tile backsplash. Affordable but tailored — clean horizontal slats, cordless lift, white finish. Sun-filled morning light, walnut floors, brass cabinet hardware, simple flowers in a vase on the island. Photorealistic, no people, editorial real-estate-photography style, warm cream and walnut palette, hyper-detailed faux wood slat texture" \
  1280 720 &

generate "install-only-service" \
  "Editorial close-up photograph of two skilled hands installing a custom blind on a window inside a clean modern Tennessee home. One hand holds the headrail level against the casing, the other tightens a mounting bracket with a cordless drill. Unopened blinds boxes from a home-improvement retailer stacked neatly on the floor nearby, brown packaging, professional drop cloth, drill set, level laid out. Soft daylight from the window, white casings, walnut floor, no faces visible. Photorealistic editorial photography, hyper-detailed, warm neutral palette" \
  1280 720 &

wait
echo "[done] converting to WebP..."
for f in "$OUT_DIR"/affordable-faux-wood.png "$OUT_DIR"/install-only-service.png; do
  cwebp -q 82 -m 6 "$f" -o "${f%.png}.webp" 2>/dev/null && rm "$f"
done
ls -lh "$OUT_DIR"/affordable-faux-wood.webp "$OUT_DIR"/install-only-service.webp
