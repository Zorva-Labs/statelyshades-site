#!/bin/bash
# Regenerate logo variants from the authoritative statelylogo.png:
#   logo-dark.webp  — dark text on transparent (for navbar / light backgrounds)
#   logo-light.webp — cream text on transparent (for footer / dark backgrounds)

set -e
source ~/.env

OUT_DIR="$HOME/statelyshades-site/assets/images"
SRC="$OUT_DIR/logo.png"

if [ ! -f "$SRC" ]; then
  echo "[err] source logo not found at $SRC"
  exit 1
fi

SRC_B64_FILE="/tmp/stately_logo_b64.txt"
base64 < "$SRC" | tr -d '\n' > "$SRC_B64_FILE"

edit_variant() {
  local name="$1"
  local prompt="$2"
  echo "[edit] $name..."
  jq -n \
    --arg m "nano-banana-pro-edit" \
    --rawfile i "$SRC_B64_FILE" \
    --arg p "$prompt" \
    '{model:$m, image:$i, prompt:$p, aspect_ratio:"auto"}' > "/tmp/venice_${name}_body.json"

  curl -sS -X POST "$VENICE_API_BASE/image/edit" \
    -H "Authorization: Bearer $VENICE_API_KEY" \
    -H "Content-Type: application/json" \
    --data-binary "@/tmp/venice_${name}_body.json" \
    -o "$OUT_DIR/${name}.png"

  local size=$(wc -c < "$OUT_DIR/${name}.png")
  echo "[edit] $name -> $OUT_DIR/${name}.png ($size bytes)"
  if [ "$size" -lt 5000 ]; then
    echo "[ERR] $name too small, response:"
    head -c 500 "$OUT_DIR/${name}.png"
    echo ""
  fi
}

# Dark variant (for light navbar) — just strip the cream background, keep colors
edit_variant "logo-dark" \
  "Remove the off-white/cream background from this logo completely, making it fully transparent (alpha channel 0). Keep all the existing dark text (the SS monogram and the STATELY SHADES wordmark) and the warm brass/champagne accents (divider line and small tagline) exactly as they are — same color, same position, same typography. Output: PNG with transparent background." &

# Light variant (for dark footer) — strip bg + recolor dark text to cream
edit_variant "logo-light" \
  "Remove the off-white/cream background from this logo completely, making it fully transparent (alpha channel 0). Recolor the dark SS monogram and the STATELY SHADES wordmark text to warm white/cream (#F7F2EA). Keep the warm brass/champagne divider line and small CUSTOM BLINDS, SHUTTERS & SHADES tagline exactly as they are. Preserve typography, proportions, and composition. Output: PNG with transparent background." &

wait
echo "[done] both variants generated"

# Convert to WebP
if command -v cwebp >/dev/null 2>&1; then
  for v in logo-dark logo-light; do
    if [ -f "$OUT_DIR/${v}.png" ]; then
      cwebp -q 90 -m 6 -alpha_q 100 "$OUT_DIR/${v}.png" -o "$OUT_DIR/${v}.webp" 2>/dev/null && rm "$OUT_DIR/${v}.png"
      echo "[webp] $OUT_DIR/${v}.webp"
    fi
  done
fi

ls -lh "$OUT_DIR"/logo* 2>/dev/null
