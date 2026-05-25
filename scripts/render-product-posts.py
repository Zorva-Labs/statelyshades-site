#!/usr/bin/env python3
"""Render the remaining product-type Journal posts from a shared template.

Posts 1 (plantation) and 2 (motorized) are hand-written; this script renders
the other 7 from a content table, keeping chrome identical and consistent.
"""

from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
DATE = "2026-05-25"
VERSION = "blog6"

# ------------ Content table -----------------------------------------------

POSTS = [
    {
        "slug": "cellular-honeycomb-shades-guide",
        "title_html": "Cellular &amp; <em>honeycomb shades.</em>",
        "h1_plain": "Cellular & Honeycomb Shades: A Complete Guide",
        "meta_title": "Cellular & Honeycomb Shades: A Complete Guide · Stately Shades",
        "meta_desc": "Single, double, and triple-cell honeycomb shades, blackout liners, top-down/bottom-up, and where Hunter Douglas Duette, Sonnette, and Norman Honeycomb win. From a Gallatin, TN dealer.",
        "eyebrow": "Product Guide · Energy Series",
        "section": "Product Guide",
        "minutes": "7",
        "image": "/assets/images/blog/cellular-shades.webp",
        "image_alt": "Top-down/bottom-up cellular honeycomb shades diffusing morning light in a Tennessee primary bedroom",
        "caption": "Top-down/bottom-up cellular shades — privacy from below, daylight from above.",
        "keywords": "cellular shades, honeycomb shades, Hunter Douglas Duette, Sonnette, Norman Honeycomb, blackout cellular, top-down bottom-up, energy-efficient blinds",
        "og_desc": "Single, double, and triple-cell honeycomb shades — and where each one belongs in a Tennessee home.",
        "tw_desc": "Cell counts, blackout liners, and the rooms where honeycomb shades earn their place.",
        "breadcrumb_name": "Cellular & Honeycomb Shades Guide",
        "body": """
      <p>Cellular shades — also called honeycomb shades — are the most-recommended single product in our showroom. They insulate, they sound-dampen, they have the broadest fabric range of any shade type, and they happen to be one of the most affordable premium treatments on the market. Here is the complete guide to what they are, the variants you can spec, and the rooms where they out-perform every other option.</p>

      <h2>How honeycomb shades work</h2>
      <p>The fabric is folded into hexagonal cells that trap a column of air across the face of the window. That air is the insulator. The principle is the same as a thermos: still air between two surfaces is the most efficient thermal break you can build out of a soft material. The more cells, the more insulation.</p>

      <h2>Single, double, and triple cell</h2>
      <ul>
        <li><strong>Single cell.</strong> One row of cells. Slimmest stack when raised, lightest fabric. The right choice for small windows, narrow casings, and anywhere energy is a secondary concern.</li>
        <li><strong>Double cell.</strong> Two rows of cells stacked front-to-back. The mainstream choice — most cellular shades we install are double-cell. Better insulation, slightly thicker stack.</li>
        <li><strong>Triple cell (Architella).</strong> Hunter Douglas's premium construction — three cells in a complex geometry. The most insulating soft shade made. We spec it for Tennessee primary bedrooms, sunrooms, and any window with bad solar gain.</li>
      </ul>

      <h2>Fabric types</h2>
      <ul>
        <li><strong>Light-filtering.</strong> Allows soft, diffused daylight. Good for living rooms, dining rooms, kitchens.</li>
        <li><strong>Room-darkening.</strong> Cuts most light without going fully black. Right for guest bedrooms and family rooms.</li>
        <li><strong>Blackout.</strong> Opaque fabric paired with side-channel light blockers — reaches true darkness. The bedroom answer. <a href="/blog/best-blinds-for-bedrooms/">More on bedroom blackout here.</a></li>
        <li><strong>Sheer cellular.</strong> A newer category — semi-transparent cellular fabric for picture windows that need glare control without view loss.</li>
      </ul>

      <p class="pull">A cellular shade is the rare treatment that performs better than it photographs.</p>

      <h2>Top-down / bottom-up</h2>
      <p>The single best upgrade on a cellular shade. Two cords (or two motor controls) let you lower the top of the shade independently from raising the bottom — so you can have privacy from the sidewalk and full daylight from the sky at the same time. Adds about 15% to the cost. Worth it on any bedroom or street-facing window.</p>

      <h2>Cordless and motorized</h2>
      <p>Every cellular shade we sell is cordless or motorized — corded shades have been a child-safety nonstarter since 2018. Cordless is the default. Motorization adds $80–$150 per window and integrates with Alexa, Google Home, and Apple HomeKit through Hunter Douglas PowerView or Somfy. <a href="/blog/motorized-smart-shades-guide/">More on motorization here.</a></p>

      <h2>The lines we install most</h2>
      <ul>
        <li><strong>Hunter Douglas Duette.</strong> The category benchmark. Available in single, double, and triple-cell Architella. PowerView motorization, LightLock blackout side-channels, top-down/bottom-up — every feature in the category.</li>
        <li><strong>Hunter Douglas Sonnette.</strong> A rolled cellular with a unique rounded profile — soft, modern, no horizontal pleat lines. Sits between a roller and a cellular visually.</li>
        <li><strong>Norman Honeycomb.</strong> Excellent fit and finish at a more accessible price point. Cordless, motorized, and blackout all available.</li>
        <li><strong>Graber CrystalPleat.</strong> The value option. Single and double cell, cordless, room-darkening.</li>
      </ul>

      <div class="callout">
        <h3>Our default 2026 cellular spec</h3>
        <p><strong>Hunter Douglas Duette Architella triple-cell, top-down/bottom-up, blackout fabric with LightLock side channels, cordless lift</strong> — or PowerView motorized for primary bedrooms. The single most-installed configuration in our showroom for the past three years.</p>
      </div>

      <h2>Where cellular shades win</h2>
      <ul>
        <li><strong>Primary bedrooms.</strong> Best-in-category blackout when properly mounted.</li>
        <li><strong>Children's bedrooms and nurseries.</strong> Cordless, soft, quiet, and naturally child-safe.</li>
        <li><strong>Bedrooms over kitchens or living rooms.</strong> The sound dampening is real.</li>
        <li><strong>Sunrooms.</strong> Triple-cell Architella cuts solar gain dramatically.</li>
        <li><strong>Energy-conscious homes.</strong> Most insulating soft shade on the market.</li>
        <li><strong>Skylights.</strong> Specialty cellular skylight shades are the only honest answer to direct overhead sun.</li>
      </ul>

      <h2>Cost</h2>
      <p>Typical installed pricing in Tennessee (2026):</p>
      <ul>
        <li>Single cell, cordless: <strong>$80–$200/window</strong></li>
        <li>Double cell, cordless: <strong>$140–$280/window</strong></li>
        <li>Triple cell (Architella), cordless: <strong>$220–$420/window</strong></li>
        <li>Add for blackout liner: <strong>$30–$60/window</strong></li>
        <li>Add for top-down/bottom-up: <strong>~15%</strong></li>
        <li>Add for motorization: <strong>$80–$200/window + hub</strong></li>
      </ul>

      <p>For a sample-in-hand quote across Gallatin, Nashville, Hendersonville, Franklin, Brentwood, Murfreesboro and the 90-mile radius, call or text <a href="tel:+16292988241">629-298-8241</a> or <a href="/#contact">book a free in-home consultation</a>.</p>
        """,
        "related": [
            ("/blog/best-blinds-for-bedrooms/", "Buyer's guide · 7 min read", "The best blinds for <em>bedrooms</em>", "Where cellular wins, room by room.", "/assets/images/cellular-shades-bedroom.webp", "Cellular shades in a Tennessee bedroom"),
            ("/blog/motorized-smart-shades-guide/", "Product guide · 7 min read", "Motorized &amp; <em>smart shades</em>", "Add PowerView or Somfy to any cellular.", "/assets/images/blog/motorized-shades.webp", "Motorized shades in a Tennessee great room"),
        ],
    },
    {
        "slug": "outdoor-shades-awnings-guide",
        "title_html": "Outdoor shades &amp; <em>awnings.</em>",
        "h1_plain": "Outdoor Shades & Awnings: A Complete Guide",
        "meta_title": "Outdoor Shades & Awnings: A Complete Guide · Stately Shades",
        "meta_desc": "Wind-rated exterior shades, retractable screens, retractable awnings, motorized patio enclosures. Sol-Lux, Phantom Screens, Somfy. A complete guide for Tennessee porches, pergolas, and outdoor rooms.",
        "eyebrow": "Product Guide · Outdoor Living",
        "section": "Product Guide",
        "minutes": "7",
        "image": "/assets/images/blog/outdoor-shades.webp",
        "image_alt": "Motorized retractable outdoor sun shades lowered three-quarters on a Tennessee covered porch at dusk",
        "caption": "Motorized exterior shades — block 80–95% of heat without losing the view.",
        "keywords": "outdoor shades, exterior shades, retractable screens, retractable awnings, motorized patio shades, Sol-Lux, Phantom Screens, porch enclosures, Tennessee outdoor living",
        "og_desc": "Retractable screens, exterior sun shades, motorized awnings — what they do and where they belong.",
        "tw_desc": "Block 80–95% of summer heat, keep the bugs out, keep the view.",
        "breadcrumb_name": "Outdoor Shades & Awnings Guide",
        "body": """
      <p>Tennessee summers are the reason outdoor shades exist. A covered porch can be 15–20 degrees hotter than the house at four o'clock in July, and a screened pergola without sun control is unusable from June through September. Outdoor shades, retractable screens, and motorized awnings turn that lost half of the house into the part you actually use. Here is the full catalogue and where each piece belongs.</p>

      <h2>The four outdoor categories</h2>

      <h3>1. Exterior solar / sun shades</h3>
      <p>Wind-rated, weatherproof fabric shades that mount on the outside of a porch, pergola, or window. They block 80–95% of solar heat <em>before</em> it reaches the wall — far more efficient than any interior shade can manage. Most popular openness: 3% (cuts almost all glare, preserves view) and 5% (slightly more daylight, slightly less view).</p>
      <p>Best for: covered porches, screened-in patios, west-facing walls of the house, pool houses, sunrooms.</p>

      <h3>2. Retractable screens (motorized)</h3>
      <p>Insect screens that disappear into a head cassette when not in use. Available for porches, pergolas, garage doors, and large picture windows. Phantom Screens and Sol-Lux are the lines we install most. When extended, they keep mosquitos and gnats out without blocking the breeze; when retracted, they're invisible.</p>
      <p>Best for: any porch in Tennessee, period. Mosquito season is real.</p>

      <h3>3. Retractable awnings</h3>
      <p>Lateral-arm or pergola-mounted fabric awnings that extend outward to shade a patio. Available in fixed cassette or retractable. Most modern installs are motorized with sun and wind sensors — the awning auto-retracts when wind crosses a threshold.</p>
      <p>Best for: brick or stucco walls over a patio, restaurants and outdoor dining areas, west-facing patios.</p>

      <h3>4. Motorized patio enclosures</h3>
      <p>Full vinyl-side curtain systems that turn a screened porch into a three-season room. Roll-down vinyl panels seal out wind and rain; motorized operation means one tap closes the entire porch. Sol-Lux Eclipse is the line we install most.</p>
      <p>Best for: outdoor kitchens, hot tubs on the porch, families who want to use the porch in November.</p>

      <h2>Materials and finishes</h2>
      <ul>
        <li><strong>Sunbrella® fabric</strong> — UV-stable, mildew-resistant, 5-year colorfastness warranty. The premium standard.</li>
        <li><strong>Phifer SheerWeave</strong> — the workhorse mesh for solar/insect screens. 10+ years of service life.</li>
        <li><strong>Aluminum frames</strong> — powder-coated in matte black, bronze, or matched-to-house. No rust.</li>
        <li><strong>Stainless hardware</strong> — every fastener, every track. Critical in humid southern climates.</li>
      </ul>

      <h2>Motorization is the default</h2>
      <p>Almost everything we install outdoors is motorized — manual cranks fail on weather exposure faster than the fabric. Somfy is the motor of choice. Sun sensors, wind sensors, and timed scenes (drop the west shades at 3 p.m.) make these systems set-and-forget.</p>

      <p class="pull">A southern Tennessee porch with no shade is half a porch. A southern porch with motorized exterior shades and a retractable screen is twice the house.</p>

      <h2>The lines we install most</h2>
      <ul>
        <li><strong>Sol-Lux</strong> — boutique exterior systems with the best fabric range and motor reliability in the category. Our default premium spec.</li>
        <li><strong>Phantom Screens</strong> — the gold standard for retractable insect screens. 10+ year track record.</li>
        <li><strong>Hunter Douglas Designer Screen</strong> — exterior solar shades on the Hunter Douglas PowerView system. Best when the rest of the house is already PowerView.</li>
        <li><strong>SunSetter</strong> — value-tier retractable awnings.</li>
      </ul>

      <div class="callout">
        <h3>Our default 2026 outdoor spec</h3>
        <p>For a typical 14×30 ft. covered porch in Tennessee: <strong>Sol-Lux exterior solar shades (5% openness) on the south and west elevations, Phantom retractable screens on the front and east, all Somfy-motorized with sun and wind sensors.</strong> Adds about $6,000–$11,000 installed; turns the porch into a year-round room.</p>
      </div>

      <h2>Wind ratings — the spec that matters</h2>
      <p>Tennessee gets thunderstorms with 40–60 mph gusts. An outdoor shade not rated for wind will tear. The lines we install are rated to a minimum of 40 mph (Beaufort scale 8). Premium Sol-Lux systems with side tracks are rated to 60+ mph. Always ask for the wind rating — it's the single most-skipped spec on cheap outdoor installs.</p>

      <h2>Where outdoor systems belong</h2>
      <ul>
        <li><strong>Covered porches.</strong> The natural home of every outdoor shade type.</li>
        <li><strong>Pergolas.</strong> Either over-pergola (top) for shade, or pergola-side (vertical) for wind/insect.</li>
        <li><strong>Pool houses and pool cabanas.</strong> Insect screens are non-negotiable.</li>
        <li><strong>Garage doors.</strong> Retractable garage-door screens turn the garage into an open workshop.</li>
        <li><strong>West-facing kitchen and great-room walls.</strong> An exterior shade outside the window beats any interior treatment for energy efficiency.</li>
        <li><strong>Sunrooms.</strong> Exterior shades on the outside, paired with interior cellular for night insulation.</li>
      </ul>

      <h2>Cost</h2>
      <ul>
        <li>Exterior solar shades, motorized: <strong>$1,800–$4,200 per opening</strong></li>
        <li>Retractable insect screens (Phantom): <strong>$1,200–$2,800 per opening</strong></li>
        <li>Retractable awnings, motorized: <strong>$3,500–$8,500 installed</strong></li>
        <li>Motorized vinyl patio enclosures: <strong>$8,000–$22,000 per porch</strong></li>
      </ul>

      <p>For an in-home consultation — porch walked, sun studied, fabric sampled in your own light — call or text <a href="tel:+16292988241">629-298-8241</a> or <a href="/#contact">book a free visit</a>. We cover Gallatin, Nashville, Hendersonville, Franklin, Brentwood, Murfreesboro and the 90-mile radius around our showroom.</p>
        """,
        "related": [
            ("/blog/motorized-smart-shades-guide/", "Product guide · 7 min read", "Motorized &amp; <em>smart shades</em>", "All Somfy-based outdoor systems are motorized.", "/assets/images/blog/motorized-shades.webp", "Motorized shades in a Tennessee great room"),
            ("/blog/zebra-banded-solar-shades-guide/", "Product guide · 6 min read", "Zebra, banded &amp; <em>solar shades</em>", "Solar control begins at the interior, too.", "/assets/images/blog/zebra-solar.webp", "Zebra banded shades in a Tennessee dining nook"),
        ],
    },
    {
        "slug": "sheer-privacy-vanes-guide",
        "title_html": "Sheer &amp; <em>privacy vanes.</em>",
        "h1_plain": "Sheer & Privacy Vanes: Silhouette, Pirouette & Luminette",
        "meta_title": "Sheer & Privacy Vanes: Silhouette, Pirouette & Luminette · Stately Shades",
        "meta_desc": "Hunter Douglas Silhouette, Pirouette, and Luminette — fabric vanes between sheer panels for picture windows, French doors, and sliding glass doors. A complete guide from a Tennessee dealer.",
        "eyebrow": "Product Guide · Fabric Sheers",
        "section": "Product Guide",
        "minutes": "6",
        "image": "/assets/images/blog/sheer-vanes.webp",
        "image_alt": "Hunter Douglas Silhouette sheer fabric shades with floating horizontal vanes in a refined Tennessee living room",
        "caption": "Silhouette-style fabric vanes — diffuse, tilt, and lift in one motion.",
        "keywords": "Hunter Douglas Silhouette, Pirouette, Luminette, sheer shades, fabric vanes, privacy sheers, picture window shades, French door shades, sliding glass door treatments",
        "og_desc": "Silhouette, Pirouette, and Luminette — Hunter Douglas's three sheer fabric vane lines, explained.",
        "tw_desc": "Soft fabric vanes that diffuse and tilt — for picture windows and sliders alike.",
        "breadcrumb_name": "Sheer & Privacy Vanes Guide",
        "body": """
      <p>Sheer privacy vanes are the most visually distinctive treatments Hunter Douglas makes. Three product lines — Silhouette, Pirouette, and Luminette — share the same idea: a soft fabric vane suspended between or alongside translucent sheer panels. The vanes tilt to control light; the sheers diffuse it. The result is something no other category does: privacy <em>and</em> daylight at the same time, with no slat-and-louver hardness anywhere in the picture.</p>

      <h2>How sheer fabric vanes work</h2>
      <p>Instead of horizontal slats (like a blind) or solid fabric (like a roller), the vanes are made of soft, brushed fabric — woven or knitted — and float between two layers of translucent sheer. Tilting the vanes is mechanical, but the effect is visual: closed, you have a soft fabric face; open, you have a window full of light passing through filaments of fabric.</p>

      <h2>Silhouette — the original</h2>
      <p>Hunter Douglas <strong>Silhouette</strong> is the line that defined the category. Horizontal fabric vanes between two sheer panels, lifted on a roller-style headrail. Vanes available in 2″, 3″, and 4″ — the wider the vane, the more contemporary the look. Light filtering, room-darkening, and a partial-blackout fabric are all offered.</p>
      <p>Best for: picture windows, formal living rooms, dining rooms, and any window where you want softness, diffusion, and the option to fully open the view (the vanes can collapse into the headrail when raised).</p>

      <h2>Pirouette — the contoured cousin</h2>
      <p>Hunter Douglas <strong>Pirouette</strong> is the more architectural sibling. Instead of flat vanes between two sheers, Pirouette uses a single layer of sheer with horizontal fabric vanes attached. When the vanes are closed, the front face is solid fabric; when tilted open, the fabric vanes rotate outward and the sheer behind shows through. Slightly thicker stack than Silhouette, more dimensional shadow play.</p>
      <p>Best for: modern interiors, picture windows facing an inner courtyard, dining rooms where you want a more graphic vane line.</p>

      <h2>Luminette — for sliding doors and French doors</h2>
      <p>Hunter Douglas <strong>Luminette</strong> is the vertical version. Instead of horizontal vanes, you have vertical fabric vanes (about 4–6″ wide) hanging between two large sheer panels that span the full width of the opening. The vanes rotate together — closed for privacy, open for view, anywhere in between for diffused light. The whole assembly traverses left or right on a track for full access to the door.</p>
      <p>Best for: <strong>sliding glass doors, French doors, atrium walls, and very wide picture windows.</strong> The only product in the Hunter Douglas catalogue that solves a 12-foot-wide sliding glass door elegantly.</p>

      <div class="callout">
        <h3>Quick spec pick</h3>
        <p><strong>Tall picture window?</strong> Silhouette. <br/><strong>Modern interior with high contrast?</strong> Pirouette. <br/><strong>Sliding glass door or French doors?</strong> Luminette. <br/>These three answer roughly 95% of what the category covers.</p>
      </div>

      <h2>Fabric options</h2>
      <ul>
        <li><strong>Light-filtering vanes</strong> — the default. Diffused, glowing.</li>
        <li><strong>Room-darkening vanes</strong> — significantly less light transmission. Right for media rooms and offices.</li>
        <li><strong>Blackout-lined vanes</strong> (Silhouette only) — for bedrooms that want the fabric look but need real darkness. Less common; we usually pair Silhouette with a separate blackout roller behind for full darkness.</li>
      </ul>

      <h2>Motorization</h2>
      <p>All three lines run on PowerView Gen 3. Silhouette and Pirouette tilt by motor; Luminette traverses (slides left/right) and rotates by motor — two independent commands. Excellent integration with Alexa, Google Home, and Apple HomeKit. The Luminette traverse-motor in particular is a near-perfect product: silent, fast, and removes the only awkward part of operating a 10-foot sheer panel manually.</p>

      <h2>What to know before you order</h2>
      <ul>
        <li><strong>Vanes don't hang plumb in a draft.</strong> A breeze from an HVAC register makes Silhouette vanes wiggle. Plan the register direction.</li>
        <li><strong>The cassette is large.</strong> Silhouette and Pirouette headrails are roughly 3.5″ tall — make sure your casing can accept that.</li>
        <li><strong>Luminette stack is wide.</strong> A 10-foot Luminette stacks roughly 18–24″ when fully open. Plan the wall space.</li>
        <li><strong>Premium pricing.</strong> Sheer fabric vanes are at the top of the catalogue cost-wise. Worth it for the rooms that earn them.</li>
      </ul>

      <h2>Cost</h2>
      <ul>
        <li>Silhouette, cordless, light-filtering: <strong>$420–$880 per window installed</strong></li>
        <li>Silhouette, PowerView motorized: <strong>$680–$1,250 per window installed</strong></li>
        <li>Pirouette, cordless: <strong>$480–$960 per window installed</strong></li>
        <li>Luminette, manual traverse: <strong>$900–$2,400 per door</strong></li>
        <li>Luminette, PowerView traverse + tilt: <strong>$1,400–$3,200 per door</strong></li>
      </ul>

      <h2>Where sheer vanes belong</h2>
      <p>Living rooms with picture windows. Primary bedrooms (paired with a blackout roller behind). Dining rooms with formal lighting. Sliding glass doors that lead to a back patio. French doors flanking a fireplace. Any room where you want softness and the option to dissolve the boundary between inside and outside with the touch of a remote.</p>

      <p>For an in-home consultation with full fabric samples — Silhouette, Pirouette, Luminette, all in your light — call or text <a href="tel:+16292988241">629-298-8241</a> or <a href="/#contact">book a free visit</a>.</p>
        """,
        "related": [
            ("/blog/motorized-smart-shades-guide/", "Product guide · 7 min read", "Motorized &amp; <em>smart shades</em>", "PowerView drives every sheer vane product.", "/assets/images/blog/motorized-shades.webp", "Motorized shades in a Tennessee great room"),
            ("/blog/plantation-shutters-vs-roller-shades/", "Comparison · 6 min read", "Plantation shutters vs. <em>roller shades</em>", "Where sheers fit between the two.", "/assets/images/sheer-fabric-shades.webp", "Sheer fabric shades behind a Tennessee window seat"),
        ],
    },
    {
        "slug": "zebra-banded-solar-shades-guide",
        "title_html": "Zebra, banded &amp; <em>solar shades.</em>",
        "h1_plain": "Zebra, Banded & Solar Shades: A Complete Guide",
        "meta_title": "Zebra, Banded & Solar Shades: A Complete Guide · Stately Shades",
        "meta_desc": "Dual-layer zebra and banded shades that toggle sheer-to-opaque, plus solar UV-filtering roller shades for sunrooms, offices, and west-facing windows. A complete 2026 guide from a Gallatin, TN dealer.",
        "eyebrow": "Product Guide · Modern Specialty",
        "section": "Product Guide",
        "minutes": "6",
        "image": "/assets/images/blog/zebra-solar.webp",
        "image_alt": "Dual-layer zebra banded shades on tall windows in a modern Tennessee dining nook",
        "caption": "Zebra banded shades — slide the bands to switch from view to privacy.",
        "keywords": "zebra shades, banded shades, solar shades, UV-filtering shades, dual-layer shades, view-thru blinds, sun shades, openness factor, screen shades",
        "og_desc": "Dual-layer zebra/banded shades and UV-filtering solar shades — modern light control without losing the view.",
        "tw_desc": "Zebra bands toggle sheer-to-opaque. Solar shades cut UV without going dark. Both, explained.",
        "breadcrumb_name": "Zebra, Banded & Solar Shades Guide",
        "body": """
      <p>Zebra, banded, and solar shades are the most-misunderstood category in the showroom — partly because the names overlap (zebra is sometimes called banded; solar sometimes called sun or screen), and partly because they solve very different problems. This is the complete guide to what each one does, where it belongs, and which rooms benefit most.</p>

      <h2>Zebra and banded shades</h2>
      <p>Zebra shades (also called <em>banded</em> or <em>vision</em> shades) are a dual-layer fabric that alternates between sheer and opaque horizontal bands. Both layers roll on the same tube. Sliding one layer relative to the other aligns the bands either to <strong>see-through mode</strong> (sheer bands overlap, you see out) or <strong>privacy mode</strong> (opaque bands overlap, you don't).</p>
      <p>Lift the shade fully and the entire window is exposed; lower fully and you toggle between view and privacy with the same cord (or motor). One product, two modes.</p>

      <h3>Where zebra/banded shines</h3>
      <ul>
        <li><strong>Modern living rooms</strong> — the graphic horizontal band reads contemporary.</li>
        <li><strong>Home offices facing a street</strong> — privacy when on camera, view when working.</li>
        <li><strong>Kitchens and breakfast nooks</strong> — diffused light when cooking, view when eating.</li>
        <li><strong>Tall narrow windows</strong> — the band geometry reads more elegant than a flat roller.</li>
      </ul>

      <h3>Where it doesn't</h3>
      <ul>
        <li><strong>Bedrooms needing blackout</strong> — the bands always leak light at the seams.</li>
        <li><strong>Very wide windows</strong> — the band alignment can creep at scale; we typically split into two shades.</li>
        <li><strong>Traditional architecture</strong> — too graphic for most heritage interiors.</li>
      </ul>

      <h2>Solar shades</h2>
      <p>Solar shades — also called <strong>screen shades</strong> or <strong>sun shades</strong> — are single-layer roller shades made of a specially-engineered woven mesh. The mesh blocks UV and a percentage of visible light (the <em>openness factor</em>) while preserving the view. They are not for privacy; they are for glare and heat control.</p>

      <h3>Openness factors</h3>
      <ul>
        <li><strong>1% openness.</strong> Cuts ~99% of UV and most glare. Best for very bright west-facing windows. View is dimmed but still legible.</li>
        <li><strong>3% openness.</strong> The most popular. Best balance of view, glare control, and heat rejection. Our default solar spec.</li>
        <li><strong>5% openness.</strong> More daylight, more view, modest glare reduction. Right for north-facing rooms or places where view is the priority.</li>
        <li><strong>10% openness.</strong> Sheer-side of the category — minimal heat rejection, maximum view.</li>
      </ul>

      <h3>Where solar wins</h3>
      <ul>
        <li><strong>Home offices.</strong> Cuts screen glare without darkening the room.</li>
        <li><strong>West-facing great rooms and kitchens.</strong> Block heat without losing the lake/yard/skyline view.</li>
        <li><strong>Sunrooms.</strong> Pairs perfectly with cellular shades for night insulation.</li>
        <li><strong>Walls of glass.</strong> Multiple synchronized motorized solar shades on PowerView or Somfy.</li>
        <li><strong>Anywhere you'd put drapery for layering.</strong> Solar shades behind drapery is one of the most-photographed combinations in modern editorial interiors.</li>
      </ul>

      <p class="pull">A solar shade is the only treatment that cuts heat while leaving the view fully intact. That's its entire job.</p>

      <h2>Light filtering vs. solar — the confusing pair</h2>
      <p>Light-filtering fabric (used in standard rollers, cellulars, Romans) is opaque and diffuses light. Solar mesh is woven, allows direct view-through, and grades by openness percentage. Different fabrics, different uses. We see homeowners confuse the two constantly — when shopping online, look for an "openness" number on the spec sheet; if it has one, it's solar.</p>

      <h2>Motorization</h2>
      <p>Both zebra and solar shades are excellent motorization candidates. Solar shades with sun sensors are some of the most-loved smart-home installs we do — they drop automatically at noon in summer and raise at 6 p.m., entirely without input.</p>

      <h2>The lines we install most</h2>
      <ul>
        <li><strong>Hunter Douglas Designer Banded</strong> — premium zebra construction, PowerView motorization.</li>
        <li><strong>Norman PerformanceRoller (zebra)</strong> — excellent value, cordless or motorized.</li>
        <li><strong>Hunter Douglas Designer Screen (solar)</strong> — the benchmark solar shade.</li>
        <li><strong>Phifer SheerWeave / Graber Solar</strong> — broad fabric range, every openness factor.</li>
      </ul>

      <h2>Cost</h2>
      <ul>
        <li>Zebra/banded shades, cordless: <strong>$120–$340 per window installed</strong></li>
        <li>Zebra, motorized: <strong>$280–$540 per window installed</strong></li>
        <li>Solar shades (3% openness), cordless: <strong>$140–$320 per window installed</strong></li>
        <li>Solar shades, motorized with sensor: <strong>$320–$640 per window installed</strong></li>
      </ul>

      <p>For a sample-in-hand quote — fabric swatches in your own light, openness factors compared side by side — call or text <a href="tel:+16292988241">629-298-8241</a> or <a href="/#contact">book a free consultation</a>.</p>
        """,
        "related": [
            ("/blog/motorized-smart-shades-guide/", "Product guide · 7 min read", "Motorized &amp; <em>smart shades</em>", "Sun-sensor automation is the killer feature for solar.", "/assets/images/blog/motorized-shades.webp", "Motorized shades in a Tennessee great room"),
            ("/blog/outdoor-shades-awnings-guide/", "Product guide · 7 min read", "Outdoor shades &amp; <em>awnings</em>", "Solar control begins on the exterior.", "/assets/images/blog/outdoor-shades.webp", "Outdoor shades on a Tennessee porch at dusk"),
        ],
    },
    {
        "slug": "woven-wood-bamboo-shades-guide",
        "title_html": "Woven wood &amp; <em>bamboo shades.</em>",
        "h1_plain": "Woven Wood & Bamboo Shades: A Complete Guide",
        "meta_title": "Woven Wood & Bamboo Shades: A Complete Guide · Stately Shades",
        "meta_desc": "Hunter Douglas Provenance, Graber woven wood. Hand-loomed bamboo, grass, jute, and reed shades for warm, organic Tennessee interiors. Light-filtering or paired with blackout liner.",
        "eyebrow": "Product Guide · Naturals",
        "section": "Product Guide",
        "minutes": "6",
        "image": "/assets/images/blog/woven-wood.webp",
        "image_alt": "Hand-loomed woven wood bamboo shade on a tall arched window in a refined Tennessee sitting room",
        "caption": "Hand-loomed bamboo and grass — the warmest natural material in the catalogue.",
        "keywords": "woven wood shades, bamboo shades, Provenance, Graber, jute shades, grass shades, natural shades, organic window treatments",
        "og_desc": "Hand-loomed bamboo, grass, jute, and reed — Hunter Douglas Provenance and the broader naturals catalogue.",
        "tw_desc": "Hand-loomed bamboo and grass shades for Tennessee homes with warm, organic interiors.",
        "breadcrumb_name": "Woven Wood & Bamboo Shades Guide",
        "body": """
      <p>Woven wood shades are the one product in our catalogue that nobody buys for performance. They are bought for material. Hand-loomed bamboo, grass, jute, and reed do nothing a roller or cellular shade doesn't do better in any single metric — but they do something neither can: they bring a living, natural texture into a room with light passing through it. For warm, organic interiors that lean coastal, traditional Southern, or refined-rustic, there is no equivalent.</p>

      <h2>What woven wood actually is</h2>
      <p>The material is woven on hand- or power-looms from natural fibers — bamboo poles, grass strands, jute reeds, and similar materials — laced together with cotton thread. Each shade is unique; no two looms produce identical pieces. Hunter Douglas <strong>Provenance</strong> is the premium line and the one we sell most; Graber and a handful of boutique workrooms cover the broader market.</p>

      <h2>Materials and where each one belongs</h2>
      <h3>Bamboo</h3>
      <p>The most popular natural. Honey to deep walnut tones, depending on the species (carbonized bamboo is darker). Tight weave reads more refined; loose weave reads more rustic.</p>

      <h3>Grass</h3>
      <p>Softer texture than bamboo, lighter tones, often almost golden. Lets through more diffused light. Beautiful in dining rooms and sunrooms.</p>

      <h3>Jute</h3>
      <p>The most rustic of the four. Knotted, irregular, very organic. Right for coastal and farmhouse interiors. Pairs with rough-hewn beam ceilings.</p>

      <h3>Reed</h3>
      <p>Slim, straight, modern. The most architectural natural. Common in transitional and modern interiors.</p>

      <h2>Light behavior</h2>
      <p>Without a liner, woven woods are <strong>light-filtering</strong> — they soften and warm direct sun into a glow with horizontal shadow lines from the weave. This is the most beautiful single feature of the category. Sunset through a woven wood is the reason people install them.</p>
      <p>With a liner, you can add:</p>
      <ul>
        <li><strong>Privacy liner</strong> — neutral fabric on the back, blocks the silhouette while preserving the natural look from inside.</li>
        <li><strong>Room-darkening liner</strong> — substantial light reduction, right for guest bedrooms.</li>
        <li><strong>Blackout liner</strong> — full darkness, right for primary bedrooms. Pairs the warm natural face with full blackout function.</li>
      </ul>

      <h2>Roll styles</h2>
      <ul>
        <li><strong>Roman fold</strong> — fabric gathers into horizontal pleats when raised. The classic look.</li>
        <li><strong>Waterfall</strong> — fabric stacks neatly behind itself, no gather at the bottom. Cleaner, more modern.</li>
        <li><strong>Front-slat</strong> — bottom rail visible, stack folds behind. Less common, more architectural.</li>
      </ul>

      <h2>Where woven woods belong</h2>
      <ul>
        <li><strong>Sitting rooms and living rooms</strong> with warm wood floors and brass or leather accents.</li>
        <li><strong>Dining rooms</strong> — the texture pairs beautifully with linen drapery.</li>
        <li><strong>Bedrooms</strong> (with blackout liner) — the warmest blackout treatment in the catalogue.</li>
        <li><strong>Sunrooms and screened porches with interior glass.</strong></li>
        <li><strong>Arched windows</strong> — woven woods on arched windows are spectacular when templated correctly.</li>
        <li><strong>Children's rooms</strong> — naturally cordless, soft, calming.</li>
      </ul>

      <h2>Where they don't</h2>
      <ul>
        <li><strong>Very humid rooms</strong> (bathrooms, laundry). Natural fiber + moisture = trouble.</li>
        <li><strong>Hard-modern interiors</strong> with high-contrast finishes — woven woods often clash.</li>
        <li><strong>Direct ocean/lake spray</strong> — even with marine treatment, natural fibers don't love salt.</li>
      </ul>

      <p class="pull">A woven wood is the rare shade that you'd want to look at even with no window behind it.</p>

      <h2>The lines we install most</h2>
      <ul>
        <li><strong>Hunter Douglas Provenance.</strong> The premium standard — exceptional weaves, top-down/bottom-up rigs, PowerView motorization, the broadest fabric library in the category.</li>
        <li><strong>Graber Naturals.</strong> Excellent value, broad material range, cordless or motorized.</li>
        <li><strong>Pacific Woven (boutique).</strong> Hand-loomed in California, for clients who want a known-provenance natural.</li>
      </ul>

      <h2>Motorization</h2>
      <p>Hunter Douglas Provenance runs on PowerView Gen 3. The motor handles the weight of natural materials beautifully — woven woods are heavier than cellular fabrics, and the Provenance motor is sized accordingly. We motorize about half of the woven wood projects we quote, because most of these shades end up on tall windows in great rooms or stairwells where reach matters.</p>

      <h2>Cost</h2>
      <ul>
        <li>Standard woven wood, cordless, light-filtering: <strong>$220–$520 per window installed</strong></li>
        <li>Premium Provenance, cordless: <strong>$340–$780 per window installed</strong></li>
        <li>With blackout liner: <strong>add $80–$160 per window</strong></li>
        <li>Top-down/bottom-up: <strong>add ~15%</strong></li>
        <li>Motorization (Provenance PowerView): <strong>add $180–$360 per window</strong></li>
      </ul>

      <p>For an in-home consultation with full bamboo, grass, jute, and reed samples — held to your window in your own light — call or text <a href="tel:+16292988241">629-298-8241</a> or <a href="/#contact">book a free visit</a>.</p>
        """,
        "related": [
            ("/blog/plantation-wood-shutters-guide/", "Product guide · 8 min read", "Plantation &amp; <em>wood shutters</em>", "The harder cousin to a soft natural.", "/assets/images/blog/plantation-shutters.webp", "Plantation shutters in a Tennessee dining room"),
            ("/blog/cellular-honeycomb-shades-guide/", "Product guide · 7 min read", "Cellular &amp; <em>honeycomb shades</em>", "The performance counterpart for bedrooms.", "/assets/images/blog/cellular-shades.webp", "Cellular shades in a Tennessee bedroom"),
        ],
    },
    {
        "slug": "wood-blinds-drapery-guide",
        "title_html": "Wood blinds &amp; <em>custom drapery.</em>",
        "h1_plain": "Wood Blinds & Custom Drapery: A Complete Guide",
        "meta_title": "Wood Blinds & Custom Drapery: A Complete Guide · Stately Shades",
        "meta_desc": "Wood blinds, faux wood blinds, custom drapery, Roman shades, valances, cornices, motorized rods. The full soft-treatments catalogue from a Gallatin, TN dealer.",
        "eyebrow": "Product Guide · The Catalogue",
        "section": "Product Guide",
        "minutes": "7",
        "image": "/assets/images/blog/wood-blinds-drapery.webp",
        "image_alt": "Custom hardwood blinds and floor-to-ceiling cream linen drapery in a luxury Tennessee bedroom",
        "caption": "Wood blinds on the side windows, ceiling-mounted drapery on the center window.",
        "keywords": "wood blinds, faux wood blinds, custom drapery, Roman shades, Vignette, motorized drapery, valances, cornices, soft treatments, child-safe blinds",
        "og_desc": "Wood blinds, faux wood, custom drapery, Romans, cornices, motorized rods — the full soft-treatments catalogue.",
        "tw_desc": "Every soft treatment that isn't a shutter, cellular, or sheer vane — explained.",
        "breadcrumb_name": "Wood Blinds & Drapery Guide",
        "body": """
      <p>Everything that isn't a shutter, a cellular, a sheer vane, a zebra, a solar, or a woven wood ends up in this guide — which is to say, the largest single category in the catalogue. Wood blinds, faux wood, custom drapery, Roman shades, valances, cornices, motorized rods. This is the complete tour, organized by what they do.</p>

      <h2>Real wood blinds</h2>
      <p>Horizontal hardwood slats — basswood, oak, or alder — strung on a lift cord. Slats tilt to control light. Slat sizes: 1″, 2″, and 2.5″ (most common). Real wood blinds carry warmth and grain that no faux can match, and they take stain beautifully — when you want blinds to match a wood floor or stained trim, real wood is the only honest answer.</p>
      <p>Best for: studies, living rooms, primary bedrooms with stained trim, dining rooms.</p>

      <h2>Faux wood blinds</h2>
      <p>The composite cousin — molded polymer or PVC slats that look like wood from across the room. About half the cost of real wood, fully waterproof, no warp. The right choice for any wet or humid room.</p>
      <p>Best for: bathrooms, kitchens, laundry, mudrooms, garages, anywhere a real wood blind would have a short life.</p>

      <h3>Cordless and child-safe</h3>
      <p>Every wood and faux-wood blind we sell is cordless. The corded lift mechanism was effectively retired from the residential category in 2018 for child-safety reasons, and we won't sell a corded blind even on request. Lift is by hand on the bottom rail or, on premium lines, by motor.</p>

      <h2>Vertical blinds and panel tracks</h2>
      <p>For sliding glass doors and very wide picture windows. Vertical blinds (vinyl, fabric, or faux wood vanes hung from an overhead track) are the budget answer; <strong>panel-track systems</strong> are the modern luxury answer — large flat fabric panels that traverse on a track like a sliding wall.</p>
      <p>Both bypass each other into a tight stack on one side, opening the full opening for use.</p>

      <h2>Roman shades</h2>
      <p>Soft fabric panels that fold into horizontal pleats when raised. Available in three styles:</p>
      <ul>
        <li><strong>Flat Romans.</strong> Crisp horizontal seams. Modern, architectural.</li>
        <li><strong>Hobbled Romans.</strong> Soft fabric horseshoe-shaped folds even when fully lowered. Traditional, dressier.</li>
        <li><strong>Relaxed Romans.</strong> Bottom dips slightly in the center. Casual, coastal.</li>
      </ul>
      <p>With or without a blackout liner. Cordless or motorized lift. Right for kitchens, dining rooms, primary bedrooms (with blackout), nurseries, breakfast nooks.</p>

      <h2>Vignette Modern Romans (Hunter Douglas)</h2>
      <p>A specific premium line worth its own callout. Hunter Douglas <strong>Vignette</strong> is a modern Roman with no exposed cords or rear-mounted hardware — the fabric rolls into an integrated headrail when raised, eliminating the bulk of a traditional Roman fold. PowerView-motorized, beautifully engineered, and the most-installed Roman in our showroom.</p>

      <h2>Custom drapery</h2>
      <p>Floor-to-ceiling fabric panels — the most timeless treatment in the category, and the one that transforms a room more than any other. Drapery is sold as the panels themselves, plus a rod, plus hardware. We make them as a kit — custom-measured panels, custom-cut rod, ceiling-mounted brackets if appropriate.</p>

      <h3>What we tell every drapery client</h3>
      <ul>
        <li><strong>Hang the rod high.</strong> 6–10 inches above the casing, not on it. Floor-length panels look 2–3 feet taller when hung from a ceiling-mounted rod.</li>
        <li><strong>Skim the floor.</strong> Custom panels should kiss the floor, never puddle (unless puddle is the look you're after — but mind the dust).</li>
        <li><strong>Double the fullness.</strong> 2.0–2.5× the rod length in fabric width for proper drape. Skinny panels read cheap.</li>
        <li><strong>Line everything.</strong> Even sheer panels benefit from a sheer liner — adds weight, hangs better, lasts longer.</li>
      </ul>

      <p class="pull">A room is finished when the drapery hits the floor. Every time.</p>

      <h2>Sheers, valances, cornices, top treatments</h2>
      <ul>
        <li><strong>Sheers</strong> — translucent fabric panels, hung alone or layered behind drapery. The softest light filter in the catalogue.</li>
        <li><strong>Valances</strong> — short fabric treatment across the top of the window, covering the hardware. Traditional but coming back in transitional design.</li>
        <li><strong>Cornices</strong> — hard upholstered or wood top treatment. Architectural, formal, less common.</li>
        <li><strong>Top treatments</strong> — catchall for valance/cornice/swag combinations on bay windows and formal rooms.</li>
      </ul>

      <h2>Motorized drapery rods</h2>
      <p>Somfy Glydea, Lutron Sivoia, and Hunter Douglas Designer Drapery Rod all motorize a custom drapery rod. The drape traverses left or right (or both, from the center) on voice or remote command. Worth it on tall windows, wide rods, and primary bedrooms where the drape closes nightly. <a href="/blog/motorized-smart-shades-guide/">More on motorization here.</a></p>

      <h2>Skylight, French door, bay window, arched specialty</h2>
      <ul>
        <li><strong>Skylight shades</strong> — specialty cellular shades operated by pole or motor. The only honest answer to direct overhead sun.</li>
        <li><strong>French door shades</strong> — small cellular or roller shades mounted directly on the glass with a hold-down at the bottom. <a href="/blog/how-to-measure-windows-for-blinds/">Measuring guide here.</a></li>
        <li><strong>Bay window treatments</strong> — three or five separate inside-mount shades, coordinated by fabric and lift mechanism.</li>
        <li><strong>Arched windows</strong> — cardboard-templated, custom fabricated. Available in shutters, cellular, woven wood, and Roman.</li>
      </ul>

      <div class="callout">
        <h3>Our default soft-treatment spec</h3>
        <p>For a primary bedroom in a typical Tennessee home: <strong>2.5″ real-wood blinds on the side windows in a stain matched to trim, cream linen drapery panels on the center window, ceiling-mounted on a motorized rod.</strong> The combination most clients ask for the photo of.</p>
      </div>

      <h2>Cost ranges</h2>
      <ul>
        <li>Faux wood blinds, cordless: <strong>$90–$240 per window installed</strong></li>
        <li>Real wood blinds, cordless: <strong>$140–$420 per window installed</strong></li>
        <li>Vertical blinds / panel track for sliders: <strong>$340–$1,200 per opening</strong></li>
        <li>Flat or hobbled Roman shades: <strong>$280–$680 per window installed</strong></li>
        <li>Hunter Douglas Vignette Modern Roman: <strong>$420–$880 per window installed</strong></li>
        <li>Custom drapery panels (lined, custom): <strong>$380–$1,200 per panel</strong></li>
        <li>Motorized drapery rod: <strong>$1,200–$3,800 per rod</strong></li>
      </ul>

      <p>For a consultation that walks every soft treatment on the catalogue — wood blinds, drapery, Romans, valances, motorized rods — call or text <a href="tel:+16292988241">629-298-8241</a> or <a href="/#contact">book a free visit</a>.</p>
        """,
        "related": [
            ("/blog/plantation-wood-shutters-guide/", "Product guide · 8 min read", "Plantation &amp; <em>wood shutters</em>", "The harder counterpart to fabric drapery.", "/assets/images/blog/plantation-shutters.webp", "Plantation shutters in a Tennessee dining room"),
            ("/blog/how-to-measure-windows-for-blinds/", "How-to · 5 min read", "How to <em>measure windows</em> for blinds", "Before you order, three points each way.", "/assets/images/consultation-detail.webp", "Measuring tape on a window casing"),
        ],
    },
    {
        "slug": "affordable-faux-wood-blinds-guide",
        "title_html": "Affordable <em>faux wood blinds.</em>",
        "h1_plain": "Affordable Faux Wood Blinds: A Complete Guide",
        "meta_title": "Affordable Faux Wood Blinds (from $89 installed) · Stately Shades",
        "meta_desc": "Custom-fit faux wood blinds from $89 per window installed — 2-inch and 2.5-inch slats, cordless, humidity-proof, whole-house packages for builders and value-conscious Tennessee homeowners.",
        "eyebrow": "Service Guide · Affordable Everyday",
        "section": "Service Guide",
        "minutes": "6",
        "image": "/assets/images/blog/affordable-faux-wood.webp",
        "image_alt": "Three crisp white 2.5-inch faux wood blinds above a marble subway-tile backsplash in a sun-filled Tennessee kitchen",
        "caption": "Custom faux wood blinds in a Tennessee kitchen — from $89 per window installed.",
        "keywords": "affordable blinds, cheap custom blinds, faux wood blinds, 2 inch faux wood, 2.5 inch faux wood, cordless blinds, child-safe blinds, whole house blinds package, builder blinds, rental property blinds",
        "og_desc": "Custom-fit faux wood blinds from $89 per window installed — humidity-proof, child-safe, whole-house packages.",
        "tw_desc": "Affordable custom faux wood blinds from $89 installed. Whole-house packages, child-safe, humidity-proof.",
        "breadcrumb_name": "Affordable Faux Wood Blinds Guide",
        "body": """
      <p>Not every window in the house needs a $700 plantation shutter. Sometimes the right answer is a clean, durable, custom-fit faux wood blind for under a hundred dollars a window — and we sell as many of those as we do anything else. This is the complete guide to affordable blinds at Stately Shades: what faux wood is, what it costs, where it belongs, and where it doesn't.</p>

      <h2>The honest pitch</h2>
      <p>Custom-fit faux wood blinds at our showroom start at <strong>$89 per window installed</strong>. That number includes measure, slat custom-cut to your opening, cordless child-safe lift, white finish, brackets, valance, and our install crew putting it on the wall level. A whole-house package of 8–12 windows most often lands between <strong>$850 and $1,500 installed</strong>. The same measure-and-install care goes into every blind, regardless of price.</p>

      <h2>What faux wood actually is</h2>
      <p>Faux wood is a molded composite — usually a PVC, polystyrene, or wood-polymer hybrid — pressed into the same slat profile as real hardwood blinds. Looks like wood from across the room, weighs about 30% more (because it's denser), and shares zero of the weaknesses of real wood. Specifically:</p>
      <ul>
        <li><strong>Doesn't warp.</strong> Real hardwood blinds in a Tennessee kitchen will eventually cup or twist at the slat ends; faux wood will not.</li>
        <li><strong>Doesn't absorb moisture.</strong> Showers, dishwasher steam, laundry humidity — none of it matters.</li>
        <li><strong>Cleans with a damp cloth.</strong> Real wood needs to stay dry; faux wood is washable.</li>
        <li><strong>Holds finish longer.</strong> Factory-applied paint doesn't chip or yellow the way wood finishes do.</li>
      </ul>

      <h2>Slat sizes</h2>
      <ul>
        <li><strong>2&Prime; slats</strong> — the workhorse. Most-installed size, slimmer profile, looks proportional on small and medium windows.</li>
        <li><strong>2.5&Prime; slats</strong> — modestly more substantial, shows more view when open, the most-installed in our showroom this year. About $10–$20 more per window.</li>
        <li><strong>2.5&Prime; with cloth tapes</strong> — fabric strips covering the ladder cords. Slightly more formal, hides the stringing detail. Add $20–$40 per window.</li>
      </ul>

      <h2>Cordless is the default</h2>
      <p>Every faux wood blind we sell is <strong>cordless and child-safe</strong>, per the Window Covering Manufacturers Association standard. You lift by the bottom rail, lower with a soft tug. Corded versions are technically available from manufacturers but we won't quote them — there's no reason to put a cord in a house in 2026.</p>

      <p class="pull">A $89 faux wood blind installed by a pro outlasts a $300 shade installed wrong.</p>

      <h2>Finish options</h2>
      <ul>
        <li><strong>White</strong> — the standard. About six variations of white from cool to warm. No upcharge.</li>
        <li><strong>Cream and oat tones</strong> — match older trim, add warmth. No upcharge.</li>
        <li><strong>Stains (walnut, oak, espresso, chestnut)</strong> — printed on the slat to mimic real wood grain. Beautiful from a normal viewing distance, $15–$35 upcharge per window.</li>
        <li><strong>Custom colors</strong> — match a paint chip; add $40–$80 per window and 2 weeks lead time.</li>
      </ul>

      <h2>Where faux wood belongs</h2>
      <ul>
        <li><strong>Kitchens.</strong> Splash, grease, steam — faux wood handles all three.</li>
        <li><strong>Bathrooms.</strong> Steam doesn't care if your blinds are pretty. Faux wood survives.</li>
        <li><strong>Kids' bedrooms.</strong> Cordless safe, durable, easy to replace a slat if it gets snapped.</li>
        <li><strong>Basements, laundry rooms, mudrooms.</strong> Humidity-tolerant, no warping.</li>
        <li><strong>Rental properties.</strong> Cheaper to spec, longer service life, easy turnover.</li>
        <li><strong>Whole-house value packages.</strong> Builders, landlords, and first-home buyers — the affordability difference at scale is real.</li>
      </ul>

      <h2>Where faux wood doesn't belong</h2>
      <ul>
        <li><strong>Formal living and dining rooms</strong> where real-wood plantation shutters belong. The eye reads the difference at close range.</li>
        <li><strong>Very wide windows over 72&Prime;</strong> — faux wood is heavy enough that wide spans get awkward on a single blind. We split into two and either match them or move up to a different product.</li>
        <li><strong>Primary bedrooms needing true blackout.</strong> Faux wood is light-filtering at best; you'll always get sunrise leak through closed slats. <a href="/blog/best-blinds-for-bedrooms/">See bedroom blind options.</a></li>
      </ul>

      <div class="callout">
        <h3>Our default affordable spec</h3>
        <p><strong>Norman or Graber 2.5&Prime; faux wood blinds, cordless, white finish, inside-mount on most windows.</strong> Whole-house package pricing typically lands $90–$140 per window installed, with the per-window price coming down on larger orders. A typical 10-window project: <strong>$1,050–$1,300 installed.</strong></p>
      </div>

      <h2>What about real wood?</h2>
      <p>We also sell real-wood blinds — basswood, oak, alder — when stain match matters. Real wood is roughly 60–80% more expensive per window, looks identical from across the room, and lasts about the same time <em>provided</em> it's not in a wet space. <a href="/blog/wood-blinds-drapery-guide/">More on real wood here.</a></p>

      <h2>What about cellular or roller for a similar price?</h2>
      <p>Good question — and sometimes the answer is "yes, that's better." Affordable cellular shades start around $80/window and are a better choice for bedrooms (better blackout, better insulation). Affordable rollers start around $90 and are better for modern interiors. We'll talk you through which is right room by room — that's what the free consultation is for.</p>

      <h2>How to get a quote</h2>
      <p>Call or text <a href="tel:+16292988241">629-298-8241</a> with the rough window count for your project, or <a href="/#contact">use the contact form</a>. We come out, measure every window, and leave you with a written quote the same visit. If affordable is the priority, we lead with faux wood — and tell you honestly when something else would be a better value.</p>
        """,
        "extra_schema": """  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "What is the cheapest custom blind option?", "acceptedAnswer": { "@type": "Answer", "text": "Custom-fit faux wood blinds are the most affordable option, starting at $89 per window installed at Stately Shades. They are humidity-proof, cordless and child-safe by default, available in 2-inch and 2.5-inch slats, and look like real wood at roughly half the cost." } },
    { "@type": "Question", "name": "How much does a whole house of faux wood blinds cost in Tennessee?", "acceptedAnswer": { "@type": "Answer", "text": "A whole-house package of 8 to 12 faux wood blinds in Middle Tennessee typically runs $850 to $1,500 installed, depending on window count, slat size, and finish. Per-window pricing comes down at scale." } },
    { "@type": "Question", "name": "Are faux wood blinds good for kitchens and bathrooms?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Faux wood blinds are humidity-proof and washable, which makes them the ideal choice for kitchens, bathrooms, laundry rooms, and basements where real hardwood blinds would warp or absorb moisture." } },
    { "@type": "Question", "name": "Is faux wood a good rental property blind?", "acceptedAnswer": { "@type": "Answer", "text": "Faux wood is the most-installed rental-property blind because it is durable, easy to clean, cordless and child-safe for tenant safety, and inexpensive enough to replace if damaged on turnover. Whole-rental packages typically run $90 to $140 per window installed." } }
  ]}
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "SpeakableSpecification", "cssSelector": [".article-hero h1", ".article-hero__inner .eyebrow", ".prose p:first-of-type", ".callout p"] }
  </script>""",
        "related": [
            ("/blog/wood-blinds-drapery-guide/", "Product guide · 7 min read", "Wood blinds &amp; <em>custom drapery</em>", "The premium catalogue counterpart.", "/assets/images/blog/wood-blinds-drapery.webp", "Wood blinds and drapery in a Tennessee bedroom"),
            ("/blog/install-only-blinds-service-guide/", "Service guide · 6 min read", "You bought, <em>we install.</em>", "Already ordered? We'll hang them for you.", "/assets/images/blog/install-only-service.webp", "Installing a blind on a window casing"),
        ],
    },
    {
        "slug": "install-only-blinds-service-guide",
        "title_html": "Install only. <em>You bought, we install.</em>",
        "h1_plain": "Install-Only Blind & Shutter Service: Bring-Your-Own",
        "meta_title": "Install Only: We Install Blinds You Bought at Lowes, Home Depot, Costco · Stately Shades",
        "meta_desc": "Professional install-only service across Middle Tennessee for blinds, shutters, and shades purchased from Lowes, Home Depot, Costco, Blinds.com, Select Blinds, Amazon, IKEA, or any other retailer. Flat-rate per window with workmanship guarantee.",
        "eyebrow": "Service Guide · Install Only · BYO Blinds",
        "section": "Service Guide",
        "minutes": "6",
        "image": "/assets/images/blog/install-only-service.webp",
        "image_alt": "Hands holding a level dark-finish blind against a Tennessee window casing while installing — Home Depot boxes on the drop cloth below",
        "caption": "Boxes from the home-improvement store, blind on the wall — what install-only service looks like.",
        "keywords": "install only blinds, blind installation service, byo blinds, blinds.com install, Home Depot blinds install, Lowes blinds install, Costco blinds installer, professional blind installer near me, Tennessee blind installation",
        "og_desc": "We install blinds, shutters, and shades you bought from Lowes, Home Depot, Costco, Blinds.com — anywhere. Flat-rate, any brand.",
        "tw_desc": "Stack of unopened blind boxes? We do install-only service across Middle Tennessee. Any brand, flat-rate.",
        "breadcrumb_name": "Install-Only Service Guide",
        "body": """
      <p>You did the homework. You measured the windows, picked the product, ordered online, and now you have a stack of boxes from Lowes or Home Depot or Blinds.com sitting in your garage and a Saturday that you'd rather not spend on a stepladder. We get the call several times a week — and yes, <strong>we install blinds you bought somewhere else</strong>. This is the complete guide to install-only service at Stately Shades.</p>

      <h2>What "install only" actually means</h2>
      <p>You bought the product. We do everything else:</p>
      <ul>
        <li><strong>Unbox</strong> every blind and check it against the manufacturer's packing slip for damage.</li>
        <li><strong>Verify dimensions</strong> against your openings — if there's a mismatch, we tell you before we drill.</li>
        <li><strong>Measure twice</strong> from the brackets to the bottom rail to confirm symmetry.</li>
        <li><strong>Mount level</strong>. The single most common mistake on a DIY install is a hairline of tilt that nobody notices until the lift cord doesn't track.</li>
        <li><strong>Program motorized hardware</strong> — pair it to your hub, set limits, walk you through the app.</li>
        <li><strong>Demo the mechanism</strong> — show you how to lift, tilt, replace batteries, troubleshoot.</li>
        <li><strong>Haul away packaging</strong>. The cardboard fortress is not yours to break down.</li>
      </ul>

      <h2>Retailers we install from</h2>
      <p>Any of them. We do not care where you bought the blinds — only that they're a real product in good condition. The list of stores we install from most often:</p>
      <ul>
        <li><strong>Lowes</strong> (Levolor, Custom Size Now, Allen + Roth)</li>
        <li><strong>Home Depot</strong> (Hampton Bay, Bali, Custom Blinds)</li>
        <li><strong>Costco</strong> (in-warehouse and Costco.com)</li>
        <li><strong>Blinds.com</strong> (and its sister sites)</li>
        <li><strong>Select Blinds</strong></li>
        <li><strong>Amazon</strong> (Chicology, Yoolax, generic faux wood, etc.)</li>
        <li><strong>IKEA</strong> (FYRTUR, KADRILJ, etc.)</li>
        <li><strong>Wayfair</strong></li>
        <li><strong>Bali Direct, Levolor Direct</strong></li>
        <li><strong>Builder leftovers</strong> from a previous project</li>
        <li><strong>Anything else</strong> — we've installed brands we've never heard of.</li>
      </ul>

      <h2>What we charge</h2>
      <p>Flat-rate per window. Pricing in 2026 across the Middle Tennessee 90-mile radius:</p>
      <ul>
        <li><strong>Standard horizontal blinds</strong> (wood, faux wood, mini, aluminum): <strong>$45–$65/window</strong></li>
        <li><strong>Cellular, roller, Roman, solar shades</strong>: <strong>$55–$75/window</strong></li>
        <li><strong>Vertical blinds, panel-track systems for sliders</strong>: <strong>$95–$160/opening</strong></li>
        <li><strong>Plantation shutters</strong> (per panel hung &amp; tensioned): <strong>$65–$140/window</strong></li>
        <li><strong>Motorized shades</strong> with programming &amp; hub pairing: <strong>$95–$180/shade</strong></li>
        <li><strong>French-door, arched, skylight, specialty shapes</strong>: quoted on site</li>
        <li><strong>Service-call minimum</strong>: $185 (3 windows or fewer)</li>
      </ul>
      <p>A typical 8-window install-only project lands between <strong>$360 and $720</strong>, parts included from your own boxes.</p>

      <div class="callout">
        <h3>The workmanship guarantee</h3>
        <p>Every install we do — even on blinds we didn't sell you — is backed by our <strong>workmanship guarantee</strong>. If a bracket pulls out of the wall, if the headrail levels itself out within 90 days, if a motor we programmed loses its limits — we come back and fix it on us. Product defects are still on the retailer's warranty, but the install is on us.</p>
      </div>

      <h2>What we ask of you before we arrive</h2>
      <ol>
        <li><strong>Open the boxes</strong> and verify quantities. Six windows ordered, six headrails delivered — we don't want to discover a missing piece on install day.</li>
        <li><strong>Lay out the boxes by room</strong>. Saves us the matching dance.</li>
        <li><strong>Have the receipt handy</strong> in case anything needs returning.</li>
        <li><strong>Clear the windows.</strong> Move furniture, plants, drapery rods if they're being replaced. We can do this ourselves at a small upcharge.</li>
        <li><strong>Tell us about motors</strong>. If anything is motorized, confirm the hub is bought and the Wi-Fi password is handy.</li>
      </ol>

      <p class="pull">The blind is yours. The level wall, the symmetry, the workmanship guarantee — those are ours.</p>

      <h2>Common scenarios</h2>

      <h3>"I bought blinds at Home Depot a year ago and never installed them."</h3>
      <p>Very common. We've installed sealed Home Depot boxes that were 2–3 years old. Manufacturer warranty is typically still valid as long as the product hasn't been opened. Bring us the boxes; we'll measure your windows and confirm fit before we drill.</p>

      <h3>"I ordered the wrong size."</h3>
      <p>Happens. If the blind is too wide we can sometimes trim it in the field (faux wood and aluminum), or you can return and re-order with the dimensions we'll measure on the first visit. Service-call minimum applies if you'd rather we just measure now and come back after the re-order.</p>

      <h3>"It's a complicated install — arches, sliders, plantation shutters."</h3>
      <p>Especially worth hiring an installer for. Specialty installs are where DIY most often goes wrong, and where a botched mount can damage the blind enough to void the warranty.</p>

      <h3>"I bought motorized shades and the app won't pair."</h3>
      <p>This is most of what we do for motorized service calls. PowerView, Somfy TaHoma, Lutron Caseta — we pair them, set the limits, walk you through the scenes. About $95–$180 per shade plus the service call.</p>

      <h3>"I want to install some myself and have you do the hard ones."</h3>
      <p>Totally normal. Tell us which windows on the consultation visit and we'll quote just those.</p>

      <h2>Where install-only doesn't make sense</h2>
      <ul>
        <li><strong>If the product is broken on arrival.</strong> Return it to the retailer before we visit; we can't certify a broken blind.</li>
        <li><strong>If you're missing major components.</strong> No mounting brackets, no install. Get the parts first.</li>
        <li><strong>If you'd save more by buying through us anyway.</strong> Sometimes our custom-fit faux wood at $89/window installed beats the Lowes price plus our install fee. We'll tell you honestly on the visit.</li>
      </ul>

      <h2>Service area</h2>
      <p>We install across the same 90-mile radius we always cover — Gallatin, Nashville, Hendersonville, Franklin, Brentwood, Murfreesboro, Mt. Juliet, Lebanon, Goodlettsville, Cookeville, Clarksville, Springfield, Bowling Green KY, and every town in between.</p>

      <h2>How to schedule</h2>
      <p>Photograph each blind's box label (or just the inside flap with the dimensions) plus the windows they'll go on. Text the photos to <strong>629-298-8241</strong> with your address. We quote from the photos within a few hours and book the install day — most jobs scheduled within a week.</p>

      <p>Or call or text <a href="tel:+16292988241">629-298-8241</a>, email <a href="mailto:hello@statelyshades.com">hello@statelyshades.com</a>, or <a href="/#contact">use the contact form</a> and we'll be in touch within one business day.</p>
        """,
        "extra_schema": """  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "Will you install blinds I bought from Home Depot or Lowes?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Stately Shades offers install-only service across the Middle Tennessee 90-mile radius for blinds, shutters, and shades purchased at Home Depot, Lowes, Costco, Blinds.com, Select Blinds, Amazon, IKEA, or any other retailer. We unbox, measure, mount level, demo the mechanism, and haul away the packaging. Flat-rate per window with a workmanship guarantee." } },
    { "@type": "Question", "name": "How much does it cost to have blinds installed professionally in Tennessee?", "acceptedAnswer": { "@type": "Answer", "text": "Professional install-only pricing in Middle Tennessee in 2026 is $45 to $85 per window for standard blinds and shades, $65 to $140 per window for plantation shutters, and $95 to $180 per shade for motorized treatments including programming. The service-call minimum is $185 for three windows or fewer." } },
    { "@type": "Question", "name": "Can you install Blinds.com window treatments?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. We install Blinds.com products regularly — they are one of the most common retailers our install-only customers buy from. We verify dimensions against your openings before drilling and back the install with our workmanship guarantee." } },
    { "@type": "Question", "name": "Do you install Costco blinds?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Costco blinds (both in-warehouse and Costco.com) are a frequent install-only product for us. Same flat-rate per window pricing, same workmanship guarantee." } },
    { "@type": "Question", "name": "What if my measurements are wrong?", "acceptedAnswer": { "@type": "Answer", "text": "We verify dimensions against your openings before we drill. If a blind is too wide we can sometimes trim it in the field (faux wood and aluminum), or you can return and re-order with the dimensions we measure on the first visit. Our service-call minimum applies if we measure now and return after the re-order." } }
  ]}
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "SpeakableSpecification", "cssSelector": [".article-hero h1", ".article-hero__inner .eyebrow", ".prose p:first-of-type", ".callout p"] }
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "Service", "@id": "https://statelyshades.com/blog/install-only-blinds-service-guide/#install-only-service", "name": "Install-Only / Bring-Your-Own-Blinds Service", "serviceType": "Window Treatment Installation Service", "provider": { "@type": "LocalBusiness", "name": "Stately Shades", "telephone": "+1-629-298-8241", "address": { "@type": "PostalAddress", "addressLocality": "Gallatin", "addressRegion": "TN", "addressCountry": "US" } }, "areaServed": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": 36.3881, "longitude": -86.4467 }, "geoRadius": "144841" }, "audience": { "@type": "Audience", "name": "Homeowners with self-purchased blinds, shutters, or shades from Lowes, Home Depot, Costco, Blinds.com, Select Blinds, Amazon, IKEA, or any other retailer" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "45", "highPrice": "180", "priceSpecification": { "@type": "UnitPriceSpecification", "priceCurrency": "USD", "unitText": "window installed" } } }
  </script>""",
        "related": [
            ("/blog/affordable-faux-wood-blinds-guide/", "Service guide · 6 min read", "Affordable <em>faux wood blinds</em>", "Skip the retailer — custom at $89.", "/assets/images/blog/affordable-faux-wood.webp", "Affordable faux wood blinds in a Tennessee kitchen"),
            ("/blog/how-to-measure-windows-for-blinds/", "How-to · 5 min read", "How to <em>measure windows</em> for blinds", "Before you order, measure right.", "/assets/images/consultation-detail.webp", "Measuring tape on a window casing"),
        ],
    },
    # ------------- 4 SEO/AEO/AIO/GEO-targeted posts ----------------------
    {
        "slug": "affordable-blinds-nashville-tennessee",
        "title_html": "Affordable blinds <em>near me</em> · Nashville &amp; Middle TN.",
        "h1_plain": "Affordable Blinds Near Me in Nashville & Middle Tennessee",
        "meta_title": "Cheap Custom Blinds Near Me · Nashville TN (from $89) · Stately Shades",
        "meta_desc": "Looking for affordable custom blinds near me in Nashville, Hendersonville, Gallatin, Franklin, or anywhere across Middle Tennessee? Faux wood from $89/window installed. Free in-home quote within 90 miles.",
        "eyebrow": "Local · Affordable · Middle TN",
        "section": "Local Service",
        "minutes": "6",
        "image": "/assets/images/blog/affordable-faux-wood.webp",
        "image_alt": "Affordable white 2.5-inch faux wood blinds in a sunlit Nashville-area kitchen",
        "caption": "Custom-fit faux wood blinds — affordable, professionally installed, across Middle Tennessee.",
        "keywords": "affordable blinds Nashville, cheap blinds near me, custom blinds Tennessee, faux wood blinds Gallatin, blinds installation Franklin TN, Brentwood blinds, Murfreesboro blinds, Hendersonville window treatments, budget blinds, blinds near me",
        "og_desc": "Affordable custom blinds across Nashville, Gallatin, Hendersonville, Franklin, Brentwood — from $89/window installed.",
        "tw_desc": "Cheap custom blinds near you in Middle TN? Faux wood from $89 installed. Free in-home quote.",
        "breadcrumb_name": "Affordable Blinds Near Me · Nashville TN",
        "body": """
      <p>Searching <em>"affordable blinds near me,"</em> <em>"cheap custom blinds Nashville,"</em> or <em>"budget blinds Tennessee"</em> and getting nowhere except big-box price calculators that don't include install? You're in the right place. Stately Shades is a family-owned dealer in Gallatin, Tennessee, and our most popular product is also our most affordable: <strong>custom-fit faux wood blinds starting at $89 per window installed</strong>. This guide explains exactly what affordable looks like at our showroom, who it's for, and which cities we serve.</p>

      <h2>What "affordable" actually means at Stately Shades</h2>
      <p>Three numbers cover most of the affordable catalogue in Middle Tennessee in 2026:</p>
      <ul>
        <li><strong>$89 per window installed</strong> — 2&Prime; or 2.5&Prime; faux wood blind, cordless, white finish, custom-fit to your opening, professionally hung level.</li>
        <li><strong>$850–$1,500</strong> — whole-house package of 8–12 faux wood windows, fully installed, including a free in-home measure and a written quote on the first visit.</li>
        <li><strong>$0</strong> — what the consultation and the measure and the quote cost you. Free, every time, within 90 miles of Gallatin.</li>
      </ul>

      <h2>Cities we serve with affordable custom blinds</h2>
      <p>Our 90-mile radius from Gallatin covers most of Middle Tennessee and a slice of southern Kentucky. We install affordable custom blinds in:</p>
      <ul>
        <li><strong>Nashville</strong> — Green Hills, East Nashville, Belle Meade, 12 South, the Gulch, Donelson, Antioch, Bellevue, Hermitage.</li>
        <li><strong>Hendersonville</strong> — Sanders Ferry, Beech Bend, downtown Hendersonville.</li>
        <li><strong>Gallatin</strong> — our showroom is here. Foxland, Long Hollow, Fairvue.</li>
        <li><strong>Franklin</strong> — Westhaven, McKay's Mill, Cool Springs, downtown.</li>
        <li><strong>Brentwood</strong> — Concord, Maryland Farms.</li>
        <li><strong>Murfreesboro</strong> — Blackman, MTSU area, downtown.</li>
        <li><strong>Mount Juliet, Lebanon, Goodlettsville, Springfield, Smyrna, Spring Hill, Cookeville, Clarksville.</strong></li>
        <li><strong>Bowling Green, KY</strong> and the border counties.</li>
      </ul>
      <p>If you can drive to our Gallatin showroom in under 90 minutes, we drive to you for free.</p>

      <p class="pull">Affordable doesn't mean stock-sized. Every blind we sell is cut to your window, even at $89.</p>

      <h2>The cheapest <em>custom</em> blind — faux wood</h2>
      <p>The lowest-cost custom blind in our showroom is a 2&Prime; or 2.5&Prime; faux wood horizontal blind. It is:</p>
      <ul>
        <li><strong>Custom-cut to your exact opening</strong> (not a stock 36×60 that doesn't fit).</li>
        <li><strong>Cordless and child-safe</strong> — meets WCMA safety standards by default.</li>
        <li><strong>Humidity-proof</strong> — won't warp like real wood in kitchens, baths, or basements.</li>
        <li><strong>Available in white, cream, oat, and printed-grain stains</strong> (walnut, oak, espresso).</li>
        <li><strong>Backed by manufacturer warranty</strong> from Norman, Graber, or Bali.</li>
        <li><strong>Professionally measured and installed</strong>, with our workmanship guarantee.</li>
      </ul>
      <p>For the deep-dive on faux wood specifically — sizes, finishes, where it belongs — see our <a href="/blog/affordable-faux-wood-blinds-guide/">complete faux wood blinds guide</a>.</p>

      <h2>Who buys affordable blinds from us</h2>
      <ul>
        <li><strong>First-home buyers in the Nashville metro</strong> furnishing 8–14 windows on a budget.</li>
        <li><strong>Landlords and property managers</strong> outfitting rentals across Davidson, Sumner, Williamson, and Rutherford counties.</li>
        <li><strong>Builders</strong> doing builder-grade-replacement upgrades on spec homes.</li>
        <li><strong>Homeowners with a long honest-do list</strong> — the kitchen needs custom shutters, the kids' rooms need faux wood, and one budget covers both.</li>
        <li><strong>Anyone with a single problem window</strong> — a bath, a basement, a garage office — who doesn't want to pay $400/window for one shade.</li>
      </ul>

      <h2>How affordable compares to big-box</h2>
      <p>A 36×60 faux wood blind from a big-box store (Home Depot, Lowes) is typically <strong>$45–$95 unboxed, plus install</strong> if you hire it out. Their install averages $40–$70 per window if the installer agrees to come at all — many won't for under five blinds. Total: <strong>$85–$165 per window</strong>, with no in-home measure and no follow-up if something's wrong.</p>
      <p>Our $89/window includes the custom dimensions, the install, the measure visit, the workmanship guarantee, and the same-week scheduling. <em>And</em> if a slat gets damaged in year two, we replace it for cost.</p>

      <div class="callout">
        <h3>The affordable spec we install most</h3>
        <p><strong>Norman 2.5&Prime; faux wood, cordless, white, inside-mount.</strong> Average installed price in 2026 across the Nashville metro: <strong>$92–$118 per window</strong>, falling to as low as $89 on whole-house packages.</p>
      </div>

      <h2>Other affordable options we sell</h2>
      <ul>
        <li><strong>Single-cell cellular shades, cordless</strong> — from $80/window. Better for bedrooms (light insulation, sound dampening).</li>
        <li><strong>Light-filtering roller shades</strong> — from $90/window. Cleaner, modern.</li>
        <li><strong>2&Prime; faux wood</strong> — slightly cheaper than 2.5&Prime;, $5–$15 less per window.</li>
        <li><strong>1&Prime; aluminum mini-blinds</strong> — from $55/window. Bare-bones bath or laundry option.</li>
      </ul>

      <h2>Already bought your blinds? We install those too.</h2>
      <p>If affordable for you means buying online at Blinds.com or driving to Lowes, that's also fine — we offer <a href="/blog/install-only-blinds-service-guide/"><strong>install-only service</strong></a> across the same 90-mile radius. Flat-rate per window, professional install, workmanship guarantee. Both routes get you a window dressed correctly; the right one depends on what you'd rather optimize for — price, custom fit, or your Saturday.</p>

      <h2>How to get an affordable quote</h2>
      <p>Three ways:</p>
      <ol>
        <li><strong>Text us photos of the windows</strong> at <a href="tel:+16292988241">629-298-8241</a> with rough dimensions. We can give you a ballpark within an hour.</li>
        <li><strong>Book a free in-home consultation</strong> via <a href="/#contact">our contact form</a>. We measure every window and leave you a written quote the same visit.</li>
        <li><strong>Call</strong> <a href="tel:+16292988241">629-298-8241</a> and tell us how many windows. We can sometimes price-quote on the phone for straightforward jobs.</li>
      </ol>

      <p>No travel fee within 90 miles. No consultation fee. No pressure to buy.</p>
        """,
        "extra_schema": """  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "What is the cheapest custom blind I can get installed in Nashville?", "acceptedAnswer": { "@type": "Answer", "text": "The cheapest custom blind professionally installed in the Nashville metro and across Middle Tennessee is a faux wood blind from Stately Shades, starting at $89 per window installed. This includes the custom measure, the cordless child-safe blind, the install, and a workmanship guarantee." } },
    { "@type": "Question", "name": "Where can I find cheap custom blinds near me in Tennessee?", "acceptedAnswer": { "@type": "Answer", "text": "Stately Shades sells affordable custom blinds from $89 per window across a 90-mile radius from Gallatin, Tennessee — including Nashville, Hendersonville, Franklin, Brentwood, Murfreesboro, Mt. Juliet, Lebanon, Spring Hill, Goodlettsville, Springfield, Cookeville, Clarksville, and across into Bowling Green, Kentucky." } },
    { "@type": "Question", "name": "Are custom blinds cheaper than Home Depot blinds with installation?", "acceptedAnswer": { "@type": "Answer", "text": "Often yes. A big-box faux wood blind plus separate install in Tennessee typically totals $85 to $165 per window with no in-home measure. Stately Shades custom faux wood is $89 per window installed including the measure, install, and workmanship guarantee — usually within $5 to $10 of the big-box total, with custom dimensions and follow-up support." } },
    { "@type": "Question", "name": "Do you serve my city for affordable blinds?", "acceptedAnswer": { "@type": "Answer", "text": "Yes if you are within 90 miles of Gallatin, TN. Coverage includes Nashville, Hendersonville, Gallatin, Franklin, Brentwood, Murfreesboro, Mt. Juliet, Lebanon, Goodlettsville, Springfield, Smyrna, Spring Hill, Cookeville, Clarksville, and parts of southern Kentucky including Bowling Green." } },
    { "@type": "Question", "name": "Is the in-home consultation really free?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. No charge for the in-home consultation, no travel fee within 90 miles of Gallatin, and no obligation to buy. We bring physical samples, measure precisely, and leave a written quote at the visit." } }
  ]}
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "SpeakableSpecification", "cssSelector": [".article-hero h1", ".prose p:first-of-type", ".callout p"] }
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "Service", "@id": "https://statelyshades.com/blog/affordable-blinds-nashville-tennessee/#service", "name": "Affordable Custom Blinds Installation — Nashville & Middle Tennessee", "serviceType": "Custom Blinds Sales and Installation", "provider": { "@type": "LocalBusiness", "name": "Stately Shades", "telephone": "+1-629-298-8241", "url": "https://statelyshades.com/", "address": { "@type": "PostalAddress", "addressLocality": "Gallatin", "addressRegion": "TN", "postalCode": "37066", "addressCountry": "US" } }, "areaServed": [ { "@type": "City", "name": "Nashville", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Hendersonville", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Gallatin", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Franklin", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Brentwood", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Murfreesboro", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Mount Juliet", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Lebanon", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Spring Hill", "containedInPlace": { "@type": "State", "name": "Tennessee" } }, { "@type": "City", "name": "Bowling Green", "containedInPlace": { "@type": "State", "name": "Kentucky" } } ], "offers": { "@type": "Offer", "priceCurrency": "USD", "price": "89", "priceSpecification": { "@type": "UnitPriceSpecification", "price": "89", "priceCurrency": "USD", "unitText": "window installed" }, "availability": "https://schema.org/InStock" } }
  </script>""",
        "related": [
            ("/blog/affordable-faux-wood-blinds-guide/", "Service guide · 6 min read", "Affordable <em>faux wood blinds</em>", "Deeper dive on the cheapest custom option.", "/assets/images/blog/affordable-faux-wood.webp", "Affordable faux wood blinds in a Tennessee kitchen"),
            ("/blog/best-blinds-for-rental-properties/", "Service guide · 6 min read", "Best blinds for <em>rental properties</em>", "The landlord's playbook.", "/assets/images/blog/rental-property-blinds.webp", "Rental property living room with white blinds"),
        ],
    },
    {
        "slug": "best-blinds-for-rental-properties",
        "title_html": "Best blinds for <em>rental properties.</em>",
        "h1_plain": "Best Blinds for Rental Properties (Landlord's Guide)",
        "meta_title": "Best Blinds for Rental Properties (2026 Landlord's Guide) · Stately Shades",
        "meta_desc": "The best blinds for rental properties in Tennessee — durable, child-safe, tenant-proof, easy to replace on turnover. Whole-rental packages from $850. Bulk landlord pricing across Middle TN.",
        "eyebrow": "Service Guide · Landlord & Property Management",
        "section": "Service Guide",
        "minutes": "6",
        "image": "/assets/images/blog/rental-property-blinds.webp",
        "image_alt": "A clean rental property living room with crisp white faux wood blinds on three large windows, ready for tenant move-in",
        "caption": "Faux wood, cordless, white — the rental landlord's default.",
        "keywords": "blinds for rental property, landlord blinds, rental property window treatments, tenant blinds, multi-unit blinds, builder blinds, Airbnb blinds, durable blinds, child-safe rental blinds, bulk landlord pricing",
        "og_desc": "The landlord's playbook for blinds — durable, child-safe, tenant-proof, easy to replace on turnover.",
        "tw_desc": "Best blinds for rental properties: durable faux wood from $89/window. Bulk landlord pricing across Middle TN.",
        "breadcrumb_name": "Best Blinds for Rental Properties",
        "body": """
      <p>Rental property blinds have a job description that retail blinds don't. They have to survive tenants who slam them shut. They have to be child-safe by default (a tenant-safety lawsuit risk worth taking seriously). They have to clean up to "rent-ready" in five minutes between turnovers. And they have to be cheap enough that replacing a damaged slat doesn't blow the maintenance budget. This is the landlord's playbook for blinds we've developed across hundreds of rental units in Middle Tennessee.</p>

      <h2>The rental landlord's four requirements</h2>
      <ol>
        <li><strong>Durable.</strong> Survives slamming, pet claws, sun, humidity. No real wood — it warps. No fancy cellular — fragile.</li>
        <li><strong>Child-safe / cord-free.</strong> Mandatory in any property that might house families. Cordless lift only.</li>
        <li><strong>Easy to clean and turn over.</strong> Washable, replaceable slats, no fabric to dry-clean.</li>
        <li><strong>Affordable enough to absorb damage.</strong> Replace a slat for $20, not the whole blind.</li>
      </ol>
      <p>One product hits all four reliably: <strong>2.5&Prime; faux wood, cordless, white.</strong></p>

      <h2>Why faux wood wins for rentals</h2>
      <ul>
        <li><strong>Humidity-proof.</strong> Bathrooms, kitchens, laundries — no warping. Real wood would fail in 2–3 years.</li>
        <li><strong>Washable.</strong> Damp microfiber removes most of what a tenant leaves behind. Heavier grime cleans with mild soap.</li>
        <li><strong>Replaceable slats.</strong> Snap a single slat? $20 part, 5-minute swap. We keep the most common slat sizes in stock for landlord clients.</li>
        <li><strong>Cordless is the default</strong>, so the WCMA child-safety standard is met without adding a cleat or a wall anchor.</li>
        <li><strong>Cheap enough to spec at scale.</strong> $89/window installed, falling to $75–$85/window on multi-unit landlord packages.</li>
      </ul>

      <p class="pull">Tenants change every year or two. The blinds should change every fifteen.</p>

      <h2>The Stately Shades landlord package</h2>
      <p>For landlords and property managers across Middle Tennessee, we offer a structured pricing tier:</p>
      <ul>
        <li><strong>Per-unit pricing</strong>: $75–$95 per window installed on multi-unit orders (10+ windows).</li>
        <li><strong>Turnover slat replacement</strong>: $20 per slat, scheduled around your turn calendar.</li>
        <li><strong>One-call scheduling</strong>: text the address and unit number, we book the install within the week.</li>
        <li><strong>Single point of contact</strong> for your whole portfolio — no juggling multiple sub-contractors.</li>
        <li><strong>Net-30 invoicing</strong> on landlord accounts (after the first project).</li>
      </ul>
      <p>If you run more than 20 doors in our service area, ask about bulk landlord pricing on the first call.</p>

      <h2>What we install at a typical rental</h2>
      <p>A 2-bedroom rental with 9 windows is a representative project. Typical spec:</p>
      <ul>
        <li><strong>Living room</strong>: 2.5&Prime; faux wood, white, cordless. 3 windows × $85 = $255.</li>
        <li><strong>Kitchen</strong>: 2&Prime; faux wood (slimmer profile), white. 1 window × $80 = $80.</li>
        <li><strong>Bathroom</strong>: 2&Prime; faux wood. 1 window × $80 = $80.</li>
        <li><strong>Bedroom 1 (primary)</strong>: 2.5&Prime; faux wood, white. 2 windows × $85 = $170.</li>
        <li><strong>Bedroom 2</strong>: 2.5&Prime; faux wood, white. 2 windows × $85 = $170.</li>
      </ul>
      <p><strong>Total: $755 for the unit, fully installed.</strong> Add roughly 10% if any windows need outside-mount or specialty trim.</p>

      <h2>Where to upgrade past faux wood</h2>
      <p>Two upgrades worth considering on a rental, depending on tenant tier:</p>
      <ul>
        <li><strong>Bedroom blackout cellular</strong> — $140–$200/window. Higher-end rentals or short-term/Airbnb properties benefit from the better blackout and insulation. Tenants notice.</li>
        <li><strong>Roller shades</strong> with a cleaner modern look — $90–$140/window. Worth it for higher-rent units (>$2,500/month) where the visual impression at showings matters.</li>
      </ul>
      <p>For everything else — 80% of the doors — faux wood is right.</p>

      <h2>Short-term rentals (Airbnb, VRBO)</h2>
      <p>Short-term rentals are blind-stress at 10× the rate. Five different guests in a month, each with a different idea of how a blind operates. Two notes specific to STRs:</p>
      <ul>
        <li><strong>Use top-down/bottom-up cellulars in primary bedrooms.</strong> Guests get privacy + view, and review scores notice.</li>
        <li><strong>Avoid drapery.</strong> Fabric is a cleaning nightmare and stains catastrophically. Roller shades behind faux drapery (visually layered) is the photogenic compromise.</li>
      </ul>

      <div class="callout">
        <h3>Our 2026 landlord default spec</h3>
        <p><strong>Norman or Bali 2.5&Prime; faux wood, cordless, white, inside-mount on every window in the unit.</strong> Whole-unit cost typical $650–$950 installed, depending on window count. Same product across the portfolio = same replacement slat inventory.</p>
      </div>

      <h2>Tenant safety: the legal note</h2>
      <p>The Window Covering Manufacturers Association requires cordless or inaccessible-cord operating systems on all stock window coverings sold for residential use as of 2018. Most states (including Tennessee) align with this standard. Installing corded blinds in a rental property in 2026 is a real liability risk if a child or pet is harmed — and we won't sell them. Every blind we install in a rental is cordless by default.</p>

      <h2>How to get rental pricing</h2>
      <p>Text or call <a href="tel:+16292988241">629-298-8241</a> with the address, unit count, and rough window count per unit. We'll quote landlord pricing on the first conversation and book the measure visit within the week. <a href="/#contact">Or use the contact form</a>.</p>

      <p>We work with landlords and property managers across Davidson, Sumner, Wilson, Williamson, Rutherford, Robertson, Cheatham, and surrounding counties.</p>
        """,
        "extra_schema": """  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "What is the best blind for a rental property?", "acceptedAnswer": { "@type": "Answer", "text": "The best rental property blind is a 2.5-inch faux wood horizontal blind with cordless child-safe lift in white. It is humidity-proof, durable, washable, replaceable slat by slat on damage, and inexpensive enough to absorb tenant wear. At Stately Shades it runs $75 to $95 per window installed on landlord packages of 10 or more windows." } },
    { "@type": "Question", "name": "Are landlords required to install cord-free blinds?", "acceptedAnswer": { "@type": "Answer", "text": "While there is no federal law in Tennessee specifically requiring cord-free blinds in rentals, the Window Covering Manufacturers Association standard (effective 2018) requires cordless or inaccessible-cord systems on all stock residential blinds. Installing corded blinds in a rental property creates real tenant-safety liability and is no longer industry standard. Every blind Stately Shades installs is cordless by default." } },
    { "@type": "Question", "name": "How much do blinds for a rental unit cost?", "acceptedAnswer": { "@type": "Answer", "text": "A typical 9-window 2-bedroom rental unit runs $650 to $950 installed for cordless 2-inch and 2.5-inch faux wood blinds in white. Multi-unit landlord packages bring the per-window price down to $75 to $95." } },
    { "@type": "Question", "name": "Can you install blinds across multiple rental units at once?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. We work with landlords and property managers across Middle Tennessee on multi-unit projects, with a single point of contact, scheduled installs around your turn calendar, and net-30 invoicing on established accounts. Bulk landlord pricing applies on portfolios of 10+ windows." } },
    { "@type": "Question", "name": "What is the best blind for an Airbnb or short-term rental?", "acceptedAnswer": { "@type": "Answer", "text": "For Airbnb and short-term rentals we recommend faux wood blinds throughout, with top-down/bottom-up cellular shades upgraded into the primary bedroom for privacy and review-score impact. Avoid drapery in STRs — fabric stains catastrophically with high guest turnover." } }
  ]}
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "SpeakableSpecification", "cssSelector": [".article-hero h1", ".prose p:first-of-type", ".callout p"] }
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "Service", "@id": "https://statelyshades.com/blog/best-blinds-for-rental-properties/#landlord-service", "name": "Landlord & Multi-Unit Blind Installation Service", "serviceType": "Multi-Property Window Treatment Installation", "provider": { "@type": "LocalBusiness", "name": "Stately Shades", "telephone": "+1-629-298-8241", "address": { "@type": "PostalAddress", "addressLocality": "Gallatin", "addressRegion": "TN", "addressCountry": "US" } }, "areaServed": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": 36.3881, "longitude": -86.4467 }, "geoRadius": "144841" }, "audience": { "@type": "Audience", "name": "Landlords, property managers, multi-family operators, short-term rental hosts in Middle Tennessee" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "75", "highPrice": "95", "priceSpecification": { "@type": "UnitPriceSpecification", "priceCurrency": "USD", "unitText": "window installed (10+ window landlord package)" } } }
  </script>""",
        "related": [
            ("/blog/affordable-faux-wood-blinds-guide/", "Service guide · 6 min read", "Affordable <em>faux wood blinds</em>", "The product behind the rental spec.", "/assets/images/blog/affordable-faux-wood.webp", "Affordable faux wood blinds in a Tennessee kitchen"),
            ("/blog/affordable-blinds-nashville-tennessee/", "Local guide · 6 min read", "Affordable blinds <em>near me</em>", "Local SEO companion piece.", "/assets/images/blog/affordable-faux-wood.webp", "Affordable faux wood blinds in a Nashville-area kitchen"),
        ],
    },
    {
        "slug": "home-depot-lowes-blinds-installer-tennessee",
        "title_html": "Home Depot &amp; Lowes blinds <em>installer near me.</em>",
        "h1_plain": "Home Depot, Lowes & Costco Blinds Installer in Middle Tennessee",
        "meta_title": "Home Depot & Lowes Blinds Installer Near Me · Middle TN · Stately Shades",
        "meta_desc": "Searching for a Home Depot blinds installer or Lowes blinds installer near me in Tennessee? We install blinds from Home Depot, Lowes, Costco, Blinds.com, Select Blinds, Amazon, IKEA. Flat-rate, workmanship guarantee.",
        "eyebrow": "Local Service · Install Only · BYO Blinds",
        "section": "Local Service",
        "minutes": "6",
        "image": "/assets/images/blog/install-only-service.webp",
        "image_alt": "A professional installer mounting a blind purchased from Home Depot on a Tennessee window, boxes visible on a drop cloth",
        "caption": "Boxes from the home-improvement store, blind on the wall — install-only service across Middle Tennessee.",
        "keywords": "Home Depot blinds installer near me, Lowes blinds installer, Costco blinds install, Blinds.com installer, professional blind installer Tennessee, blind installation service Nashville, install only blinds Middle TN, BYO blinds installer, Select Blinds installer",
        "og_desc": "Professional installer for blinds bought at Home Depot, Lowes, Costco, Blinds.com — across Middle Tennessee.",
        "tw_desc": "Searched 'Home Depot blinds installer near me'? We install any-brand blinds across Middle TN. Flat-rate.",
        "breadcrumb_name": "Home Depot & Lowes Blinds Installer · Middle TN",
        "body": """
      <p>If you've been searching <em>"Home Depot blinds installer near me,"</em> <em>"Lowes blinds installer Tennessee,"</em> <em>"Costco blinds install,"</em> or <em>"who installs Blinds.com window treatments,"</em> the answer is the same regardless of which retailer you used: <strong>Stately Shades does install-only service across Middle Tennessee for any brand, any retailer, any product</strong>. This guide covers the specifics of what we do, what we charge, and what to expect.</p>

      <h2>Retailers we install from most often</h2>
      <p>In rough order of how many we install per month:</p>
      <ol>
        <li><strong>Home Depot</strong> — Hampton Bay, Bali, Custom Blinds, Levolor in-store products. The most common retailer we install for.</li>
        <li><strong>Lowes</strong> — Levolor, Custom Size Now, Allen + Roth, Bali. Their custom-sized line is excellent quality.</li>
        <li><strong>Blinds.com</strong> — and sister sites (JustBlinds, BlindsOnline). Solid quality, dimensions usually accurate.</li>
        <li><strong>Costco</strong> — both warehouse and Costco.com. Best-in-category value at the price point.</li>
        <li><strong>Amazon</strong> — Chicology, Yoolax, Loomgaal, generic faux wood, motorized SmartWings. Quality varies; we'll install what's structurally sound.</li>
        <li><strong>Select Blinds</strong> — strong cellular and roller lines.</li>
        <li><strong>IKEA</strong> — FYRTUR (motorized blackout roller), KADRILJ, TIBBLE. We've installed dozens of FYRTURs.</li>
        <li><strong>Wayfair</strong> — Bali, Achim, custom no-name brands.</li>
        <li><strong>Bali Direct, Levolor Direct</strong> — manufacturer-direct purchases.</li>
        <li><strong>Builder leftovers</strong> from a previous project (5+ years old still install fine if sealed).</li>
      </ol>

      <h2>What it costs in Middle Tennessee in 2026</h2>
      <p>Flat-rate per window, no surprises:</p>
      <ul>
        <li><strong>Faux wood and aluminum horizontal blinds</strong>: $45–$65/window</li>
        <li><strong>Real-wood blinds</strong>: $55–$75/window</li>
        <li><strong>Cellular, roller, and Roman shades</strong>: $55–$75/window</li>
        <li><strong>Solar / sun shades</strong>: $55–$75/window</li>
        <li><strong>Vertical blinds and panel-track for sliding doors</strong>: $95–$160/opening</li>
        <li><strong>Plantation shutters</strong> (per panel hung &amp; tensioned): $65–$140/window</li>
        <li><strong>Motorized shades with hub pairing &amp; programming</strong>: $95–$180/shade</li>
        <li><strong>French door, arch, skylight, specialty shapes</strong>: quoted on site</li>
        <li><strong>Service-call minimum</strong> (3 or fewer windows): $185</li>
      </ul>
      <p>A typical 8-window install-only project across Middle Tennessee lands between <strong>$360 and $720</strong>, with parts coming from your own boxes.</p>

      <p class="pull">You did the research. You picked the product. Saturday belongs to you, not to a stepladder.</p>

      <h2>Cities we serve for install-only</h2>
      <p>Our 90-mile service radius from Gallatin covers most of Middle Tennessee and into southern Kentucky:</p>
      <ul>
        <li><strong>Nashville</strong> and every neighborhood — Green Hills, East Nashville, Belle Meade, the Gulch, Antioch, Bellevue, Donelson, Hermitage, Madison.</li>
        <li><strong>Hendersonville, Gallatin, Goodlettsville, Springfield</strong> — Sumner and Robertson counties.</li>
        <li><strong>Franklin, Brentwood, Spring Hill, Cool Springs</strong> — Williamson County.</li>
        <li><strong>Murfreesboro, Smyrna, La Vergne</strong> — Rutherford County.</li>
        <li><strong>Mt. Juliet, Lebanon</strong> — Wilson County.</li>
        <li><strong>Clarksville, Springfield, Cookeville</strong> — outer ring.</li>
        <li><strong>Bowling Green, KY</strong> and the bordering Kentucky counties.</li>
      </ul>

      <h2>What our install includes</h2>
      <ol>
        <li><strong>Unbox</strong> every blind and check against the packing slip for damage.</li>
        <li><strong>Verify dimensions</strong> against your openings before we drill.</li>
        <li><strong>Mount level</strong> — the single most common DIY mistake, easily worth the install fee on its own.</li>
        <li><strong>Hang the bottom rail symmetrically</strong> and tension the lift cord properly.</li>
        <li><strong>Program motors</strong> — pair with your hub, set up/down limits, test scenes, walk you through the app.</li>
        <li><strong>Demo the mechanism</strong> in person — lift, tilt, batteries, troubleshooting.</li>
        <li><strong>Haul away packaging</strong> — cardboard, plastic, and the foam your hands don't want to deal with.</li>
        <li><strong>Workmanship guarantee</strong>: if a bracket pulls out, the headrail levels itself out within 90 days, or a motor we programmed loses its limits, we come back on us.</li>
      </ol>

      <div class="callout">
        <h3>The Home Depot Levolor scenario we see weekly</h3>
        <p>The single most common install-only request we get: a 6–10 window Home Depot Levolor faux wood order, arrived in boxes 2–4 weeks ago, customer didn't realize how much work the install would be. Typical project total: <strong>$310–$580 installed</strong>, scheduled within 5 business days, completed in a single 3–4 hour visit.</p>
      </div>

      <h2>When it makes sense to use install-only vs. buy through us</h2>
      <ul>
        <li><strong>You already ordered.</strong> Obvious — install-only.</li>
        <li><strong>You want a specific online product</strong> we don't stock (a Smart Wings FYRTUR alternative, a niche cellular cell count, an IKEA-only color). Install-only.</li>
        <li><strong>You're price-shopping at the very bottom.</strong> A $40 Home Depot stock blind + our $50 install = $90 installed, which is comparable to our $89 custom. Honest math says we usually come out within $5 either direction. We'll tell you on the visit which way to go.</li>
        <li><strong>You want custom dimensions, a free measure, and a quote from a pro before you spend.</strong> Buy through us — the consultation is free.</li>
      </ul>

      <h2>The single most common DIY mistake</h2>
      <p>It's the same on every retailer: <strong>ordering the wrong size</strong>. Lowes and Home Depot both default to a "factory deduction" for inside-mount and a "no deduction" for outside-mount, and getting that wrong is a $100 mistake. If you'd like us to measure before you order, we'll do that on the consultation visit for the cost of a service call — applied toward the eventual install fee.</p>

      <h2>How to schedule</h2>
      <p>Photograph the unopened blind boxes (or the inside flap with dimensions) and the windows they'll go on. Text the photos to <strong>629-298-8241</strong> with your address. We quote from the photos within a few hours and book the install within the week. <a href="/#contact">Or use the contact form</a>.</p>
        """,
        "extra_schema": """  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "Who installs Home Depot blinds in Tennessee?", "acceptedAnswer": { "@type": "Answer", "text": "Stately Shades installs Home Depot blinds (Hampton Bay, Bali, Custom Blinds, Levolor) across the entire Middle Tennessee 90-mile radius from Gallatin — including Nashville, Hendersonville, Franklin, Brentwood, Murfreesboro, Mt. Juliet, Lebanon, Spring Hill, Cookeville, Clarksville, and into Bowling Green, Kentucky. Flat-rate per window with a workmanship guarantee." } },
    { "@type": "Question", "name": "Does Home Depot install blinds they sell?", "acceptedAnswer": { "@type": "Answer", "text": "Home Depot does offer an install service via third-party contractors in some regions, but pricing varies and scheduling can be slow. Many Tennessee customers prefer to hire an independent installer like Stately Shades — flat-rate pricing, faster scheduling (usually within a week), and direct accountability with the installer." } },
    { "@type": "Question", "name": "How much does Lowes blinds installation cost?", "acceptedAnswer": { "@type": "Answer", "text": "Lowes installation services (where available) run roughly $40 to $70 per window in Tennessee, plus the cost of the blind. Stately Shades install-only service runs $45 to $85 per window for standard blinds and includes a workmanship guarantee — typically comparable or slightly lower total cost with faster scheduling." } },
    { "@type": "Question", "name": "Who installs Blinds.com blinds in Nashville?", "acceptedAnswer": { "@type": "Answer", "text": "Stately Shades installs Blinds.com window treatments throughout the Nashville metro and Middle Tennessee. Same flat-rate pricing ($45 to $85 per window standard, $65 to $140 per plantation shutter panel), same workmanship guarantee." } },
    { "@type": "Question", "name": "Do you install Costco blinds?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Costco blinds — both in-warehouse and Costco.com purchases — are a regular install-only product for us. Same per-window pricing and workmanship guarantee as any other retailer." } },
    { "@type": "Question", "name": "Can you install IKEA FYRTUR motorized blinds?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. IKEA FYRTUR (and KADRILJ, TIBBLE) motorized blinds are among the most-installed motorized products in our install-only catalogue. We mount, pair with the gateway, set up Apple Home / Google Home / Alexa integration, and demo the mechanism. Typical cost $95 to $180 per shade with hub pairing included." } }
  ]}
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "SpeakableSpecification", "cssSelector": [".article-hero h1", ".prose p:first-of-type", ".callout p"] }
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "Service", "@id": "https://statelyshades.com/blog/home-depot-lowes-blinds-installer-tennessee/#service", "name": "Home Depot, Lowes, Costco & Blinds.com Installer — Middle Tennessee", "serviceType": "Bring-Your-Own-Blinds Professional Installation", "provider": { "@type": "LocalBusiness", "name": "Stately Shades", "telephone": "+1-629-298-8241", "address": { "@type": "PostalAddress", "addressLocality": "Gallatin", "addressRegion": "TN", "addressCountry": "US" } }, "areaServed": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": 36.3881, "longitude": -86.4467 }, "geoRadius": "144841" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "45", "highPrice": "180", "priceSpecification": { "@type": "UnitPriceSpecification", "priceCurrency": "USD", "unitText": "window installed" } } }
  </script>""",
        "related": [
            ("/blog/install-only-blinds-service-guide/", "Service guide · 6 min read", "Install only · <em>BYO blinds</em>", "The deeper install-only walkthrough.", "/assets/images/blog/install-only-service.webp", "Installing a blind on a Tennessee window casing"),
            ("/blog/cost-to-install-blinds-professionally/", "Pricing · 6 min read", "Cost to install blinds <em>professionally</em>", "2026 pricing breakdown.", "/assets/images/blog/professional-installer-detail.webp", "Professional installer hands and tools"),
        ],
    },
    {
        "slug": "cost-to-install-blinds-professionally",
        "title_html": "Cost to install blinds <em>professionally.</em>",
        "h1_plain": "What Does It Cost to Install Blinds Professionally? (2026 Pricing)",
        "meta_title": "Cost to Install Blinds Professionally · 2026 Pricing Guide · Stately Shades",
        "meta_desc": "Real 2026 pricing for professional blind installation in Tennessee — per-window cost by type, plantation shutter install pricing, motorized programming fees, and what's included. Flat-rate, no surprises.",
        "eyebrow": "Pricing · Professional Installation",
        "section": "Pricing",
        "minutes": "6",
        "image": "/assets/images/blog/professional-installer-detail.webp",
        "image_alt": "Close-up of a professional installer's hands threading a hidden lift cord through a custom blind headrail with brass tools",
        "caption": "Professional install — measured, level, demoed, guaranteed.",
        "keywords": "cost to install blinds, professional blind installation cost, blind installation price per window, how much does it cost to install blinds, plantation shutter installation cost, motorized blind programming fee, Tennessee blind installer pricing",
        "og_desc": "Real 2026 pricing for professional blind installation in Tennessee — per-window, per-type, no surprises.",
        "tw_desc": "Professional blind install pricing in 2026: $45-$180/window depending on type. Full breakdown.",
        "breadcrumb_name": "Cost to Install Blinds Professionally",
        "body": """
      <p>The single most-asked pricing question we get on the phone: <em>what does it cost to have blinds professionally installed?</em> The answer depends on the type of blind, the window count, the complexity of the install, and a few specialty factors that don't show up in any online calculator. This is the real 2026 pricing across Middle Tennessee, with no upsell built in.</p>

      <h2>The short answer</h2>
      <p>Professional blind installation in Middle Tennessee in 2026 typically runs <strong>$45 to $180 per window installed</strong>, depending on what's going on the wall. The exact range:</p>
      <ul>
        <li><strong>Standard horizontal blinds</strong> (faux wood, real wood, aluminum mini): <strong>$45–$75/window</strong></li>
        <li><strong>Cellular &amp; honeycomb shades</strong>: <strong>$55–$75/window</strong></li>
        <li><strong>Roller, solar, and Roman shades</strong>: <strong>$55–$75/window</strong></li>
        <li><strong>Vertical blinds &amp; panel-track</strong> (for sliding doors): <strong>$95–$160/opening</strong></li>
        <li><strong>Plantation shutters</strong> (per panel hung &amp; tensioned): <strong>$65–$140/window</strong></li>
        <li><strong>Motorized shades</strong> with hub pairing &amp; programming: <strong>$95–$180/shade</strong></li>
        <li><strong>French-door &amp; specialty shapes</strong>: $85–$220/opening</li>
        <li><strong>Service-call minimum</strong> (3 or fewer windows): <strong>$185 flat</strong></li>
      </ul>

      <h2>What "professionally installed" actually includes</h2>
      <p>Cheap "installation services" charge per-blind and skip steps. A real professional install includes all of the following:</p>
      <ol>
        <li><strong>Unbox &amp; QC</strong> — open every package, check against the packing slip for damage or wrong-size deliveries.</li>
        <li><strong>Verify dimensions</strong> against your openings <em>before</em> drilling. Catching a too-narrow blind before mounting saves a $100 return.</li>
        <li><strong>Drop cloths down</strong>, walls protected, vacuum on hand for drywall dust.</li>
        <li><strong>Level mounting</strong> — bracket placement at the correct height, fascia or headrail perfectly horizontal on the level.</li>
        <li><strong>Bottom rail symmetry</strong> — every blind in a room should land at the same height when fully closed.</li>
        <li><strong>Operate &amp; demo</strong> — every blind raised, lowered, tilted with you watching. Hand you the wand or remote and walk through replacement (batteries, etc.).</li>
        <li><strong>Haul packaging</strong> — cardboard, plastic, foam wedges.</li>
        <li><strong>Workmanship guarantee</strong> — return if anything fails on the install side within 90 days. Free.</li>
      </ol>

      <h2>Where pricing scales</h2>

      <h3>Number of windows</h3>
      <p>Per-window pricing comes down at scale. 1–3 windows triggers our service-call minimum ($185). 4–8 windows runs the standard per-window rate. 9+ windows or a whole-house package gets a bulk discount — typically 10–20% off the per-window rate.</p>

      <h3>Window type</h3>
      <ul>
        <li><strong>Standard double-hung or casement windows</strong> with normal trim: bottom of the range.</li>
        <li><strong>Deep sills, casing returns, decorative trim</strong>: middle of the range — more time to mount cleanly.</li>
        <li><strong>French doors, sliders, transoms, skylights, arches</strong>: top of the range or quoted separately.</li>
      </ul>

      <h3>Product type</h3>
      <p>Plantation shutters take longer than horizontal blinds because each panel needs to be tensioned and aligned. Motorized shades cost more because programming the hub + setting limits + walking you through the app adds 20–40 minutes per shade.</p>

      <h3>Specialty work</h3>
      <ul>
        <li><strong>Outside-mount on plaster or stone:</strong> +$15–$30/window (anchors needed).</li>
        <li><strong>Atrium/vaulted/stairwell mounting</strong> requiring a 12'+ ladder or scaffolding: $50–$150 extra per window.</li>
        <li><strong>Out-of-square frames</strong> requiring shims and re-templated brackets: case-by-case.</li>
        <li><strong>Existing blind removal</strong> (we take down what's there): $10–$20/window.</li>
      </ul>

      <p class="pull">A flat $89 quote with the trip fee added in writing beats a $45 quote that becomes $145 by the time the installer leaves.</p>

      <h2>Real example projects</h2>

      <h3>Example 1 · 8 faux wood blinds in a Hendersonville bungalow</h3>
      <ul>
        <li>8 windows × $55/window faux wood install = <strong>$440</strong></li>
        <li>1 existing-blind removal × $15 = $15</li>
        <li><strong>Total: $455 installed.</strong> About a 3-hour visit.</li>
      </ul>

      <h3>Example 2 · 12 plantation shutter panels in a Franklin colonial</h3>
      <ul>
        <li>12 panels × $95/window plantation = <strong>$1,140</strong></li>
        <li>2 specialty bay-window panels × $30 extra = $60</li>
        <li><strong>Total: $1,200 installed.</strong> A full-day visit.</li>
      </ul>

      <h3>Example 3 · 6 motorized cellular shades in a Brentwood primary suite</h3>
      <ul>
        <li>6 shades × $130/window motorized w/ programming = <strong>$780</strong></li>
        <li>Hub pairing + Alexa/Google scenes: $0 (included)</li>
        <li><strong>Total: $780 installed.</strong> About 4 hours.</li>
      </ul>

      <h2>What you'll spend if you DIY</h2>
      <p>Be honest about the trade-off. A typical homeowner with no install experience spends roughly 45–90 minutes per blind on a DIY install, plus the cost of a step ladder and a stud finder if they don't have one, plus the risk of getting the brackets at the wrong height and re-drilling. Average DIY 8-blind job: <strong>6–12 hours of weekend, ~$30 in supplies, and a 1-in-4 chance of needing to call us afterward anyway.</strong> Math worth considering.</p>

      <div class="callout">
        <h3>Our service-call minimum, explained</h3>
        <p>For 1–3 windows, we charge a <strong>$185 service-call minimum</strong> instead of per-window pricing. This covers the truck, the drive, the measure, the install of up to 3 standard blinds, and the demo. It's the only way the math works on small jobs across a 90-mile radius. For 4+ windows the per-window rate is always cheaper.</p>
      </div>

      <h2>How to get a written quote</h2>
      <p>Three ways:</p>
      <ol>
        <li><strong>Text photos to 629-298-8241</strong> — windows + product boxes if you have them. Most jobs we quote within an hour.</li>
        <li><strong>Book a free consultation</strong> via <a href="/#contact">the contact form</a>. We come measure, sample, and quote on the same visit.</li>
        <li><strong>Call</strong> <a href="tel:+16292988241">629-298-8241</a> and tell us the window count + product type. Phone quotes possible on straightforward jobs.</li>
      </ol>

      <p>For the broader buyer's guide on what we install (any retailer's products), see <a href="/blog/install-only-blinds-service-guide/">the install-only service guide</a>. For local SEO/service-area coverage, see <a href="/blog/home-depot-lowes-blinds-installer-tennessee/">our Home Depot, Lowes & Costco installer guide</a>.</p>
        """,
        "extra_schema": """  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    { "@type": "Question", "name": "How much does it cost to install blinds professionally?", "acceptedAnswer": { "@type": "Answer", "text": "Professional blind installation in Middle Tennessee in 2026 runs $45 to $75 per window for standard horizontal blinds, $55 to $75 per window for cellular and roller shades, $65 to $140 per panel for plantation shutters, and $95 to $180 per shade for motorized treatments with programming. A typical 8-window project lands between $360 and $720 installed." } },
    { "@type": "Question", "name": "Is it worth paying to have blinds installed?", "acceptedAnswer": { "@type": "Answer", "text": "For most homeowners, yes. A typical 8-window DIY install takes 6 to 12 hours over a weekend, requires a step ladder and stud finder, and has roughly a 1-in-4 chance of needing professional follow-up. Professional install runs $360 to $720 for the same job, completed in a single 3 to 4 hour visit with a workmanship guarantee." } },
    { "@type": "Question", "name": "What is included in professional blind installation?", "acceptedAnswer": { "@type": "Answer", "text": "A real professional install includes unboxing and QC, verifying dimensions against openings before drilling, drop cloths for drywall dust, level mounting, bottom-rail symmetry across the room, demo of every blind with the homeowner watching, packaging haul-away, and a workmanship guarantee on the install for 90 days." } },
    { "@type": "Question", "name": "Does plantation shutter install cost more than blind install?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Plantation shutter install runs $65 to $140 per panel in Middle Tennessee because each panel must be hinged, tensioned, and aligned individually. Standard horizontal blind install runs $45 to $75 per window. A 12-panel shutter project typically takes a full day; a 12-blind project takes 3 to 4 hours." } },
    { "@type": "Question", "name": "How much extra does motorized blind installation cost?", "acceptedAnswer": { "@type": "Answer", "text": "Motorized shade installation in Middle Tennessee runs $95 to $180 per shade in 2026. The premium over standard install covers hub pairing (PowerView, Somfy TaHoma, Lutron), setting up and down limits, scene programming, and walking the homeowner through the mobile app and voice control with Alexa, Google Home, or Apple HomeKit." } }
  ]}
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "SpeakableSpecification", "cssSelector": [".article-hero h1", ".prose p:first-of-type", ".callout p"] }
  </script>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "Service", "@id": "https://statelyshades.com/blog/cost-to-install-blinds-professionally/#service", "name": "Professional Blind Installation Service — Middle Tennessee", "serviceType": "Window Treatment Installation", "provider": { "@type": "LocalBusiness", "name": "Stately Shades", "telephone": "+1-629-298-8241", "address": { "@type": "PostalAddress", "addressLocality": "Gallatin", "addressRegion": "TN", "addressCountry": "US" } }, "areaServed": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": 36.3881, "longitude": -86.4467 }, "geoRadius": "144841" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "45", "highPrice": "180", "priceSpecification": { "@type": "UnitPriceSpecification", "priceCurrency": "USD", "unitText": "window installed" } } }
  </script>""",
        "related": [
            ("/blog/home-depot-lowes-blinds-installer-tennessee/", "Local guide · 6 min read", "Home Depot &amp; Lowes <em>installer near me</em>", "Retailer-specific install service.", "/assets/images/blog/install-only-service.webp", "Installing a blind purchased from Home Depot"),
            ("/blog/install-only-blinds-service-guide/", "Service guide · 6 min read", "Install only · <em>BYO blinds</em>", "The full install-only walkthrough.", "/assets/images/blog/install-only-service.webp", "Installing a blind on a Tennessee window casing"),
        ],
    },
    {
        "slug": "blind-shutter-shade-repair-guide",
        "title_html": "Blind, shutter &amp; <em>shade repair.</em>",
        "h1_plain": "Blind, Shutter & Shade Repair: A Complete Guide",
        "meta_title": "Blind, Shutter & Shade Repair: A Complete Guide · Stately Shades",
        "meta_desc": "Repair vs. replace decision guide for broken blinds, shutters, and shades — any brand. Tilt rods, lift cords, motor service, PowerView repair, blackout liner replacement. Middle Tennessee.",
        "eyebrow": "Service Guide · Repair",
        "section": "Service Guide",
        "minutes": "5",
        "image": "/assets/images/blog/repair-service.webp",
        "image_alt": "A craftsman restringing a hardwood plantation shutter louver mechanism on a walnut workbench",
        "caption": "Restringing a hardwood shutter — most repairs take less than an hour on site.",
        "keywords": "blind repair, shutter repair, shade repair, blind restringing, PowerView repair, motor service, lift cord, tilt rod replacement, blind repair near me",
        "og_desc": "Repair vs. replace decision guide for broken blinds, shutters, and shades — any brand, anywhere in Middle Tennessee.",
        "tw_desc": "Blind repair near me? Here's the decision tree — what's worth fixing and what isn't.",
        "breadcrumb_name": "Blind, Shutter & Shade Repair Guide",
        "body": """
      <p>Most broken blinds aren't replaced — they're repaired. A snapped lift cord, a stuck tilt rod, a frayed cord, a PowerView motor that won't respond, a blackout liner that's lost its grip after eight years of sun. Almost all of these are fixable, often in under an hour, often for a fraction of replacement cost. Here is the complete guide to what we repair, what's worth repairing, and what isn't.</p>

      <h2>What we repair</h2>
      <p>Anything we (or anyone else) installed — and any brand:</p>
      <ul>
        <li><strong>Hunter Douglas</strong> — all lines, all eras. PowerView, Duette, Silhouette, Pirouette, Luminette, Provenance, Designer Roller, Vignette, NewStyle, Heritage.</li>
        <li><strong>Norman</strong> — Heritance shutters, Woodlore composite, Honeycomb cellular, all roller lines.</li>
        <li><strong>Somfy motors</strong> — any installation, any year.</li>
        <li><strong>Graber, Levolor, Bali, Lutron, Comfortex</strong> — full coverage.</li>
        <li><strong>Builder-grade and big-box generics</strong> — yes, even these. We carry universal parts.</li>
        <li><strong>Custom workroom drapery</strong> — re-pleating, re-lining, re-rodding.</li>
      </ul>

      <h2>Common repairs</h2>
      <h3>Lift cord replacement</h3>
      <p>The single most common repair. A frayed or snapped lift cord on a Roman or cellular shade. Done in 20–30 minutes on site. Restringing kits exist for every major manufacturer, and we keep them on the truck.</p>

      <h3>Tilt rod and tilt mechanism</h3>
      <p>For wood blinds and plantation shutters. The vertical rod that tilts louvers cracks or the internal mechanism strips. Replaceable on every Hunter Douglas and Norman product we install. Plantation shutters get their hinge/tension reset at the same time.</p>

      <h3>Stuck or dead motor</h3>
      <p>For motorized shades. PowerView Gen 1 and Gen 2 motors are now 10+ years old in some installs and reaching end of life. Gen 3 motors retrofit directly into Gen 1/2 brackets in most cases. Somfy motors are field-serviceable; we replace the motor without changing the shade.</p>

      <h3>Battery replacement / recharge</h3>
      <p>For battery-powered motorized shades. Batteries last 12–36 months. Replacement is plug-and-play.</p>

      <h3>Broken slat replacement</h3>
      <p>For real-wood and faux-wood blinds. Individual slats can be swapped in many cases. For older blinds where slat color is no longer manufactured, we sometimes pull a matching slat from the bottom or top of the existing blind.</p>

      <h3>Blackout liner re-attachment</h3>
      <p>For cellular and Roman shades. The blackout liner separates from the shade fabric after 6–10 years of UV exposure. Re-attached with manufacturer-spec adhesive.</p>

      <h3>Plantation shutter restringing</h3>
      <p>The hidden tilt cords inside a plantation shutter stile occasionally need re-tensioning or full replacement. A 30–45 minute on-site job per panel.</p>

      <h3>Cord shroud (child-safety) retrofit</h3>
      <p>For older corded blinds in homes with young children. We add cord cleats, cord shrouds, or convert to cordless lift where possible.</p>

      <h2>Repair vs. replace — the decision tree</h2>

      <p>The honest framework we walk every client through:</p>

      <h3>Repair if:</h3>
      <ul>
        <li>The blind is under 10 years old and structurally sound.</li>
        <li>The fabric/wood is in good condition.</li>
        <li>The repair is mechanical (cord, motor, hinge, tilt rod) rather than the shade material itself.</li>
        <li>It's a premium product — Hunter Douglas, Norman, Hunter Douglas Provenance, motorized PowerView — that warrants the labor.</li>
        <li>Replacement would require re-ordering custom dimensions you no longer have records of.</li>
      </ul>

      <h3>Replace if:</h3>
      <ul>
        <li>The fabric is faded, stained, or torn beyond what cleaning will recover.</li>
        <li>The product is 15+ years old and obsolete (parts no longer manufactured).</li>
        <li>The whole room is being redecorated and the existing shade is the wrong color/style.</li>
        <li>The repair cost approaches 60%+ of replacement cost.</li>
        <li>The product was builder-grade and you've been waiting for an excuse anyway.</li>
      </ul>

      <p class="pull">A $40 lift cord almost always beats a $400 shade. Repair first, replace when the math doesn't work.</p>

      <h2>What it costs</h2>
      <ul>
        <li><strong>Service call (covers the visit + first 30 min of work):</strong> $95 within 30 miles, $140 within 60 miles, $185 within 90 miles</li>
        <li><strong>Lift cord restring:</strong> $35–$75 per shade</li>
        <li><strong>Tilt rod / mechanism replacement:</strong> $45–$120 per shade</li>
        <li><strong>PowerView Gen 3 motor (retrofit Gen 1/Gen 2):</strong> $180–$340 per shade installed</li>
        <li><strong>Battery wand replacement:</strong> $80–$140 per shade</li>
        <li><strong>Wood blind slat replacement:</strong> $15–$40 per slat installed</li>
        <li><strong>Blackout liner re-attachment:</strong> $40–$90 per shade</li>
        <li><strong>Plantation shutter restring per panel:</strong> $65–$120</li>
      </ul>

      <p>The service call fee is applied toward the repair cost — so if you call us out for a $95 service call and the repair is a $35 cord restring, the total is $95, not $130. We're not nickel-and-diming service calls.</p>

      <h2>How to schedule a repair</h2>
      <p>Take a photo of the broken shade in context (the whole window with the shade visible) plus a close-up of the broken part. Text both photos to <strong>629-298-8241</strong> with a sentence describing the issue. We can usually quote the repair from the photos before we visit and bring the right parts on the first trip.</p>

      <h2>Service area</h2>
      <p>We repair across the same 90-mile radius we install in — Gallatin, Nashville, Hendersonville, Franklin, Brentwood, Murfreesboro, Mt. Juliet, Lebanon, Goodlettsville, Cookeville, Clarksville, Springfield, Bowling Green KY, and every town in between.</p>

      <p>For a repair quote or to schedule a visit, call or text <a href="tel:+16292988241">629-298-8241</a>, email <a href="mailto:hello@statelyshades.com">hello@statelyshades.com</a>, or <a href="/#contact">use the contact form</a>.</p>
        """,
        "related": [
            ("/blog/plantation-wood-shutters-guide/", "Product guide · 8 min read", "Plantation &amp; <em>wood shutters</em>", "What we repair and what we install.", "/assets/images/blog/plantation-shutters.webp", "Plantation shutters in a Tennessee dining room"),
            ("/blog/motorized-smart-shades-guide/", "Product guide · 7 min read", "Motorized &amp; <em>smart shades</em>", "Motor service and PowerView retrofits.", "/assets/images/blog/motorized-shades.webp", "Motorized shades in a Tennessee great room"),
        ],
    },
]

# ------------ Template ----------------------------------------------------

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{meta_title}</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="canonical" href="https://statelyshades.com/blog/{slug}/" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#14110D" />

  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://statelyshades.com/blog/{slug}/" />
  <meta property="og:title" content="{h1_plain}" />
  <meta property="og:description" content="{og_desc}" />
  <meta property="og:image" content="https://statelyshades.com{image}" />
  <meta property="og:image:alt" content="{image_alt}" />
  <meta property="og:site_name" content="Stately Shades" />
  <meta property="og:locale" content="en_US" />
  <meta property="article:published_time" content="{date}" />
  <meta property="article:section" content="{section}" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{h1_plain}" />
  <meta name="twitter:description" content="{tw_desc}" />
  <meta name="twitter:image" content="https://statelyshades.com{image}" />

  <link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg" />
  <link rel="icon" type="image/png" href="/assets/images/logo-v4.png" />
  <link rel="apple-touch-icon" href="/assets/images/logo-v4.png" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=DM+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="/styles.css?v={version}" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "@id": "https://statelyshades.com/blog/{slug}/#article",
    "mainEntityOfPage": "https://statelyshades.com/blog/{slug}/",
    "url": "https://statelyshades.com/blog/{slug}/",
    "headline": "{h1_plain}",
    "description": "{meta_desc}",
    "image": {{ "@type": "ImageObject", "url": "https://statelyshades.com{image}", "width": 1024, "height": 1024 }},
    "datePublished": "{date}",
    "dateModified": "{date}",
    "inLanguage": "en-US",
    "author": {{ "@type": "Organization", "name": "Stately Shades", "url": "https://statelyshades.com/" }},
    "publisher": {{ "@type": "Organization", "name": "Stately Shades", "url": "https://statelyshades.com/", "logo": {{ "@type": "ImageObject", "url": "https://statelyshades.com/assets/images/logo.png" }} }},
    "articleSection": "{section}",
    "keywords": "{keywords}"
  }}
  </script>
  <script type="application/ld+json">
  {{ "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://statelyshades.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Journal", "item": "https://statelyshades.com/blog/" }},
    {{ "@type": "ListItem", "position": 3, "name": "{breadcrumb_name}", "item": "https://statelyshades.com/blog/{slug}/" }}
  ]}}
  </script>
{extra_schema}
</head>
<body>

  <a class="skip-link" href="#main">Skip to content</a>

  <header class="nav" id="nav">
    <div class="container nav__inner">
      <a class="nav__brand" href="/" aria-label="Stately Shades home">
        <span class="nav__monogram" aria-hidden="true">S<span>S</span></span>
        <span class="nav__lockup">
          <span class="nav__wordmark">STATELY SHADES</span>
          <span class="nav__rule" aria-hidden="true"></span>
          <span class="nav__tagline">Blinds, Shutters &amp; Shades</span>
        </span>
      </a>
      <nav class="nav__links" aria-label="Primary">
        <a href="/#products">Products</a>
        <a href="/#services">Services</a>
        <a href="/#process">Process</a>
        <a href="/blog/">Journal</a>
        <a href="/#service-area">Service Area</a>
        <a href="/#contact" class="nav__cta"><span>Free Consultation</span></a>
      </nav>
      <button class="nav__toggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>

  <main id="main">

    <section class="article-hero">
      <div class="container article-hero__inner">
        <a class="article-hero__back" href="/blog/">The Journal</a>
        <span class="eyebrow">{eyebrow}</span>
        <h1>{title_html}</h1>
        <p class="article-hero__meta">
          <time datetime="{date}">{date_pretty}</time>
          <span>·</span>
          <span>{minutes} min read</span>
        </p>
      </div>
    </section>

    <figure class="article-figure">
      <img src="{image}" alt="{image_alt}" />
      <figcaption>{caption}</figcaption>
    </figure>

    <article class="prose">
{body}
    </article>

    <section class="article-cta">
      <div class="article-cta__inner">
        <span class="eyebrow">Free Consultation</span>
        <h2>Bring the showroom <em>to your window.</em></h2>
        <p>We measure, sample, and quote on the same visit. No pressure, no fee, every product line on hand.</p>
        <a href="/#contact" class="btn">Book your visit <span class="arrow" aria-hidden="true"></span></a>
      </div>
    </section>

    <section class="related">
      <div class="container">
        <div class="related__head">
          <span class="eyebrow">Keep Reading</span>
          <h2>More from the Journal</h2>
        </div>
        <div class="related__grid">
{related_cards}
        </div>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand">
        <a href="/" class="footer__lockup" aria-label="Stately Shades home">
          <span class="footer__monogram" aria-hidden="true">S<span>S</span></span>
          <span class="footer__words">
            <span class="footer__wordmark">STATELY SHADES</span>
            <span class="footer__rule" aria-hidden="true"></span>
            <span class="footer__tagline">Blinds, Shutters &amp; Shades</span>
          </span>
        </a>
        <p>Family-owned in Gallatin, Tennessee.</p>
      </div>
      <div class="footer__col">
        <span class="eyebrow eyebrow--light">Products</span>
        <ul>
          <li><a href="/#products">Plantation &amp; Wood Shutters</a></li>
          <li><a href="/#products">Motorized &amp; Smart Shades</a></li>
          <li><a href="/#products">Cellular / Honeycomb</a></li>
          <li><a href="/#products">Outdoor Shades &amp; Awnings</a></li>
          <li><a href="/#products">Zebra, Sheer &amp; Solar</a></li>
          <li><a href="/#products">Blinds &amp; Drapery</a></li>
          <li><a href="/#products">Repair &amp; Restoration</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <span class="eyebrow eyebrow--light">Company</span>
        <ul>
          <li><a href="/#about">About</a></li>
          <li><a href="/#process">Process</a></li>
          <li><a href="/blog/">Journal</a></li>
          <li><a href="/#faq">FAQ</a></li>
          <li><a href="/#service-area">Service Area</a></li>
          <li><a href="/#contact">Free Consultation</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <span class="eyebrow eyebrow--light">Contact</span>
        <ul>
          <li><a href="tel:+16292988241">629-298-8241</a></li>
          <li><a href="mailto:hello@statelyshades.com">hello@statelyshades.com</a></li>
          <li>Gallatin, Tennessee</li>
          <li>Mon–Sat · 8am–6pm</li>
        </ul>
      </div>
    </div>
    <div class="footer__legal container">
      <p>© <span id="year"></span> Stately Shades · All rights reserved</p>
      <p>Website Design by <a href="https://zorvalabs.com" target="_blank" rel="noopener">Zorva Labs</a></p>
    </div>
  </footer>

  <div class="mobile-cta">
    <a href="tel:+16292988241" class="mobile-cta__btn mobile-cta__btn--ghost">Call</a>
    <a href="/#contact" class="mobile-cta__btn mobile-cta__btn--primary">Free Consultation</a>
  </div>

  <script src="/script.js?v={version}" defer></script>
</body>
</html>
"""

RELATED_CARD = """          <a class="post-card" href="{url}">
            <div class="post-card__media"><img src="{img}" alt="{alt}" loading="lazy" /></div>
            <span class="post-card__meta">{meta}</span>
            <h2>{title}</h2>
            <p>{lede}</p>
          </a>"""


def render():
    pretty = "May 25, 2026"
    for p in POSTS:
        related_html = "\n".join(
            RELATED_CARD.format(url=r[0], meta=r[1], title=r[2], lede=r[3], img=r[4], alt=r[5])
            for r in p["related"]
        )
        out = TEMPLATE.format(
            slug=p["slug"],
            meta_title=p["meta_title"],
            meta_desc=p["meta_desc"],
            h1_plain=p["h1_plain"],
            og_desc=p["og_desc"],
            tw_desc=p["tw_desc"],
            image=p["image"],
            image_alt=p["image_alt"],
            caption=p["caption"],
            eyebrow=p["eyebrow"],
            section=p["section"],
            minutes=p["minutes"],
            keywords=p["keywords"],
            breadcrumb_name=p["breadcrumb_name"],
            title_html=p["title_html"],
            body=p["body"],
            related_cards=related_html,
            date=DATE,
            date_pretty=pretty,
            version=VERSION,
            extra_schema=p.get("extra_schema", ""),
        )
        out_path = BLOG / p["slug"] / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    render()
