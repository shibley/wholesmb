#!/usr/bin/env python3
"""Generate the /acquire/*-valuation page family.

Net-new family: buyer-intent valuation pages ("how much is a laundromat worth").
Sits between the top-of-funnel `buy-a-*` playbooks and the generic
`how-to-value-a-business` guide, and monetizes the same affiliate CTAs.

Each niche carries its own prose so pages are not templated boilerplate.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "acquire")

NICHES = [
    {
        "slug": "laundromat-valuation",
        "plural": "laundromats",
        "noun": "Laundromat",
        "kw": "laundromat valuation",
        "title": "Laundromat Valuation (2026): What Multiple Do Laundromats Sell For?",
        "desc": "How much is a laundromat worth? Typical SDE multiples, the value drivers that move the number, red flags that cut it, and a worked valuation example.",
        "og_desc": "Typical laundromat SDE multiples, what raises and lowers the number, and a worked valuation example.",
        "intro": "Laundromats are priced off cash flow, not off the machines &mdash; but equipment is what decides whether that cash flow is believable and repeatable. A store doing $80,000 of owner earnings on twenty-year-old washers is not worth the same multiple as an identical store on five-year-old high-efficiency machines with a ten-year lease. This page covers the multiple range laundromats actually trade in, the specific factors that move a store up or down that range, and how to sanity-check an asking price before you spend money on diligence.",
        "buyer_metric": "SDE (seller's discretionary earnings)",
        "low": "2.0x",
        "high": "4.0x",
        "mid": "3x",
        "range_note": "Small, older, attended stores in secondary markets sit at the low end. Large, modern, card-operated stores with long leases and verifiable revenue reach the top of the range and occasionally beyond.",
        "drivers": [
            ("Equipment age and efficiency", "A fleet under about seven years old with high-efficiency washers means no near-term capital call and lower water and gas cost. That is worth real multiple, because the buyer is not underwriting a six-figure replacement in year two."),
            ("Remaining lease term", "Laundromats are location businesses with immovable plumbing and gas lines. Ten-plus years of remaining term (including options) supports a premium; under five years pushes buyers toward the bottom of the range or out of the deal entirely."),
            ("Verifiability of revenue", "Card systems and modern payment readers produce a transaction record. Coin-only stores force buyers to rely on water bills as a proxy, and uncertainty always gets priced as a discount."),
            ("Ancillary revenue mix", "Wash-dry-fold, commercial accounts, and vending diversify the income, but they are also more labor-dependent. Buyers typically value verified WDF revenue at a lower multiple than self-service turns."),
            ("Utility trend", "Rising water and sewer rates compress margin over the hold. Two or three years of utility bills showing a steep rate curve is a legitimate reason for a buyer to bid lower."),
        ],
        "discounts": [
            "Coin-only revenue with no independent water-bill corroboration.",
            "A lease with under five years remaining, or one that is not assignable.",
            "More than about a third of the machine fleet past useful life.",
            "A new competitor within the store's realistic catchment area.",
            "Owner-attended hours that were never expensed as wages in the P&amp;L.",
        ],
        "example_title": "Worked example: a $95,000 SDE laundromat",
        "example": "A store reports $310,000 of revenue and $95,000 of SDE after adding back the owner's $20,000 of unpaid attendant hours. At a mid-range 3x, that is roughly $285,000. Now adjust: the lease has six years left (neutral), the dryers average eleven years old and roughly $60,000 of replacement is due within three years (down), and the store is fully card-operated with three years of processor reports (up). A realistic bid lands nearer $240,000&ndash;$260,000, with the equipment gap negotiated as a price reduction or a seller-financed note rather than absorbed at close.",
        "faqs": [
            ("What multiple do laundromats sell for?", "Most laundromats trade at roughly 2x&ndash;4x SDE. The spread is driven mainly by equipment age, remaining lease term, and how verifiable the revenue is. Larger stores with modern card systems and long leases sit at the top; small coin-only stores with aging machines sit at the bottom."),
            ("Should a laundromat be valued on revenue or cash flow?", "Cash flow. Revenue multiples are sometimes quoted casually but they ignore the two things that decide laundromat profitability &mdash; utility cost and equipment condition. Price the SDE, then adjust for deferred capital expenditure."),
            ("Does the equipment get valued separately?", "Not usually as an addition. In a cash-flow-priced deal the equipment is already reflected in the earnings it produces, and its condition moves the multiple. Equipment is priced separately only in asset sales of stores with little or no provable cash flow."),
            ("How do I check an asking price quickly?", "Divide the asking price by the claimed SDE. If the implied multiple is above about 4x, the seller needs to point at something specific &mdash; a brand-new fleet, a very long lease, or documented commercial contracts &mdash; that justifies it."),
        ],
        "related": [
            ("/acquire/buy-a-laundromat", "Playbook", "How to Buy a Laundromat", "The full playbook: economics, financing, and what to inspect."),
            ("/acquire/businesses-for-sale-laundromat", "Listings", "Laundromats for Sale", "Where laundromats are listed and how to read a specific deal."),
            ("/acquire/car-wash-valuation", "Valuation", "Car Wash Valuation", "The other real-estate-anchored equipment business, priced."),
            ("/acquire/hvac-business-valuation", "Valuation", "HVAC Business Valuation", "Why service contracts command a higher multiple."),
        ],
    },
    {
        "slug": "hvac-business-valuation",
        "plural": "HVAC companies",
        "noun": "HVAC Business",
        "kw": "HVAC business valuation",
        "title": "HVAC Business Valuation (2026): Multiples, Value Drivers &amp; Example",
        "desc": "What is an HVAC company worth? Typical SDE and EBITDA multiples, why maintenance agreements raise the number, what drags it down, and a worked example.",
        "og_desc": "HVAC multiples, why service agreements move the number, and a worked valuation example.",
        "intro": "HVAC is one of the few home-service niches where two companies with identical revenue can be worth very different amounts. The difference is almost always the mix: recurring maintenance agreements and service calls are valued far more highly than new-construction installation work, because one is a contracted annuity and the other is a bid-by-bid business tied to the housing cycle. This page covers the multiple ranges HVAC companies actually trade at, why the revenue mix moves them, and how to price a specific company.",
        "buyer_metric": "SDE for owner-operated shops, EBITDA once earnings clear roughly $1M",
        "low": "2.5x",
        "high": "5.0x",
        "mid": "3.5x",
        "range_note": "Owner-operated shops under about $1M of earnings are priced on SDE in the 2.5x&ndash;4x band. Larger companies with a management layer are priced on EBITDA and reach 4x&ndash;6x or higher, which is why private-equity roll-ups have been active in the trade.",
        "drivers": [
            ("Maintenance agreement base", "A book of annual service agreements is the single most valuable asset in an HVAC company. It produces predictable revenue, feeds replacement leads, and survives ownership change. Buyers pay a premium for a large, current, transferable base."),
            ("Service and replacement vs. new construction", "Service and residential replacement work is high-margin and recurring. New-construction installation is cyclical, lower-margin, and dependent on builder relationships that may not transfer. A construction-heavy mix pulls the multiple down."),
            ("Technician retention", "The binding constraint in the trade is licensed labor. A crew that has been with the company for years, with the license held by someone staying through a transition, materially de-risks the deal."),
            ("Customer concentration", "A shop where one builder or one property-management group is a large share of revenue carries obvious risk. Diversified residential bases support higher multiples."),
            ("Owner dependence", "If the owner is the license holder, the top salesperson, and the dispatcher, the buyer is buying a job. Companies with a working general manager in place trade higher because there is a business left after the owner walks."),
        ],
        "discounts": [
            "Heavy new-construction concentration with thin backlog.",
            "The owner personally holds the license with no plan for transfer.",
            "A shrinking or lapsed maintenance-agreement base.",
            "Aging trucks and equipment with deferred replacement.",
            "Warranty and callback liabilities that are not reserved for.",
        ],
        "example_title": "Worked example: a $600,000 SDE HVAC company",
        "example": "A residential HVAC company reports $3.4M of revenue and $600,000 of SDE. Mix is roughly 60% service and replacement, 40% new construction, with 900 active maintenance agreements. At a mid-range 3.5x that is about $2.1M. Adjust up for the agreement base and diversified residential customers; adjust down because the owner is the license holder and intends to retire at close. A realistic outcome is a price near the mid-range with a meaningful portion structured as an earnout or seller note tied to agreement retention and a licensed-tech transition period.",
        "faqs": [
            ("What multiple do HVAC companies sell for?", "Owner-operated shops generally sell for about 2.5x&ndash;4x SDE. Larger companies with real management depth are valued on EBITDA and commonly reach 4x&ndash;6x, sometimes higher when a roll-up buyer is competing for them."),
            ("Why do maintenance agreements matter so much?", "They convert a bid-to-bid business into recurring revenue and a captive lead source for equipment replacement. Buyers underwrite them as an annuity, so a large, transferable, current agreement base is the clearest way to move an HVAC valuation up."),
            ("Is SDE or EBITDA the right metric?", "Use SDE when the owner works in the business and their compensation is discretionary. Use EBITDA once the company employs a real management layer and the owner's pay is a market-rate salary rather than the residual profit."),
            ("Does the truck fleet add to the price?", "Only marginally, and only when it is unusually new. In a cash-flow-priced deal a normal fleet is assumed to be included; an aged fleet is a deduction because the buyer inherits the replacement schedule."),
        ],
        "related": [
            ("/acquire/buy-a-hvac-business", "Playbook", "How to Buy an HVAC Business", "Economics, licensing, and what to inspect before you bid."),
            ("/acquire/buy-a-plumbing-business", "Playbook", "Buy a Plumbing Business", "The adjacent trade, with the same licensing dynamics."),
            ("/acquire/trucking-company-valuation", "Valuation", "Trucking Company Valuation", "An asset-heavy business priced very differently."),
            ("/acquire/how-to-value-a-business", "Guide", "How to Value a Business", "SDE, EBITDA, add-backs, and multiples explained."),
        ],
    },
    {
        "slug": "car-wash-valuation",
        "plural": "car washes",
        "noun": "Car Wash",
        "kw": "car wash valuation",
        "title": "Car Wash Valuation (2026): Multiples, Memberships &amp; Real Estate",
        "desc": "What is a car wash worth? Typical EBITDA multiples, how unlimited-wash memberships and owned real estate change the number, and a worked example.",
        "og_desc": "Car wash EBITDA multiples, the membership effect, real estate treatment, and a worked example.",
        "intro": "Car wash valuation is the one small-business category where the headline multiples you read about are usually wrong for the deal in front of you. The eye-catching numbers come from express-tunnel sites with large unlimited-membership bases, often sold with the real estate to institutional buyers. A self-serve bay or an in-bay automatic at a gas station is a different asset priced on different math. This page separates the formats, gives the multiple range for each, and explains how the property is handled.",
        "buyer_metric": "EBITDA, with real estate valued separately",
        "low": "3.5x",
        "high": "8.0x",
        "mid": "5x",
        "range_note": "Self-serve and single in-bay automatic sites generally trade around 3x&ndash;5x EBITDA. Express tunnels with a substantial recurring membership base command materially more, which is why the format matters more than the revenue figure.",
        "drivers": [
            ("Membership base", "Unlimited-wash plans convert weather-dependent walk-up volume into monthly recurring revenue. A site where memberships are a large share of revenue is underwritten much closer to a subscription business, and that is the main reason express tunnels outrun other formats."),
            ("Format", "Express tunnel, flex-serve, in-bay automatic, and self-serve bays have genuinely different throughput, labor models, and buyer pools. Compare a site only to others in its own format."),
            ("Real estate", "Most car wash sites include the land and building. Treat that as a separate line: value the operating business on its earnings after a market-rate rent, then add the property value. Blending the two is the most common way buyers mis-price these deals."),
            ("Equipment condition and water reclaim", "Tunnel equipment and reclaim systems are expensive and have finite life. A recent equipment refresh removes a near-term capital call; a tired tunnel is a direct deduction."),
            ("Site and traffic", "Car counts, ingress and egress, visibility, and stacking capacity constrain the ceiling on volume no matter how well the site is run. These do not change quickly, so buyers price them.")
        ],
        "discounts": [
            "Membership churn that the seller cannot document month by month.",
            "A tunnel or reclaim system near end of life.",
            "Leased land with a short remaining term.",
            "Revenue that swings hard with weather and has no membership floor.",
            "A competing express tunnel newly opened in the same trade area.",
        ],
        "example_title": "Worked example: an in-bay automatic doing $220,000 EBITDA",
        "example": "A single in-bay automatic site on owned land reports $700,000 of revenue and $220,000 of EBITDA before any rent charge. First, charge a market rent &mdash; say $60,000 &mdash; leaving $160,000 of operating EBITDA. At 4x for the format that is about $640,000 for the business. The land and building are appraised separately at roughly $850,000. Total consideration is therefore in the $1.4M&ndash;$1.5M range, and a buyer who instead applied a tunnel-style 7x to the unadjusted $220,000 would have offered materially over the asset's real worth.",
        "faqs": [
            ("What multiple does a car wash sell for?", "It depends on format. Self-serve bays and in-bay automatics generally sell for about 3x&ndash;5x EBITDA. Express tunnels with a meaningful unlimited-membership base sell for considerably more, and the largest sites attract institutional buyers at higher multiples again."),
            ("How is the real estate handled?", "Value them separately. Charge the operating business a market-rate rent, apply the multiple to the resulting EBITDA, then add the appraised property value. Applying a business multiple to combined earnings that include free occupancy overstates the price."),
            ("Do unlimited memberships really change the valuation?", "Yes, and it is the largest single factor within the express format. Recurring plan revenue smooths weather risk and raises the quality of earnings, so buyers pay a higher multiple for the same dollar of EBITDA."),
            ("What should I verify first on a car wash?", "Month-by-month membership counts and churn, the equipment service history, and the water and sewer bills. Those three together tell you whether the reported earnings are durable or a good-weather year."),
        ],
        "related": [
            ("/acquire/buy-a-car-wash", "Playbook", "How to Buy a Car Wash", "Formats, costs, financing, and the inspection list."),
            ("/acquire/laundromat-valuation", "Valuation", "Laundromat Valuation", "The other equipment-and-utilities business, priced."),
            ("/acquire/buy-a-gas-station", "Playbook", "Buy a Gas Station", "Often paired with a wash bay on the same parcel."),
            ("/acquire/how-to-value-a-business", "Guide", "How to Value a Business", "SDE, EBITDA, add-backs, and multiples explained."),
        ],
    },
    {
        "slug": "trucking-company-valuation",
        "plural": "trucking companies",
        "noun": "Trucking Company",
        "kw": "trucking company valuation",
        "title": "Trucking Company Valuation (2026): Multiples, Fleet &amp; Contracts",
        "desc": "What is a trucking company worth? Typical EBITDA multiples, how the fleet and contracted freight change the number, asset vs. asset-light, and a worked example.",
        "og_desc": "Trucking multiples, fleet treatment, contract freight, and a worked valuation example.",
        "intro": "Trucking valuation confuses buyers because the balance sheet is loud and the earnings are cyclical. A carrier can own $2M of tractors and trailers and still be worth less than an asset-light broker with a fraction of the equipment, because what buyers actually pay for is contracted, repeatable freight and a driver base that stays. This page covers how carriers and brokerages are priced, how to handle the fleet and its debt, and what moves a specific company up or down the range.",
        "buyer_metric": "EBITDA, with fleet equity treated separately",
        "low": "3.0x",
        "high": "5.0x",
        "mid": "4x",
        "range_note": "Small asset-based carriers commonly trade around 3x&ndash;4x EBITDA. Companies with contracted dedicated freight, low driver turnover, and a clean safety record reach the upper end. Freight brokerages are priced on their own logic and often higher, because they carry no fleet risk.",
        "drivers": [
            ("Contracted vs. spot freight", "Dedicated contracts and committed lanes are worth far more than spot-market exposure. Spot rates are volatile enough that buyers heavily discount earnings that depend on them, and a good spot year is not a durable earnings base."),
            ("Customer concentration", "One shipper at 40% of revenue is the most common reason a trucking deal reprices during diligence. Diversified revenue supports the top of the range."),
            ("Driver retention and pay", "Turnover is the industry's structural problem. A carrier with retention well below the industry norm has an operating advantage buyers will pay for; one that is chronically short of seats cannot run the trucks it owns."),
            ("Safety and compliance record", "CSA scores, the DOT rating, and the claims history feed directly into insurance cost, which is one of the largest line items. A poor record is both a price discount and, occasionally, a deal breaker."),
            ("Fleet age and financing", "Tractor age drives maintenance and near-term replacement. Equally important is what is owed: the enterprise value from the multiple is not the check the seller receives once equipment notes are settled."),
        ],
        "discounts": [
            "Revenue concentrated in one or two shippers.",
            "Earnings built on a spot-rate spike rather than contracted lanes.",
            "Tractors averaging past their trade cycle with deferred maintenance.",
            "Elevated CSA scores or a rising claims history driving insurance up.",
            "Owner-operator relationships that are informal and may not transfer.",
        ],
        "example_title": "Worked example: a 22-truck carrier at $900,000 EBITDA",
        "example": "A regional carrier reports $8.5M of revenue and $900,000 of EBITDA, with roughly 70% of miles under dedicated contracts. At 4x, enterprise value is about $3.6M. The fleet carries $1.9M of equipment debt, so the seller's actual proceeds before taxes and fees are closer to $1.7M. A buyer would then test the multiple: contracted freight and a clean safety record argue for holding at 4x, while an average tractor age of six years and one shipper at 30% of revenue argue for either a lower number or holdback tied to that customer renewing.",
        "faqs": [
            ("What multiple do trucking companies sell for?", "Small asset-based carriers typically sell for roughly 3x&ndash;5x EBITDA. The position within that range is set mainly by how much freight is contracted rather than spot, customer concentration, and the safety and insurance record."),
            ("How is the fleet valued?", "The multiple produces enterprise value, which already assumes the trucks needed to run the business are included. Equipment debt is then deducted to reach the equity value. Do not add fleet appraisal value on top of a cash-flow multiple &mdash; that double-counts the same asset."),
            ("Are freight brokerages worth more than carriers?", "Often, per dollar of EBITDA. A brokerage has no fleet, no drivers, and far lower fixed cost, so its earnings are less capital-intensive. The trade-off is that its value sits almost entirely in carrier and shipper relationships, which makes retention terms central to the deal."),
            ("What kills trucking deals in diligence?", "Three things dominate: customer concentration that turns out to be worse than presented, earnings that were a spot-rate anomaly, and safety or insurance problems that make the buyer's cost structure different from the seller's."),
        ],
        "related": [
            ("/acquire/buy-a-trucking-company", "Playbook", "How to Buy a Trucking Company", "Authority, insurance, drivers, and what to inspect."),
            ("/acquire/hvac-business-valuation", "Valuation", "HVAC Business Valuation", "Why recurring contracts raise a services multiple."),
            ("/acquire/buy-a-towing-company", "Playbook", "Buy a Towing Company", "Another fleet business with contract-driven revenue."),
            ("/acquire/how-to-value-a-business", "Guide", "How to Value a Business", "SDE, EBITDA, add-backs, and multiples explained."),
        ],
    },
]

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{title} | WholeSMB</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://wholesmb.com/acquire/{slug}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:url" content="https://wholesmb.com/acquire/{slug}">
  <meta property="og:site_name" content="WholeSMB">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{noun} Valuation &mdash; Multiples &amp; Drivers">
  <meta name="twitter:description" content="{og_desc}">

  <!-- Favicon -->
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="/img/apple-touch-icon.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/css/style.css">

  <!-- Schema: BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://wholesmb.com/"}},
      {{"@type": "ListItem", "position": 2, "name": "Buy a Business", "item": "https://wholesmb.com/acquire/"}},
      {{"@type": "ListItem", "position": 3, "name": "{noun} Valuation"}}
    ]
  }}
  </script>

  <!-- Schema: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{plain_title}",
    "description": "{plain_desc}",
    "author": {{"@type": "Organization", "name": "WholeSMB editorial team"}},
    "publisher": {{"@type": "Organization", "name": "WholeSMB", "url": "https://wholesmb.com"}},
    "datePublished": "2026-08-05",
    "dateModified": "2026-08-05",
    "mainEntityOfPage": "https://wholesmb.com/acquire/{slug}"
  }}
  </script>

  <!-- Schema: FAQPage -->
  <script type="application/ld+json">
  {faq_ld}
  </script>
  <script defer src="/_vercel/insights/script.js"></script>
  <script defer src="/_vercel/speed-insights/script.js"></script>
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <nav class="nav container">
      <a href="/" class="nav-logo">
        <svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect width="28" height="28" rx="6" fill="#2563eb"/><path d="M7 14l4 4 10-10" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Whole<span>SMB</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/acquire/">Buy a Business</a>
        <a href="/acquire/how-to-buy-a-business">Guides</a>
        <a href="/about.html">About</a>
      </div>
    </nav>
  </header>

  <!-- ===== Breadcrumb ===== -->
  <div class="container">
    <div class="breadcrumb">
      <a href="/">Home</a> <span>/</span>
      <a href="/acquire/">Buy a Business</a> <span>/</span>
      {noun} Valuation
    </div>
  </div>

  <!-- ===== Page Header ===== -->
  <section class="page-header" style="padding-top:24px">
    <div class="container">
      <h1>{h1}</h1>
      <p>{intro}</p>
      <p style="font-size:.813rem;color:var(--color-text-light);margin-top:8px">
        &#8505; <em>This page may contain affiliate links. See our <a href="/disclosure.html">disclosure</a>. Figures are general market ranges for orientation, not an appraisal &mdash; get a professional valuation before you sign anything.</em>
      </p>
    </div>
  </section>

  <!-- ===== Content ===== -->
  <section class="content">
    <div class="container">

      <div class="verdict-box">
        <h2>&#9889; The Short Answer</h2>
        <div class="verdict-columns">
          <div class="verdict-col">
            <h3>Typical range</h3>
            <p><strong>{low}&ndash;{high} {metric_short}</strong>, with {mid} a reasonable starting point before adjustments. {range_note}</p>
          </div>
          <div class="verdict-col">
            <h3>Priced on</h3>
            <p>{buyer_metric}. Start from normalized earnings, apply the multiple, then adjust for the specific factors below &mdash; that order matters more than the multiple you pick.</p>
          </div>
        </div>
      </div>

      <div class="content-body" style="max-width:100%">
"""

FOOTER = """
      </div>
    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <a href="/" class="footer-logo">
          <svg width="24" height="24" viewBox="0 0 28 28" fill="none"><rect width="28" height="28" rx="6" fill="#2563eb"/><path d="M7 14l4 4 10-10" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Whole<span>SMB</span>
        </a>
        <p>Your guide to finding, financing, and buying a profitable small business.</p>
      </div>
      <div>
        <h4>Browse</h4>
        <ul>
          <li><a href="/acquire/how-to-value-a-business">How to Value a Business</a></li>
          <li><a href="/acquire/laundromat-valuation">Laundromat Valuation</a></li>
          <li><a href="/acquire/hvac-business-valuation">HVAC Business Valuation</a></li>
          <li><a href="/acquire/car-wash-valuation">Car Wash Valuation</a></li>
          <li><a href="/acquire/trucking-company-valuation">Trucking Company Valuation</a></li>
          <li><a href="/acquire/how-to-buy-a-business">How to Buy a Business</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about.html">About</a></li>
          <li><a href="/disclosure.html">Affiliate Disclosure</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="/privacy.html">Privacy Policy</a></li>
          <li><a href="/disclosure.html">Disclosure</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; 2026 WholeSMB. All rights reserved. WholeSMB is a <a href="https://bity.llc">Bity LLC</a> property.</p>
    </div>
  </footer>

  <script src="/js/main.js"></script>
</body>
</html>
"""


def plain(s):
    return (s.replace("&amp;", "and").replace("&mdash;", "-")
             .replace("&ndash;", "-").replace("&rsquo;", "'").replace("&hellip;", "..."))


def faq_jsonld(faqs):
    items = []
    for q, a in faqs:
        items.append(
            '      {"@type": "Question", "name": "%s", "acceptedAnswer": {"@type": "Answer", "text": "%s"}}'
            % (plain(q), plain(a))
        )
    return ('{\n    "@context": "https://schema.org",\n    "@type": "FAQPage",\n'
            '    "mainEntity": [\n' + ",\n".join(items) + "\n    ]\n  }")


def build(n):
    metric_short = "SDE" if n["buyer_metric"].startswith("SDE") else "EBITDA"
    h1 = "How Much Is a %s Worth?" % n["noun"] if not n["noun"].endswith("Business") \
        else "How Much Is an %s Worth?" % n["noun"]
    head = HEADER.format(
        title=n["title"], desc=n["desc"], og_desc=n["og_desc"], slug=n["slug"],
        noun=n["noun"], h1=h1, intro=n["intro"], low=n["low"], high=n["high"],
        mid=n["mid"], range_note=n["range_note"], buyer_metric=n["buyer_metric"],
        metric_short=metric_short, faq_ld=faq_jsonld(n["faqs"]),
        plain_title=plain(n["title"]), plain_desc=plain(n["desc"]),
    )

    b = []
    b.append("        <h2>How %s are priced</h2>" % n["plural"])
    b.append("        <p>Every credible small-business valuation is the same two steps: normalize the earnings, then apply a multiple that reflects risk. Normalizing means stripping out the owner's personal expenses, one-time items, and any compensation that a new owner would not pay &mdash; and adding back nothing you cannot document. The multiple is where the specifics of this business show up. A %s is priced on <strong>%s</strong>, and the range below is the starting point, not the answer.</p>" % (n["noun"].lower(), n["buyer_metric"]))
    b.append('        <p>For the underlying mechanics &mdash; what counts as an add-back, how SDE differs from EBITDA, and how working capital is handled at close &mdash; see <a href="/acquire/how-to-value-a-business">how to value a business</a>.</p>')

    b.append("        <h2>What moves the multiple</h2>")
    b.append('        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">')
    for label, text in n["drivers"]:
        b.append("          <li><strong>%s</strong> &mdash; %s</li>" % (label, text))
    b.append("        </ul>")

    b.append('        <div class="cta-buttons">')
    b.append("          <!-- AFFILIATE: replace with SmartBiz SBA affiliate link once approved -->")
    b.append('          <a href="https://www.smartbizloans.com/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">Check SBA Loan Eligibility &rarr;</a>')
    b.append("          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->")
    b.append('          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-outline btn-lg" rel="nofollow sponsored" target="_blank">Compare Live Listings &rarr;</a>')
    b.append("        </div>")

    b.append("        <h2>What pulls the price down</h2>")
    b.append("        <p>These are the findings that most often reprice a deal between the letter of intent and the closing table. Each one is a reason to bid below the mid-range or to move part of the price into a seller note or earnout rather than paying it at close.</p>")
    b.append('        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">')
    for d in n["discounts"]:
        b.append("          <li>%s</li>" % d)
    b.append("        </ul>")

    b.append("        <h2>%s</h2>" % n["example_title"])
    b.append("        <p>%s</p>" % n["example"])
    b.append('        <p>Run the same arithmetic on any listing you are considering: divide the asking price by the stated earnings to get the implied multiple, then ask what in this specific business justifies its position relative to the %s&ndash;%s range. If nothing does, the price is the seller&rsquo;s hope rather than the market&rsquo;s.</p>' % (n["low"], n["high"]))

    b.append("        <h2>Before you rely on any of this</h2>")
    b.append("        <p>Market ranges orient a first conversation; they do not price a deal. Once you are past the initial screen, get the last three years of tax returns, reconcile them to the P&amp;L, and have an accountant or a certified appraiser confirm the normalized earnings. Working through our <a href=\"/acquire/business-due-diligence-checklist\">due diligence checklist</a> before you sign a letter of intent is the cheapest money you will spend on the transaction.</p>")

    b.append('        <div class="faq-section">')
    b.append("          <h2>Frequently Asked Questions</h2>")
    for q, a in n["faqs"]:
        b.append('          <div class="faq-item">')
        b.append("            <h3>%s</h3>" % q)
        b.append("            <p>%s</p>" % a)
        b.append("          </div>")
    b.append("        </div>")

    b.append("        <h2>Related Guides</h2>")
    b.append('        <div class="comparisons-grid" style="margin-top:20px">')
    for href, badge, name, blurb in n["related"]:
        b.append('          <a href="%s" class="comparison-card">' % href)
        b.append('            <span class="comparison-card-badge">%s</span>' % badge)
        b.append("            <h3>%s</h3>" % name)
        b.append("            <p>%s</p>" % blurb)
        b.append("          </a>")
    b.append('          <a href="/acquire/" class="comparison-card">')
    b.append('            <span class="comparison-card-badge">Hub</span>')
    b.append("            <h3>Buy a Business Hub</h3>")
    b.append("            <p>All our acquisition guides, valuation pages, and listing resources.</p>")
    b.append("          </a>")
    b.append("        </div>")

    return head + "\n".join(b) + FOOTER


if __name__ == "__main__":
    for n in NICHES:
        path = os.path.join(OUT, n["slug"] + ".html")
        with open(path, "w") as f:
            f.write(build(n))
        print("wrote", path)
