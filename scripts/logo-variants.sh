#!/bin/bash
# Generate logo variants from the original Stately Shades logo:
#   logo-dark.png  — dark espresso text on transparent (for navbar / light backgrounds)
#   logo-light.png — white/cream text on transparent (for footer / dark backgrounds)

set -e
source ~/.env

OUT_DIR="$HOME/statelyshades-site/assets/images"
SRC="$OUT_DIR/logo.png"

if [ ! -f "$SRC" ]; then
  echo "[err] source logo not found at $SRC"
  exit 1
fi

# Base64-encode source image
SRC_B64=$(base64 < "$SRC" | tr -d '\n')

edit_variant() {
  local name="$1"
  local prompt="$2"
  echo "[edit] $name..."
  jq -n \
    --arg m "nano-banana-pro-edit" \
    --arg i "$SRC_B64" \
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

# Dark variant (for light navbar)
edit_variant "logo-dark" \
  "Remove the solid black background from this logo completely, making it fully transparent (alpha 0). Recolor all the white text (the SS monogram and the STATELY SHADES wordmark) to a deep dark espresso color (#14110D). Recolor the cream/champagne tagline 'CUSTOM BLINDS, SHUTTERS & SHADES' and the thin divider line to a warm brass color (#9D7A3E). Preserve the exact typography, composition, proportions, and serif style. Output: PNG with transparent background." &

# Light variant (for dark footer)
edit_variant "logo-light" \
  "Remove the solid black background from this logo completely, making it fully transparent (alpha 0). Keep the white text (SS monogram and STATELY SHADES wordmark) exactly as white (#F7F2EA). Keep the cream/champagne tagline and divider line in their original warm cream/champagne color. Preserve the exact typography, composition, proportions, and serif style. Output: PNG with transparent background." &

wait
echo "[done] both variants generated"
ls -lh "$OUT_DIR"/logo-*.png 2>/dev/null
