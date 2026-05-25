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
VERSION = "blog2"

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
          <span class="nav__tagline">Custom Blinds, Shutters &amp; Shades</span>
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
            <span class="footer__tagline">Custom Blinds, Shutters &amp; Shades</span>
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
        )
        out_path = BLOG / p["slug"] / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    render()
