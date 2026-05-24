# Stately Shades

Custom blinds, plantation shutters, and shades — family-owned in Gallatin, Tennessee.

**Live:** https://statelyshades.com
**Hosting:** Cloudflare Pages (project: `statelyshades`)
**Service area:** 90-mile radius from Gallatin, TN
**Phone/Text:** +1 629-298-8241

## Local development

Static site — open `index.html` directly, or:

```bash
python3 -m http.server 8000
```

## Hero & product imagery

Run `bash scripts/generate-images.sh` (requires Venice.ai credits) to regenerate
the hero + product photography. Outputs land in `assets/images/`.

If images are missing, the site gracefully falls back to a brand-themed SVG
placeholder via `script.js`.

## Deploy

```bash
CLOUDFLARE_API_KEY=$CLOUDFLARE_API_KEY CLOUDFLARE_EMAIL=$CLOUDFLARE_EMAIL \
  npx wrangler pages deploy . --project-name=statelyshades
```

## Form submissions

The contact form posts to Formspree. Update the `action` attribute on the
`<form>` in `index.html` with your real Formspree endpoint before launch.
