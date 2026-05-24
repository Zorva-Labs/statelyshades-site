#!/usr/bin/env bash
# Deploy Stately Shades to Cloudflare Pages AND purge the zone cache in one shot.
#
# Without the purge, the Pages origin updates but Cloudflare's edge CDN keeps
# serving stale CSS/JS/HTML for a while — which is what causes the "I deployed
# but the live site looks old" lag.
#
# Usage:
#   bash scripts/deploy.sh                  # production (statelyshades.com)
#   bash scripts/deploy.sh preview          # preview branch, no purge
#   bash scripts/deploy.sh --no-purge       # production, skip the purge step

set -euo pipefail

# ---- Config ----------------------------------------------------------------
PROJECT="statelyshades"
ZONE_ID="bb1ad7575de5c8fe2140b884aa44ec5e"
PROD_DOMAIN="statelyshades.com"

# ---- Args ------------------------------------------------------------------
BRANCH="main"
DO_PURGE="yes"
for arg in "$@"; do
  case "$arg" in
    preview)    BRANCH="preview"; DO_PURGE="no" ;;
    --no-purge) DO_PURGE="no" ;;
    -h|--help)
      head -16 "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "Unknown arg: $arg" >&2; exit 1 ;;
  esac
done

# ---- Env -------------------------------------------------------------------
# shellcheck disable=SC1090
source "$HOME/.env"
: "${CLOUDFLARE_API_KEY:?missing}"
: "${CLOUDFLARE_EMAIL:?missing}"

# ---- cd to project root (this script's parent) -----------------------------
cd "$(dirname "$0")/.."

# ---- 1. Deploy via wrangler -----------------------------------------------
echo "▶︎ Deploying to Cloudflare Pages (branch=$BRANCH)..."
DEPLOY_OUTPUT=$(CLOUDFLARE_API_KEY="$CLOUDFLARE_API_KEY" \
                CLOUDFLARE_EMAIL="$CLOUDFLARE_EMAIL" \
                npx --yes wrangler@latest pages deploy . \
                  --project-name="$PROJECT" \
                  --commit-dirty=true \
                  --branch="$BRANCH" 2>&1)
echo "$DEPLOY_OUTPUT" | tail -8

DEPLOY_URL=$(echo "$DEPLOY_OUTPUT" | grep -oE 'https://[a-f0-9]+\.statelyshades\.pages\.dev' | head -1 || true)

# ---- 2. Purge Cloudflare cache (production only) ---------------------------
if [ "$BRANCH" = "main" ] && [ "$DO_PURGE" = "yes" ]; then
  echo ""
  echo "▶︎ Purging Cloudflare cache for $PROD_DOMAIN..."
  PURGE_RESULT=$(curl -fsS -X POST \
    "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
    -H "X-Auth-Email: $CLOUDFLARE_EMAIL" \
    -H "X-Auth-Key: $CLOUDFLARE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"purge_everything": true}')
  if echo "$PURGE_RESULT" | grep -q '"success":true'; then
    PURGE_ID=$(echo "$PURGE_RESULT" | sed -E 's/.*"id":"([^"]+)".*/\1/' | head -c 32)
    echo "  ✓ Cache purged (id: $PURGE_ID)"
  else
    echo "  ✗ Purge failed:"
    echo "$PURGE_RESULT"
    exit 1
  fi
fi

# ---- 3. Summary ------------------------------------------------------------
echo ""
echo "─────────────────────────────────────────────────────"
if [ -n "$DEPLOY_URL" ]; then
  echo "  Deploy URL:  $DEPLOY_URL"
fi
if [ "$BRANCH" = "main" ]; then
  echo "  Production:  https://$PROD_DOMAIN"
fi
echo "─────────────────────────────────────────────────────"
