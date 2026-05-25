#!/bin/bash
# Generate hero photography for the 9 product-type Journal posts via Venice.ai
# Atelier Boutique aesthetic: espresso/oat/champagne, Tennessee golden hour,
# Architectural Digest editorial style. No people, photorealistic, 1280x720 each.

set -e
source ~/.env

MODEL="nano-banana-pro"
OUT_DIR="$HOME/statelyshades-site/assets/images/blog"
mkdir -p "$OUT_DIR"

generate() {
  local name="$1"
  local prompt="$2"
  local width="${3:-1280}"
  local height="${4:-720}"
  echo "[gen] $name (${width}x${height})..."
  curl -sS -X POST "$VENICE_API_BASE/image/generate" \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$(jq -n --arg m "$MODEL" --arg p "$prompt" --argjson w "$width" --argjson h "$height" \
      '{model:$m, prompt:$p, width:$w, height:$h, format:"png"}')" \
    -o "/tmp/venice_blog_${name}.json"
  jq -r '.images[0]' "/tmp/venice_blog_${name}.json" | base64 -d > "$OUT_DIR/${name}.png"
  local size=$(wc -c < "$OUT_DIR/${name}.png")
  echo "[gen] $name -> $OUT_DIR/${name}.png ($size bytes)"
  if [ "$size" -lt 5000 ]; then
    echo "[ERR] $name file too small. Response head:"
    head -c 500 "/tmp/venice_blog_${name}.json"
    echo ""
  fi
}

# Run all 9 in parallel
generate "plantation-shutters" \
  "Architectural Digest editorial photograph of a refined Tennessee dining room with classic white hardwood plantation shutters on tall windows. Wide 3.5-inch louvers tilted partially open, soft warm golden-hour light filtering through onto a walnut dining table. Linen upholstered chairs, brass pendant lights, oat-toned walls. Restrained luxury, espresso-cream-champagne palette. Photorealistic, no people, ultra-detailed shutter louver texture, cinematic warm light, shallow depth of field" \
  1280 720 &

generate "motorized-shades" \
  "Editorial photograph of a modern luxury great room in Tennessee with floor-to-ceiling windows and three sleek motorized roller shades in warm taupe, each descended to a different height in a synchronized choreography. Walnut floors, low linen sofa, brass coffee table, sunset light streaming through the partially raised shades. Refined neutral palette, Restoration Hardware vibes, photorealistic, no people, cinematic warm lighting, ultra-detailed" \
  1280 720 &

generate "cellular-shades" \
  "Quiet luxury Tennessee primary bedroom in soft morning light. Top-down/bottom-up cellular honeycomb shades on tall windows, lowered halfway from the top with the bottom raised — the room glows with diffused light from above. Cream linen bedding, walnut nightstand, brass sconces, oat-colored walls. Photorealistic Architectural Digest editorial photography, no people, ultra-detailed honeycomb pleat texture, warm cream and champagne palette" \
  1280 720 &

generate "outdoor-shades" \
  "Elegant covered Tennessee porch at dusk with motorized retractable outdoor sun shades in warm tan tone, lowered three-quarters to filter golden-amber sunset light. Wicker lounge chairs with cream linen cushions, stone fireplace with kindled fire, walnut tongue-and-groove ceiling, view of rolling Tennessee countryside beyond. Sophisticated outdoor living room, photorealistic editorial photography, no people, hyper-detailed" \
  1280 720 &

generate "sheer-vanes" \
  "Architectural Digest interior photograph of a refined Tennessee living room with Hunter Douglas Silhouette-style sheer fabric shades on tall picture windows. Soft fabric vanes float between sheer panels, diffusing golden afternoon light into a glow. Cream linen sofa, brass coffee table, vintage rug, framed botanical prints. Quiet luxury palette of cream, oat, champagne, espresso. Photorealistic, no people, ultra-detailed sheer textile texture, cinematic warm light, shallow depth of field" \
  1280 720 &

generate "zebra-solar" \
  "Modern luxury Tennessee dining nook with dual-layer zebra banded shades on tall windows, the alternating sheer and opaque bands aligned to filter view from the outside while letting in diffused light. Walnut breakfast table, cream linen chairs, brass pendant, oat-toned walls. Crisp modern aesthetic, photorealistic editorial photography, no people, ultra-detailed zebra fabric texture, warm natural light" \
  1280 720 &

generate "woven-wood" \
  "Editorial interior photograph of a refined Tennessee sitting room with hand-loomed woven wood bamboo shades on a tall arched window. Natural bamboo, grass, and jute texture catches warm afternoon light. Linen reading chair in cream, brass arc floor lamp, walnut side table, botanical art. Organic warmth meets quiet luxury, Architectural Digest style, photorealistic, no people, hyper-detailed natural bamboo weave texture" \
  1280 720 &

generate "wood-blinds-drapery" \
  "Architectural Digest editorial photograph of a luxury Tennessee primary bedroom with custom 2.5-inch hardwood blinds on the side windows and floor-to-ceiling cream linen drapery panels on the larger center window. The drapery rod is ceiling-mounted, panels gracefully puddle to the floor. Walnut bed, cream linen bedding, brass sconces, oat-toned walls. Warm golden afternoon light. Photorealistic, no people, ultra-detailed fabric texture, soft cinematic light, restrained luxurious decor" \
  1280 720 &

generate "repair-service" \
  "Editorial close-up detail photograph of a Stately Shades technician's hands carefully restringing a hardwood plantation shutter louver mechanism on a workbench. Brass-finish tools laid out neatly, replacement tilt rod and lift cord visible, a section of white plantation shutter with louvers being serviced. Walnut workbench, soft window light. Photorealistic, hyper-detailed, ultra-precise craftsmanship aesthetic, warm cream and brass palette, Architectural Digest editorial styling" \
  1280 720 &

wait
echo ""
echo "[done] all PNGs generated, converting to WebP..."

if command -v cwebp >/dev/null 2>&1; then
  for f in "$OUT_DIR"/*.png; do
    cwebp -q 82 -m 6 "$f" -o "${f%.png}.webp" 2>/dev/null && rm "$f"
  done
  echo "[done] WebP conversion complete"
else
  echo "[warn] cwebp not installed — keeping PNGs"
fi

ls -lh "$OUT_DIR"
