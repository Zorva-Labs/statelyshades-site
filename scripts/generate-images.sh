#!/bin/bash
# Generate hero + product imagery for Stately Shades via Venice.ai
# Atelier Boutique direction: espresso/oat/champagne, Tennessee golden hour, refined luxury

set -e
source ~/.env

MODEL="nano-banana-pro"
OUT_DIR="$HOME/statelyshades-site/assets/images"
mkdir -p "$OUT_DIR"

generate() {
  local name="$1"
  local prompt="$2"
  local width="${3:-1280}"
  local height="${4:-800}"
  echo "[gen] $name (${width}x${height})..."
  curl -sS -X POST "$VENICE_API_BASE/image/generate" \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$(jq -n --arg m "$MODEL" --arg p "$prompt" --argjson w "$width" --argjson h "$height" \
      '{model:$m, prompt:$p, width:$w, height:$h, format:"png"}')" \
    -o "/tmp/venice_${name}.json"
  # extract base64 image
  jq -r '.images[0]' "/tmp/venice_${name}.json" | base64 -d > "$OUT_DIR/${name}.png"
  local size=$(wc -c < "$OUT_DIR/${name}.png")
  echo "[gen] $name -> $OUT_DIR/${name}.png ($size bytes)"
  if [ "$size" -lt 5000 ]; then
    echo "[ERR] $name file too small, showing response:"
    head -c 500 "/tmp/venice_${name}.json"
    echo ""
  fi
}

# Run in parallel
generate "hero-shades-opening" \
  "Cinematic luxury interior photograph, refined Tennessee dining room at golden hour. Floor-to-ceiling windows with elegant cream linen motorized roller shades half-raised, revealing rolling Tennessee countryside in distance. Long live-edge walnut dining table, vintage brass pendant lighting, neutral oat-toned walls, restrained sophistication. Soft warm golden light streaming through. Architectural Digest editorial photography style, shallow depth of field, ultra-high-end residential interior, no people, hyper-detailed, photorealistic" \
  1280 720 &

generate "plantation-shutters-living" \
  "Editorial interior photograph of a refined Tennessee living room with classic white plantation shutters on tall windows. Wide louvered shutters slightly angled, soft warm light filtering through. Linen sofa in oatmeal, brass coffee table, framed art, restrained luxurious decor in espresso, cream and champagne tones. Architectural Digest style, photorealistic, no people, golden hour, warm cinematic lighting" \
  1080 1080 &

generate "cellular-shades-bedroom" \
  "Serene luxury bedroom in soft morning light, cellular honeycomb shades on tall windows diffusing gentle light into a glow. Neutral linen bedding, walnut nightstand, brass sconces, oat-colored walls. Quiet luxury aesthetic. Photorealistic editorial interior photography, no people, ultra-detailed textile texture on the cellular shade pleats, warm cream and champagne palette" \
  1080 1080 &

generate "motorized-blinds-modern" \
  "Modern luxury great room with floor-to-ceiling windows. Sleek motorized roller shades in warm taupe descending halfway, controlled by a hand holding a small designer remote in soft focus foreground. Open-plan living, walnut floors, refined neutral palette. Cinematic warm light, photorealistic editorial interior photography, ultra-detailed, Restoration Hardware vibes" \
  1080 1080 &

generate "outdoor-shades-porch" \
  "Elegant covered Tennessee porch at dusk with rolled-down outdoor sun shades in warm tan tone. Wicker lounge chairs with cream linen cushions, stone fireplace, walnut ceiling. View toward landscaped garden. Warm amber lighting, sophisticated outdoor living, photorealistic editorial photography, no people, high-end residential" \
  1080 1080 &

generate "consultation-detail" \
  "Close-up editorial detail shot of fabric swatches and shade samples arranged on a walnut table. Linen, sheer, blackout textiles in cream, oat, champagne, espresso. Brass measuring tape, leather notebook, ceramic coffee mug. Soft natural window light. Photorealistic, Architectural Digest editorial styling, no people, ultra-detailed textile texture" \
  1080 1080 &

wait
echo "[done] all images generated"
ls -lh "$OUT_DIR"
