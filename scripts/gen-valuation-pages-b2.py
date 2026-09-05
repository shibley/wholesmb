#!/usr/bin/env python3
"""Generate batch 2 of the /acquire/ industry-valuation page family.

Same skeleton as batch 1 (laundromat / hvac / car-wash / trucking):
BreadcrumbList + Article + FAQPage JSON-LD, clean-URL canonical, affiliate
disclosure line, CTAs with rel="nofollow sponsored" target="_blank" behind
<!-- AFFILIATE: --> swap comments.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "acquire")
DATE = "2026-08-06"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://wholesmb.com/acquire/{slug}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{short_desc}">
  <meta property="og:url" content="https://wholesmb.com/acquire/{slug}">
  <meta property="og:site_name" content="WholeSMB">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{tw_title}">
  <meta name="twitter:description" content="{short_desc}">

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
      {{"@type": "ListItem", "position": 2, "name": "Buy a Business", "item": "https://wholesmb.com/acquire"}},
      {{"@type": "ListItem", "position": 3, "name": "{crumb}"}}
    ]
  }}
  </script>

  <!-- Schema: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{og_title}",
    "description": "{desc}",
    "author": {{"@type": "Organization", "name": "WholeSMB editorial team"}},
    "publisher": {{"@type": "Organization", "name": "WholeSMB", "url": "https://wholesmb.com"}},
    "datePublished": "{date}",
    "dateModified": "{date}",
    "mainEntityOfPage": "https://wholesmb.com/acquire/{slug}"
  }}
  </script>

  <!-- Schema: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_jsonld}
    ]
  }}
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
        <a href="/acquire">Buy a Business</a>
        <a href="/acquire/how-to-buy-a-business">Guides</a>
        <a href="/about.html">About</a>
      </div>
    </nav>
  </header>

  <!-- ===== Breadcrumb ===== -->
  <div class="container">
    <div class="breadcrumb">
      <a href="/">Home</a> <span>/</span>
      <a href="/acquire">Buy a Business</a> <span>/</span>
      {crumb}
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
            <p>{range_html}</p>
          </div>
          <div class="verdict-col">
            <h3>Priced on</h3>
            <p>{priced_on}</p>
          </div>
        </div>
      </div>

      <div class="content-body" style="max-width:100%">
        <h2>How {plural} are priced</h2>
        <p>{pricing_p1}</p>
        <p>For the underlying mechanics &mdash; what counts as an add-back, how SDE differs from EBITDA, and how working capital is handled at close &mdash; see <a href="/acquire/how-to-value-a-business">how to value a business</a>.</p>
        <h2>What moves the multiple</h2>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
{drivers}
        </ul>
        <div class="cta-buttons">
          <!-- AFFILIATE: replace with SmartBiz SBA affiliate link once approved -->
          <a href="https://www.smartbizloans.com/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">Check SBA Loan Eligibility &rarr;</a>
          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->
          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-outline btn-lg" rel="nofollow sponsored" target="_blank">Compare Live Listings &rarr;</a>
        </div>
        <h2>What pulls the price down</h2>
        <p>{drags_intro}</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
{drags}
        </ul>
        <h2>{example_h2}</h2>
        <p>{example_p1}</p>
        <p>{example_p2}</p>
        <h2>Before you rely on any of this</h2>
        <p>Market ranges orient a first conversation; they do not price a deal. Once you are past the initial screen, get the last three years of tax returns, reconcile them to the P&amp;L, and have an accountant or a certified appraiser confirm the normalized earnings. Working through our <a href="/acquire/business-due-diligence-checklist">due diligence checklist</a> before you sign a letter of intent is the cheapest money you will spend on the transaction.</p>
        <div class="faq-section">
          <h2>Frequently Asked Questions</h2>
{faq_html}
        </div>
        <h2>Related Guides</h2>
        <div class="comparisons-grid" style="margin-top:20px">
{related}
          <a href="/acquire/how-to-value-a-business" class="comparison-card">
            <span class="comparison-card-badge">Method</span>
            <h3>How to Value a Business</h3>
            <p>SDE, EBITDA, add-backs, and the arithmetic behind every multiple.</p>
          </a>
          <a href="/acquire" class="comparison-card">
            <span class="comparison-card-badge">Hub</span>
            <h3>Buy a Business Hub</h3>
            <p>All our acquisition guides, valuation pages, and listing resources.</p>
          </a>
        </div>
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
        <h4>Valuation Guides</h4>
        <ul>
          <li><a href="/acquire/how-to-value-a-business">How to Value a Business</a></li>
          <li><a href="/acquire/restaurant-valuation">Restaurant Valuation</a></li>
          <li><a href="/acquire/self-storage-valuation">Self-Storage Valuation</a></li>
          <li><a href="/acquire/auto-repair-shop-valuation">Auto Repair Shop Valuation</a></li>
          <li><a href="/acquire/laundromat-valuation">Laundromat Valuation</a></li>
          <li><a href="/acquire/hvac-business-valuation">HVAC Business Valuation</a></li>
          <li><a href="/acquire/car-wash-valuation">Car Wash Valuation</a></li>
          <li><a href="/acquire/trucking-company-valuation">Trucking Company Valuation</a></li>
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

CARD = """          <a href="/acquire/{href}" class="comparison-card">
            <span class="comparison-card-badge">{badge}</span>
            <h3>{title}</h3>
            <p>{blurb}</p>
          </a>
"""


def jsonld_escape(s):
    return s.replace("&mdash;", "-").replace("&ndash;", "-").replace("&rsquo;", "'") \
            .replace("&amp;", "and").replace("&quot;", "'").replace('"', "'")


PAGES = [
    {
        "slug": "restaurant-valuation",
        "crumb": "Restaurant Valuation",
        "title": "Restaurant Valuation (2026): What Multiple Do Restaurants Sell For? | WholeSMB",
        "og_title": "Restaurant Valuation (2026): What Multiple Do Restaurants Sell For?",
        "tw_title": "Restaurant Valuation &mdash; Multiples &amp; Drivers",
        "desc": "How much is a restaurant worth? Typical SDE multiples, why the lease and the liquor licence matter more than the food, and a worked valuation example.",
        "short_desc": "Typical restaurant SDE multiples, what raises and lowers the number, and a worked valuation example.",
        "h1": "How Much Is a Restaurant Worth?",
        "plural": "restaurants",
        "intro": "Restaurants are the most frequently mispriced small business on the market, in both directions. Sellers price off what they spent building it out; buyers price off a multiple they read somewhere. Neither is how the deal actually clears. A restaurant is worth the cash it produces for an owner-operator, discounted for how much of that cash depends on the owner personally &mdash; and then bounded, hard, by the lease and the licences. This page covers the range restaurants really trade in, the specific factors that move a deal up or down that range, and how to sanity-check an asking price before you spend a dollar on diligence.",
        "range_html": "<strong>1.5x&ndash;3.0x SDE</strong>, with roughly 2x a reasonable starting point. Single-location independents with an owner behind the pass sit at the low end. Established, managed restaurants with a long assignable lease, a transferable liquor licence, and three clean years of tax returns reach the top of the range.",
        "priced_on": "SDE (seller's discretionary earnings), with a separate look at the asset value of the build-out. Multi-unit groups with real management depth get priced on EBITDA instead, and at higher multiples, because the earnings survive the owner leaving.",
        "pricing_p1": "Every credible small-business valuation is two steps: normalize the earnings, then apply a multiple that reflects risk. For a restaurant, normalizing is where most of the argument happens &mdash; owner and family labour is frequently unpaid or underpaid in the P&amp;L, and adding it back at market rates often cuts stated SDE by a third. Do that first. The multiple then reflects one question above all others: how much of this cash flow walks out the door with the seller? A restaurant where the owner is the chef, the face, and the scheduler is a job with inventory attached, and it prices like one.",
        "drivers": [
            "<strong>Remaining lease term and rent-to-sales</strong> &mdash; This is the single biggest driver. Ten or more years of assignable term including options supports a premium; under five years, or a landlord with consent rights they intend to use, caps the deal at the bottom of the range. Rent above roughly 10% of sales compresses the multiple regardless of term.",
            "<strong>Owner dependence</strong> &mdash; A restaurant with a salaried general manager and a chef under contract prices materially higher than an identical one run by the seller, because the buyer inherits an operation rather than a shift.",
            "<strong>Licence transferability</strong> &mdash; A full liquor licence that transfers cleanly carries real independent value in quota states and can be worth more than the operating business. One that does not transfer, or that sits with the seller personally, is a repricing event.",
            "<strong>Equipment and build-out condition</strong> &mdash; Hoods, walk-ins, HVAC, and line equipment near end of life are a near-term capital call the buyer must underwrite. Recent, documented, permitted work moves the number up.",
            "<strong>Verifiable sales mix</strong> &mdash; Three years of POS exports reconciled to sales-tax filings and merchant statements. Heavy cash with no corroboration is discounted, not credited &mdash; unreported sales you cannot verify are worth nothing to a buyer and nothing to a lender.",
        ],
        "drags_intro": "These are the findings that most often reprice a restaurant deal between the letter of intent and the closing table. Each is a reason to bid below the mid-range, or to shift part of the price into a seller note or an earnout rather than paying it at close.",
        "drags": [
            "A lease under five years remaining, not assignable, or with a personal guarantee the landlord will not release.",
            "Stated SDE that does not expense the owner's or family's hours at market rates.",
            "Sales trending down over the trailing twelve months while the asking price is based on a peak year.",
            "Deferred maintenance on hood, refrigeration, or HVAC that the seller has never quoted.",
            "A liquor licence held personally, in dispute, or subject to a transfer queue measured in months.",
            "Concentration in one delivery platform whose commission structure can change without notice.",
        ],
        "example_h2": "Worked example: a $140,000 SDE neighbourhood restaurant",
        "example_p1": "A single-location restaurant reports $1.1M of revenue and $140,000 of SDE. The owner works the line six days a week and takes no salary; replacing that role costs about $65,000 fully loaded, so normalized SDE for a non-operating buyer is nearer $75,000. At 2x that is roughly $150,000 &mdash; not the $280,000 the 2x-on-stated-SDE arithmetic implies. Now adjust: the lease has eight years including options and assigns with landlord consent (neutral to positive), the walk-in and hood need about $35,000 of work in the next two years (down), and the liquor licence transfers cleanly and is separately marketable (up).",
        "example_p2": "A realistic bid lands nearer $130,000&ndash;$160,000 for the business, with the licence valued and negotiated on its own line and the equipment gap taken as a price reduction rather than absorbed at close. Run the same arithmetic on any listing you are considering: expense the owner's labour at market, divide the asking price by what is left, then ask what in this specific restaurant justifies its position relative to the 1.5x&ndash;3.0x range. If nothing does, the price is the seller's cost basis rather than the market's.",
        "faq": [
            ("What multiple do restaurants sell for?",
             "Most independent restaurants trade at roughly 1.5x&ndash;3.0x SDE, with about 2x a fair starting point. The spread is driven by owner dependence, remaining lease term, and how verifiable the sales are. Multi-unit groups with real management depth are priced on EBITDA instead and clear at higher multiples."),
            ("Is a restaurant valued on revenue?",
             "Rarely, and never well. Revenue multiples circulate because they are easy, but restaurant margins vary enormously with rent, labour model, and sales mix. Two restaurants with identical revenue can differ threefold in owner earnings. Price the normalized SDE."),
            ("How is the liquor licence valued?",
             "Separately, in states where licences are quota-limited and independently marketable. In those markets the licence can be worth more than the operating business and should be a distinct line in the purchase agreement. In open-licence states it carries little standalone value."),
            ("Does the build-out add to the price?",
             "Not as an addition on top of a cash-flow price &mdash; the equipment is already producing the earnings you are buying. Build-out value matters mostly as a floor: a profitable restaurant should never sell for less than the depreciated resale value of its assets, and a loss-making one usually sells at exactly that."),
        ],
        "related": [
            ("buy-a-restaurant", "Playbook", "How to Buy a Restaurant", "The full playbook: economics, licences, and what to inspect."),
            ("buy-a-bar", "Playbook", "How to Buy a Bar", "Where bar economics and licensing differ from a restaurant."),
            ("buy-a-coffee-shop", "Playbook", "How to Buy a Coffee Shop", "Smaller footprint, different labour model, different multiple."),
        ],
    },
    {
        "slug": "self-storage-valuation",
        "crumb": "Self-Storage Valuation",
        "title": "Self-Storage Valuation (2026): Cap Rates, NOI &amp; What Facilities Sell For | WholeSMB",
        "og_title": "Self-Storage Valuation (2026): Cap Rates, NOI and What Facilities Sell For",
        "tw_title": "Self-Storage Valuation &mdash; Cap Rates &amp; NOI",
        "desc": "How much is a self-storage facility worth? Why storage is priced on NOI and a cap rate rather than an SDE multiple, what moves the rate, and a worked example.",
        "short_desc": "Self-storage is priced on NOI and a cap rate. What moves the rate, and a worked valuation example.",
        "h1": "How Much Is a Self-Storage Facility Worth?",
        "plural": "self-storage facilities",
        "intro": "Self-storage is the one business on this site that is usually not priced on an earnings multiple at all. It is real estate with an operating business bolted on, and it trades the way real estate trades: net operating income divided by a capitalisation rate. Getting that right matters more than any negotiating tactic, because a half-point of cap rate on a facility with $200,000 of NOI is a swing of hundreds of thousands of dollars. This page covers how storage valuations are actually built, what moves the cap rate up or down, and how to check an asking price before you spend money on diligence.",
        "range_html": "<strong>Value = NOI &divide; cap rate.</strong> Cap rates for small non-institutional facilities commonly sit in the <strong>6.5%&ndash;9%</strong> band, with class-B and rural assets at the higher (cheaper) end and modern climate-controlled facilities in growing metros at the lower end. Every point of cap rate is worth far more than any operating improvement you can make in year one.",
        "priced_on": "NOI &mdash; gross potential rent, less vacancy and concessions, less all operating expenses including a market management fee. Not SDE, and not the seller's cash flow after their own labour.",
        "pricing_p1": "Build NOI from the rent roll, not the P&amp;L. Start with gross potential rent at current street rates, subtract actual economic vacancy (physical vacancy plus concessions and delinquency), add ancillary income you can verify &mdash; late fees, tenant insurance commission, retail, truck rental &mdash; then subtract every real operating expense: property tax at the reassessed post-sale basis, insurance at a current quote, utilities, repairs, marketing, and a market-rate management fee of roughly 5%&ndash;6% of revenue even if the seller manages it themselves. That last adjustment is the one sellers leave out, and it is often the difference between the asking price and a fundable one.",
        "drivers": [
            "<strong>Economic occupancy, not physical</strong> &mdash; A facility that is 92% full because half the tenants are on a first-month-free promotion is not a 92% facility. Pull twelve months of the rent roll and compute collected rent against gross potential.",
            "<strong>Rate history and pull-through</strong> &mdash; Whether existing customer rate increases actually stick without a spike in move-outs. A facility that has never raised rates has upside; a facility that raised them last quarter has already used it.",
            "<strong>Competitive supply within three miles</strong> &mdash; Storage demand is hyper-local and new supply is fast to build. A permitted competitor inside the catchment is a direct, quantifiable hit to future NOI and should move the cap rate up.",
            "<strong>Unit mix and climate control</strong> &mdash; Climate-controlled square footage commands higher rates and lower turnover in most markets. A mix weighted to large drive-up units in a market that wants 10x10s is a rate problem you cannot fix cheaply.",
            "<strong>Deferred capital and site condition</strong> &mdash; Roofs, doors, paving, gate and access-control software, and fencing. These do not show up in NOI but they come straight off what you should pay.",
            "<strong>Expansion or lease-up upside</strong> &mdash; Excess land with zoning, or a facility in genuine lease-up, is worth paying for &mdash; but underwrite it as your return, not the seller's.",
        ],
        "drags_intro": "These are the findings that most often reprice a storage deal between the letter of intent and the closing table. Each one is a reason to bid at a higher cap rate, or to hold back part of the price until the issue is resolved.",
        "drags": [
            "A pro forma priced on street rates the facility has never actually achieved.",
            "Property tax modelled at the seller's assessed basis rather than the post-sale reassessment.",
            "No management fee in the expense stack because the seller runs it themselves.",
            "Concessions and delinquency buried so physical occupancy overstates economic occupancy.",
            "A permitted or under-construction competitor within the three-mile catchment.",
            "Deferred roof, paving, or gate-system work the seller has never obtained a quote for.",
        ],
        "example_h2": "Worked example: a $210,000 NOI facility",
        "example_p1": "A 340-unit facility is listed at $3.0M on a stated NOI of $210,000 &mdash; an implied 7.0% cap. Rebuild the NOI: property tax reassesses on sale and adds about $14,000, there is no management fee in the seller's numbers so add roughly $11,000 at 5% of revenue, and twelve months of rent roll show economic occupancy at 84% against the 91% physical figure in the marketing package, costing about another $12,000. Real NOI is closer to $173,000.",
        "example_p2": "At the same 7.0% cap that is $2.47M, not $3.0M. Then decide whether 7.0% is even the right rate for a class-B asset with a competitor permitted two miles away &mdash; at 8.0% it is $2.16M, and $95,000 of deferred paving comes off that. Run this on every storage listing you screen: rebuild NOI from the rent roll with a full expense stack, then apply a cap rate you can defend with local comparable sales rather than the one the listing implies.",
        "faq": [
            ("Is self-storage valued on a multiple or a cap rate?",
             "A cap rate. Value equals net operating income divided by the capitalisation rate. SDE multiples are used for very small operator-run facilities without real estate, but any facility that includes the land and buildings is valued as income-producing real estate."),
            ("What cap rate should I use for a small facility?",
             "Small non-institutional facilities commonly trade in the 6.5%&ndash;9% range, but the only defensible number comes from recent comparable sales in the same market. Class, location, competitive supply, and asset condition all move it. Do not take the cap rate implied by the asking price as evidence of the market rate."),
            ("What expenses do sellers most often leave out?",
             "Three, consistently: a market-rate management fee when the owner self-manages, property tax at the post-sale reassessed basis rather than the seller's, and a realistic repairs-and-maintenance line. Adding all three back typically reduces stated NOI by 10%&ndash;20%."),
            ("Does the real estate get valued separately from the business?",
             "No &mdash; in a standard storage acquisition the income and the real estate are one asset and the cap rate prices both together. The business is only valued separately when you are buying an operating leasehold without the land, which is uncommon at this size."),
        ],
        "related": [
            ("buy-a-self-storage-business", "Playbook", "How to Buy a Self-Storage Business", "The full playbook: sourcing, financing, and site diligence."),
            ("buy-a-mobile-home-park", "Playbook", "How to Buy a Mobile Home Park", "The other NOI-and-cap-rate small asset class."),
            ("buy-an-rv-park", "Playbook", "How to Buy an RV Park", "Seasonal income, similar underwriting discipline."),
        ],
    },
    {
        "slug": "auto-repair-shop-valuation",
        "crumb": "Auto Repair Shop Valuation",
        "title": "Auto Repair Shop Valuation (2026): What Multiple Do Shops Sell For? | WholeSMB",
        "og_title": "Auto Repair Shop Valuation (2026): What Multiple Do Shops Sell For?",
        "tw_title": "Auto Repair Shop Valuation &mdash; Multiples &amp; Drivers",
        "desc": "How much is an auto repair shop worth? Typical SDE multiples, why technician retention and the property decide the number, and a worked valuation example.",
        "short_desc": "Typical auto repair shop SDE multiples, what raises and lowers the number, and a worked example.",
        "h1": "How Much Is an Auto Repair Shop Worth?",
        "plural": "auto repair shops",
        "intro": "An independent auto repair shop is bought for its repeat customer base and its technicians, and it is priced on cash flow. What separates a 2x shop from a 3.5x shop is almost never the equipment &mdash; it is whether the earnings survive the seller leaving and whether the techs stay. A shop where the owner is also the master technician and the service writer is buying yourself a job; a shop with two certified techs on the floor and a manager running the counter is buying a business. This page covers the range shops actually trade in, what moves a deal within it, and how to check an asking price before you spend money on diligence.",
        "range_html": "<strong>2.0x&ndash;3.5x SDE</strong> for the business, with roughly 2.5x a fair starting point, plus real estate valued separately if it is included. Owner-tech shops in secondary markets sit at the bottom; shops with certified staff technicians, a manager, fleet or warranty contracts, and clean books reach the top and occasionally beyond.",
        "priced_on": "SDE for shops under roughly $1M of revenue; EBITDA with a market manager salary expensed for larger, multi-bay operations. Real estate, when the seller owns it, is appraised and priced on its own rather than folded into the multiple.",
        "pricing_p1": "Normalize first. Expense the owner's technician and service-writer hours at what it would actually cost to replace them &mdash; certified tech wages have moved a long way, and a shop whose stated SDE assumes free skilled labour is quoting a number no buyer can reproduce. Then check whether the shop rents from or owns its building: if the seller owns it and charges the business below-market rent, restate rent to market before applying any multiple, or you will pay a multiple on a subsidy that ends at close.",
        "drivers": [
            "<strong>Technician retention</strong> &mdash; The most important factor and the hardest to diligence. Certified techs are scarce; two who leave at close can take a third of gross profit with them. Tenure, pay structure, and whether they have met the buyer all move the number.",
            "<strong>Owner independence</strong> &mdash; A shop with a service manager running the counter and the owner out of the bays prices a full turn higher than an identical shop where the owner does both jobs.",
            "<strong>Repeat customer base and car count</strong> &mdash; Named, returning customers in the shop management system with visit history. Car count trend over three years matters more than any single year's revenue.",
            "<strong>Fleet, warranty, and commercial contracts</strong> &mdash; Contracted volume that transfers with the business is worth a premium over walk-in work, provided the contracts are assignable and not personal to the seller.",
            "<strong>Building: lease term or ownership</strong> &mdash; Repair shops are permitted, zoned, and lifted; they do not relocate cheaply. A long assignable lease, or a purchasable building, supports the top of the range. A short lease in an area zoning out auto uses is a discount and a risk.",
            "<strong>Equipment and diagnostic currency</strong> &mdash; Lifts within inspection, current scan tools and subscriptions, and ADAS calibration capability. Falling behind on diagnostics is a capital call and a lost-work problem at once.",
        ],
        "drags_intro": "These are the findings that most often reprice a shop between the letter of intent and the closing table. Each is a reason to bid below the mid-range, or to move part of the price into a seller note or a retention-linked earnout.",
        "drags": [
            "Stated SDE that does not expense the owner's own wrench or service-writer hours at market.",
            "Below-market rent from a seller-owned building that will reset when the lease is renegotiated.",
            "Key technicians with no notice period, no retention agreement, and no intention to stay.",
            "Declining car count masked by rising ticket averages and parts price inflation.",
            "Uninspected or out-of-certification lifts, or an environmental issue at the site.",
            "Revenue concentrated in one fleet account that has never been under a written contract.",
        ],
        "example_h2": "Worked example: a $185,000 SDE three-bay shop",
        "example_p1": "A three-bay shop reports $820,000 of revenue and $185,000 of SDE. The owner turns wrenches roughly half-time; replacing that labour costs about $45,000 fully loaded, so normalized SDE is nearer $140,000. The seller owns the building and charges the business $2,000 a month against a market rent of $3,800, so restate rent and normalized SDE falls to about $118,000. At a mid-range 2.5x, the business is roughly $295,000 &mdash; before the building, which is appraised and negotiated separately.",
        "example_p2": "Now adjust: both certified techs have five-plus years of tenure and have agreed to stay with a modest retention bonus (up), car count is flat over three years while ticket average carries the revenue growth (neutral to down), and two lifts are due for recertification with about $12,000 of work (down). A realistic bid lands nearer $270,000&ndash;$300,000 for the business, with the retention bonuses funded from the price and the lift work taken as a reduction. Run the same arithmetic on any shop you screen: expense the owner's labour and restate rent to market, then divide the asking price by what is left.",
        "faq": [
            ("What multiple do auto repair shops sell for?",
             "Most independent shops trade at roughly 2.0x&ndash;3.5x SDE, with about 2.5x a fair starting point. Owner-technician shops sit at the bottom of the range; shops with certified staff technicians, a service manager, and transferable fleet or warranty contracts sit at the top. Real estate is valued separately."),
            ("Is the real estate included in the multiple?",
             "No. When the seller owns the building it should be appraised and priced on its own, and the business earnings should be restated at market rent first. Paying a business multiple on earnings that only exist because of below-market rent is one of the most common overpayments in this sector."),
            ("How do I diligence technician retention?",
             "Ask for tenure, pay structure, and certification status for every technician, then make a meeting with the key techs a condition before closing. Where the seller will not allow contact until late in the process, shift a portion of the price into a seller note or an earnout tied to the first twelve months of gross profit."),
            ("Does equipment add to the price?",
             "Not on top of a cash-flow price &mdash; the lifts and scan tools are already producing the earnings you are buying. Equipment matters as a deduction: anything out of certification, out of subscription, or unable to service the vehicles in your local car parc is a near-term cost that comes off what you pay."),
        ],
        "related": [
            ("buy-an-auto-repair-shop", "Playbook", "How to Buy an Auto Repair Shop", "The full playbook: sourcing, financing, and shop-floor diligence."),
            ("buy-a-towing-company", "Playbook", "How to Buy a Towing Company", "Adjacent automotive services, different asset intensity."),
            ("hvac-business-valuation", "Valuation", "HVAC Business Valuation", "The other skilled-trade business where technicians set the multiple."),
        ],
    },
]


def render(p):
    faq_jsonld = ",\n".join(
        '      {{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}'.format(
            q=jsonld_escape(q), a=jsonld_escape(a))
        for q, a in p["faq"])
    faq_html = "\n".join(
        '          <div class="faq-item">\n            <h3>{q}</h3>\n            <p>{a}</p>\n          </div>'.format(q=q, a=a)
        for q, a in p["faq"])
    drivers = "\n".join("          <li>{}</li>".format(d) for d in p["drivers"])
    drags = "\n".join("          <li>{}</li>".format(d) for d in p["drags"])
    related = "".join(CARD.format(href=h, badge=b, title=t, blurb=bl) for h, b, t, bl in p["related"])
    return TEMPLATE.format(
        date=DATE, faq_jsonld=faq_jsonld, faq_html=faq_html,
        drivers=drivers, drags=drags, related=related, **{
            k: p[k] for k in ("slug", "crumb", "title", "og_title", "tw_title", "desc",
                              "short_desc", "h1", "plural", "intro", "range_html",
                              "priced_on", "pricing_p1", "drags_intro", "example_h2",
                              "example_p1", "example_p2")})


for p in PAGES:
    path = os.path.join(OUT, p["slug"] + ".html")
    with open(path, "w") as f:
        f.write(render(p))
    print("wrote", path)
