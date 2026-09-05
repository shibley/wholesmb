#!/usr/bin/env python3
"""One-off generator for /acquire/ marketplace-comparison pages.

Builds pages on the same shell as flippa-vs-empire-flippers.html so the
comparison sub-family stays visually and structurally consistent.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "acquire")
BASE = "https://wholesmb.com"


def faq_ld(faqs):
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faqs
            ],
        },
        indent=2,
    )


def build(p):
    url = f"{BASE}/acquire/{p['slug']}"
    faq_html = "\n".join(
        f"""          <div class="faq-item">
            <h3>{q}</h3>
            <p>{a}</p>
          </div>"""
        for q, a in p["faqs"]
    )
    related_html = "\n".join(
        f"""          <a href="{href}" class="comparison-card">
            <span class="comparison-card-badge">{badge}</span>
            <h3>{title}</h3>
            <p>{blurb}</p>
          </a>"""
        for href, badge, title, blurb in p["related"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{p['title']}</title>
  <meta name="description" content="{p['meta']}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{url}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{p['og_title']}">
  <meta property="og:description" content="{p['og_desc']}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="WholeSMB">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p['og_title']}">
  <meta name="twitter:description" content="{p['og_desc']}">

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
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/"}},
      {{"@type": "ListItem", "position": 2, "name": "Buy a Business", "item": "{BASE}/acquire"}},
      {{"@type": "ListItem", "position": 3, "name": "{p['crumb']}"}}
    ]
  }}
  </script>

  <!-- Schema: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{p['title'].split(' | ')[0]}",
    "description": "{p['article_desc']}",
    "author": {{"@type": "Organization", "name": "WholeSMB editorial team"}},
    "publisher": {{
      "@type": "Organization",
      "name": "WholeSMB",
      "url": "{BASE}"
    }},
    "datePublished": "2026-08-04",
    "dateModified": "2026-08-04",
    "mainEntityOfPage": "{url}"
  }}
  </script>

  <!-- Schema: FAQPage -->
  <script type="application/ld+json">
{faq_ld(p['faqs'])}
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
      {p['crumb']}
    </div>
  </div>

  <!-- ===== Page Header ===== -->
  <section class="page-header" style="padding-top:24px">
    <div class="container">
      <h1>{p['h1']}</h1>
      {p['intro']}
      <p style="font-size:.813rem;color:var(--color-text-light);margin-top:8px">
        &#8505; <em>This page may contain affiliate links. See our <a href="/disclosure.html">disclosure</a>.</em>
      </p>
    </div>
  </section>

  <!-- ===== Content ===== -->
  <section class="content">
    <div class="container">

      <div class="verdict-box">
        <h2>&#9889; Quick Verdict</h2>
        <div class="verdict-columns">
          <div class="verdict-col">
            <h3>{p['verdict_a_title']}</h3>
            <p>{p['verdict_a']}</p>
          </div>
          <div class="verdict-col">
            <h3>{p['verdict_b_title']}</h3>
            <p>{p['verdict_b']}</p>
          </div>
        </div>
      </div>

      <div class="content-body" style="max-width:100%">

{p['body']}

        <!-- FAQ -->
        <div class="faq-section">
          <h2>Frequently Asked Questions</h2>
{faq_html}
        </div>

        <!-- Related -->
        <h2>Related Guides</h2>
        <div class="comparisons-grid" style="margin-top:20px">
{related_html}
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
        <h4>Browse</h4>
        <ul>
          <li><a href="/acquire/how-to-buy-a-business">How to Buy a Business</a></li>
          <li><a href="/acquire/best-websites-to-buy-a-business">Best Websites to Buy a Business</a></li>
          <li><a href="/acquire/flippa-vs-empire-flippers">Flippa vs Empire Flippers</a></li>
          <li><a href="/acquire/bizbuysell-vs-flippa">BizBuySell vs Flippa</a></li>
          <li><a href="/acquire/bizbuysell-review">BizBuySell Review</a></li>
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


PAGES = []

# ---------------------------------------------------------------- page 1
PAGES.append({
    "slug": "bizbuysell-vs-flippa",
    "crumb": "BizBuySell vs Flippa",
    "title": "BizBuySell vs Flippa (2026): Main Street or Online? | WholeSMB",
    "meta": "BizBuySell lists Main Street businesses with premises and staff. Flippa lists internet businesses you run from anywhere. A buyer-side comparison of inventory, financing, diligence and what you are actually buying.",
    "og_title": "BizBuySell vs Flippa: Main Street or Online?",
    "og_desc": "Two marketplaces, two entirely different asset classes. Which one matches the business you actually want to own?",
    "article_desc": "A buyer-side comparison of BizBuySell and Flippa covering what each marketplace lists, how financing differs between Main Street and online assets, what diligence each demands, and which buyer each suits.",
    "h1": "BizBuySell vs Flippa: Which Marketplace Fits the Business You Want?",
    "intro": """<p>These two get compared as competitors, and they barely overlap. <strong>BizBuySell</strong> is the largest listing site for Main Street businesses in the United States &mdash; restaurants, auto shops, laundromats, HVAC contractors, liquor stores. Physical premises, employees, local customers, and a business you generally have to show up to. <strong>Flippa</strong> is an open marketplace for internet businesses &mdash; content sites, ecommerce stores, apps, small SaaS, domains. No premises, often no staff, run from wherever you are.</p>
      <p>So the real question is not which marketplace is better. It is which asset class you want to own, because that decision determines everything downstream: how you finance it, how long the search takes, what diligence looks like, and what your week looks like after closing.</p>""",
    "verdict_a_title": "Choose BizBuySell if…",
    "verdict_a": "You want cash flow attached to something physical and local, you can qualify for or already have SBA financing, and you are willing to be present in the business. Multiples are lower, leverage is available, and the earnings tend to be steadier than online equivalents.",
    "verdict_b_title": "Choose Flippa if…",
    "verdict_b": "You want an asset you can operate remotely, your capital is limited, and you can move fast on verification. Entry prices start far lower, there is no lender to satisfy, but the quality range is wide and the earnings are more fragile.",
    "body": """        <h2>Head to head</h2>
        <table class="feature-table">
          <thead>
            <tr>
              <th>&nbsp;</th>
              <th>BizBuySell</th>
              <th>Flippa</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Asset class</strong></td>
              <td>Main Street &mdash; physical, local, staffed</td>
              <td>Internet &mdash; content, ecommerce, apps, domains</td>
            </tr>
            <tr>
              <td><strong>Listing source</strong></td>
              <td>Mostly business brokers, plus some owner-listed</td>
              <td>Mostly owner-listed, self-serve</td>
            </tr>
            <tr>
              <td><strong>Vetting</strong></td>
              <td><span class="cross">&#10007;</span> Listing site, not a broker &mdash; the broker screens, not the platform</td>
              <td><span class="cross">&#10007;</span> Limited screening; buyer is the first filter</td>
            </tr>
            <tr>
              <td><strong>Financing</strong></td>
              <td><span class="check">&#10003;</span> SBA 7(a) is routine at these deal sizes</td>
              <td>Rare &mdash; usually cash, sometimes seller notes</td>
            </tr>
            <tr>
              <td><strong>Typical earnings basis</strong></td>
              <td>Seller's discretionary earnings, tax-return supported</td>
              <td>Net profit from dashboards and processor data</td>
            </tr>
            <tr>
              <td><strong>Where the risk sits</strong></td>
              <td>Staff, lease, licences, owner-dependence, local demand</td>
              <td>Traffic durability, platform policy, supplier and channel concentration</td>
            </tr>
            <tr>
              <td><strong>Time to close</strong></td>
              <td>Months &mdash; lender, landlord and licensing all gate it</td>
              <td>Days to weeks &mdash; escrow and asset transfer</td>
            </tr>
            <tr>
              <td><strong>Post-close life</strong></td>
              <td>You manage people and a location</td>
              <td>You manage traffic, product and vendors, remotely</td>
            </tr>
          </tbody>
        </table>

        <div class="cta-buttons">
          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->
          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">Browse Main Street Listings on BizBuySell &rarr;</a>
          <!-- AFFILIATE: replace with Flippa affiliate link once approved -->
          <a href="https://flippa.com/businesses" class="btn btn-outline btn-lg" rel="nofollow sponsored" target="_blank">Browse Online Listings on Flippa &rarr;</a>
        </div>

        <h2>The financing gap is the biggest practical difference</h2>
        <p>This is the part most comparisons skip, and it changes the maths more than anything on the feature table. A profitable Main Street business with clean tax returns is a familiar credit to a lender: there are hard assets, a lease, verifiable filings, and decades of comparable loans behind it. That means a buyer with a modest down payment and a decent credit profile can control a business several times larger than their cash position. Our <a href="/acquire/how-to-buy-a-business-with-an-sba-loan">SBA loan guide</a> walks the process end to end.</p>
        <p>Internet businesses generally do not get that treatment. There is rarely collateral, the earnings history is short, and the durability of the traffic is hard for an underwriter to assess. Some lenders do write these deals, but they are the exception rather than the default. In practice most Flippa purchases are cash, occasionally with a seller note attached &mdash; see <a href="/acquire/seller-financing-business-purchase">seller financing</a> for how to structure that.</p>
        <p>The consequence is counter-intuitive. Online listings look cheaper at the sticker, but Main Street is often more accessible to a buyer with limited cash, because leverage is available. A buyer with $60,000 might buy a small content site outright, or put that same $60,000 down on a Main Street business earning several times as much. Those are very different outcomes from the same starting capital, and the risk profiles differ accordingly &mdash; debt service is a fixed obligation that does not care whether the business had a slow quarter.</p>

        <h2>What diligence looks like on each</h2>
        <p>On BizBuySell you are usually verifying <strong>documents and people</strong>. Three years of tax returns reconciled to the profit and loss, the add-backs that turn reported profit into seller's discretionary earnings and whether each one is genuinely discretionary, the lease and whether it transfers or has to be renegotiated, licences and whether they are transferable in your state, and how much of the customer relationship lives in the departing owner's head. Staff are both the asset and the risk: a business that runs without the owner is worth a premium, a business that <em>is</em> the owner may be worth very little to you.</p>
        <p>On Flippa you are verifying <strong>systems and durability</strong>. Analytics access granted directly rather than screenshots, revenue traced to the payment processor and reconciled to a bank account, traffic composition rather than traffic totals, and concentration in every dimension &mdash; one keyword, one referrer, one supplier, one platform whose policy change could end the business. The <a href="/acquire/business-due-diligence-checklist">due diligence checklist</a> covers both paths, but the weighting differs sharply.</p>
        <p>One thing is identical on both platforms: neither is vouching for the business. BizBuySell is a listing site where brokers advertise; the broker works for the seller. Flippa is an open marketplace with limited screening. In both cases the only diligence that protects you is the diligence you run yourself.</p>

        <h2>Which multiple is actually cheaper?</h2>
        <p>Main Street businesses generally trade at lower multiples of earnings than online businesses of similar size, and buyers often read that as a bargain. Some of it is a genuine risk discount and some is a liquidity discount &mdash; a laundromat in one county has a limited pool of buyers, while a content site is sellable to anyone with an internet connection.</p>
        <p>But the lower multiple is partly compensation for real obligations: you may be tied to a location, a lease, a payroll, and a set of licences. The higher online multiple buys mobility and buys out of payroll, and pays for it with earnings that can move sharply when a platform changes its rules. Neither is free. Underwrite each on your own verified earnings using <a href="/acquire/how-to-value-a-business">the valuation approach</a> rather than comparing headline multiples across two asset classes that do not measure the same risk.</p>

        <h2>How to decide</h2>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Start with your week, not the listing.</strong> Do you want to manage employees at a location, or manage a website from anywhere? That answer eliminates one platform immediately, and it is a lifestyle question more than a financial one.</li>
          <li><strong>Then check your financing.</strong> If you can qualify for SBA debt, Main Street lets your capital reach much further. If you cannot, or you want to avoid a personal guarantee, the online route is the realistic one.</li>
          <li><strong>Then pick a category and learn it.</strong> The buyers who do worst on both platforms are the ones evaluating listings across five unrelated industries at once. Our category playbooks &mdash; <a href="/acquire/buy-a-laundromat">laundromats</a>, <a href="/acquire/buy-a-hvac-business">HVAC</a>, <a href="/acquire/buy-a-saas-business">SaaS</a>, <a href="/acquire/buy-an-ecommerce-business">ecommerce</a> &mdash; exist to give you a baseline for what normal looks like before you value anything.</li>
          <li><strong>Watch both if you are genuinely undecided.</strong> Browsing is free on each, and a month of watching listings in two categories teaches you more about pricing than any article can.</li>
        </ul>

        <div class="cta-buttons">
          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->
          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">See Businesses for Sale Near You &rarr;</a>
        </div>

        <p>If you want the wider field rather than a head-to-head, our roundup of the <a href="/acquire/best-websites-to-buy-a-business">best websites to buy a business</a> covers all five main marketplaces, and <a href="/acquire/flippa-vs-empire-flippers">Flippa vs Empire Flippers</a> handles the open-versus-curated question within the online category.</p>
""",
    "faqs": [
        ("Is BizBuySell or Flippa better for a first-time buyer?",
         "It depends on which kind of business you want to own rather than on which platform is better run. BizBuySell lists Main Street businesses with premises, staff and local customers, and those deals are usually financeable with an SBA loan, so a first-time buyer with a modest down payment can acquire meaningful cash flow. Flippa lists internet businesses that are cheaper at the sticker and transfer in days rather than months, which makes them a lower-stakes first purchase, but they are almost always cash deals and the earnings are more fragile. A first-time buyer who wants to keep a job while learning usually starts online. A first-time buyer who wants the acquisition to replace their income usually starts on Main Street."),
        ("Does BizBuySell vet its listings?",
         "No. BizBuySell is a listing marketplace rather than a broker or an escrow service. Most listings are placed by business brokers who represent the seller, and the platform does not independently verify the financials presented in a listing. That is not a criticism of the site, it is simply how a classifieds model works, but buyers sometimes assume broker involvement means the numbers have been audited. It has not been. Treat every figure in a listing as a claim to be verified against tax returns, bank statements and the profit and loss before you rely on it."),
        ("Can you get an SBA loan for a Flippa business?",
         "Sometimes, but it is the exception. SBA lenders are most comfortable with businesses that have hard assets, a multi-year filed tax history and predictable local demand, and most internet businesses have none of those. Some lenders do finance established online businesses with several years of clean, verifiable earnings, particularly larger ecommerce and SaaS deals, but it is not something to assume when you are budgeting. Plan for a Flippa purchase to be cash, and treat any financing you do secure as upside. Seller financing is more commonly available than bank debt on these deals."),
        ("Which marketplace has more listings?",
         "Both carry large inventories, but of completely different things, so the comparison is not meaningful in the abstract. BizBuySell is the dominant listing site for US Main Street businesses and is the first place most brokers post. Flippa carries a very large volume of internet assets ranging from small domains to established stores. What matters more than raw count is inventory in your specific category and price range, and that is worth checking directly before you commit your search to one platform. Both are free to browse."),
        ("Should I use a broker instead of a marketplace?",
         "For Main Street deals you will usually end up dealing with a broker anyway, because most BizBuySell listings are broker-placed. The distinction worth understanding is who they work for: a listing broker represents the seller and is paid on the sale, so their advice is not neutral. A buy-side broker or an acquisition adviser works for you, and can be worth the fee on a larger deal. For online purchases, curated platforms such as Empire Flippers effectively play the broker role themselves. In every case, budget for your own accountant and attorney at closing regardless of who introduced the deal."),
    ],
    "related": [
        ("/acquire/best-websites-to-buy-a-business", "Comparison", "Best Websites to Buy a Business", "All five main marketplaces, Main Street and online."),
        ("/acquire/flippa-vs-empire-flippers", "Comparison", "Flippa vs Empire Flippers", "Open versus curated within the online category."),
        ("/acquire/how-to-buy-a-business-with-an-sba-loan", "Financing", "Buying With an SBA Loan", "How leverage works on Main Street acquisitions."),
        ("/acquire/business-due-diligence-checklist", "Diligence", "Due Diligence Checklist", "The verification that applies whichever platform listed it."),
        ("/acquire/how-to-value-a-business", "Valuation", "How to Value a Business", "Underwrite on verified earnings, not headline multiples."),
    ],
})

# ---------------------------------------------------------------- page 2
PAGES.append({
    "slug": "bizbuysell-review",
    "crumb": "BizBuySell Review",
    "title": "BizBuySell Review (2026): Worth It for Buyers? | WholeSMB",
    "meta": "An honest buyer-side review of BizBuySell: what the inventory is actually like, what the platform does and does not do for you, where the listings mislead, and how to search it properly.",
    "og_title": "BizBuySell Review: Worth It for Buyers?",
    "og_desc": "The biggest Main Street listing site in the US. What it does well, what it does not do at all, and how to use it without wasting six months.",
    "article_desc": "A buyer-side review of BizBuySell covering inventory quality, what the platform does and does not verify, the recurring problems in Main Street listings, and a practical search method for buyers.",
    "h1": "BizBuySell Review: Is It Worth It for Buyers?",
    "intro": """<p>BizBuySell is the default starting point for anyone buying a Main Street business in the United States. It is where most business brokers post first, which means it carries the broadest inventory of restaurants, auto shops, salons, contractors, laundromats and small manufacturers you will find in one place.</p>
      <p>That scale is the whole value proposition, and it is also the whole problem. A marketplace this large is a firehose of listings written by people paid to sell them, on a platform that does not verify what they claim. This review is written from the buyer's side: what BizBuySell genuinely does for you, what it explicitly does not do, the patterns that recur in listings, and how to search it without burning six months.</p>""",
    "verdict_a_title": "What it's good for",
    "verdict_a": "Inventory coverage and market education. Nowhere else shows you as many Main Street businesses at once, and a few weeks of watching listings in one category teaches you what asking prices and multiples actually look like in your area.",
    "verdict_b_title": "What it is not",
    "verdict_b": "It is not a broker, an escrow service, or a verification layer. Nothing in a listing has been checked by the platform. Every number is a seller's claim until your accountant traces it to a tax return.",
    "body": """        <h2>The verdict at a glance</h2>
        <table class="feature-table">
          <thead>
            <tr>
              <th>&nbsp;</th>
              <th>BizBuySell</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>What it is</strong></td>
              <td>A listing marketplace for US Main Street businesses, mostly broker-posted</td>
            </tr>
            <tr>
              <td><strong>Cost to browse</strong></td>
              <td><span class="check">&#10003;</span> Free for buyers; sellers and brokers pay to list</td>
            </tr>
            <tr>
              <td><strong>Inventory breadth</strong></td>
              <td><span class="check">&#10003;</span> The widest single view of the US Main Street market</td>
            </tr>
            <tr>
              <td><strong>Listing verification</strong></td>
              <td><span class="cross">&#10007;</span> None &mdash; the platform hosts claims, it does not audit them</td>
            </tr>
            <tr>
              <td><strong>Represents the buyer</strong></td>
              <td><span class="cross">&#10007;</span> No. The listing broker works for the seller</td>
            </tr>
            <tr>
              <td><strong>Search and alerts</strong></td>
              <td><span class="check">&#10003;</span> Filter by location, industry, price and cash flow; saved-search alerts</td>
            </tr>
            <tr>
              <td><strong>Financing fit</strong></td>
              <td><span class="check">&#10003;</span> Most inventory is the kind of business SBA lenders understand</td>
            </tr>
            <tr>
              <td><strong>Best suited to</strong></td>
              <td>Buyers who want a local, cash-flowing business and will do their own diligence</td>
            </tr>
          </tbody>
        </table>

        <div class="cta-buttons">
          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->
          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">Browse Businesses for Sale &rarr;</a>
        </div>

        <h2>What BizBuySell actually does well</h2>
        <p>Coverage first. If a Main Street business is being marketed in the US, there is a strong chance it appears here, because brokers post where the buyers are and buyers go where the listings are. That network effect is real and it is not easily replicated by a newer competitor.</p>
        <p>Second, and underrated: it is a free education in pricing. Set a saved search for one industry in one metro, watch it for a month, and you will learn more about what businesses in that category actually ask &mdash; and which ones sit unsold at that ask &mdash; than any valuation article will teach you. Buyers who skip this step tend to anchor on the first listing they like. Buyers who do it can tell within thirty seconds whether an asking price is inside the normal band.</p>
        <p>Third, the filters are genuinely useful once you know what to filter on. Location, industry, asking price and reported cash flow all narrow the field quickly, and saved-search alerts mean new inventory finds you rather than the other way round. In a market where good Main Street listings sometimes go under contract quickly, being early matters.</p>

        <h2>What it does not do &mdash; and buyers keep assuming it does</h2>
        <p>The single most important thing to internalise is that BizBuySell is a <strong>classifieds platform, not a broker or a vetting service</strong>. It hosts listings. It does not audit financials, confirm that reported cash flow reconciles to a tax return, or assess whether the add-backs in a seller's discretionary earnings figure are legitimate. When a listing says a business earns a certain amount, that is the seller's claim, relayed by a broker the seller is paying.</p>
        <p>Nor does anyone on the listing side represent you. A listing broker has a fiduciary relationship with the seller and a commission tied to the sale price. They can be professional, helpful and completely honest, and still not be on your side. Budget for your own accountant and your own attorney; on a six-figure acquisition that spend is small relative to what a missed liability costs.</p>
        <p>Finally, the platform is not an escrow or transaction service. Funds, transfer mechanics, licences and lease assignment all sit outside it, handled by your professionals and the closing process.</p>

        <h2>The recurring problems in Main Street listings</h2>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Add-backs doing too much work.</strong> Seller's discretionary earnings is reported profit plus owner salary plus expenses deemed discretionary. Some add-backs are legitimate; others are costs the business will genuinely keep incurring once you own it. Ask for the add-back schedule line by line and challenge each one.</li>
          <li><strong>Owner-dependence dressed up as a strength.</strong> "Owner handles all sales" reads as a growth opportunity in a listing. It usually means the customer relationships walk out with the seller. Ask what happens to revenue if the owner stops answering the phone the day after closing.</li>
          <li><strong>Lease risk buried in the fine print.</strong> For a location-dependent business the lease is the business. A short remaining term, an assignment clause requiring landlord consent, or a rent reset can wipe out the margin you underwrote. Read it before you fall in love with the numbers.</li>
          <li><strong>Cash-heavy accounting.</strong> In some categories sellers hint that reported revenue understates reality. You cannot buy, finance or resell on unreported income, and a lender will not either. Underwrite what is on the returns and treat everything else as zero.</li>
          <li><strong>Stale listings and phantom inventory.</strong> Listings can sit long after a business is under contract or effectively withdrawn. Confirm a listing is live before investing hours in it.</li>
          <li><strong>Vague "confidential" listings.</strong> Confidentiality is normal and appropriate, but at some point after an NDA you need specifics. A broker who still cannot produce financials after signing is a signal, not an obstacle.</li>
        </ul>
        <p>None of this is unique to BizBuySell &mdash; it is what a broker-led Main Street market looks like. The platform is the messenger. Our <a href="/acquire/business-due-diligence-checklist">due diligence checklist</a> is built around exactly these failure modes.</p>

        <h2>How to actually search it</h2>
        <p>The mistake most buyers make is browsing everything, everywhere, in every industry. That produces months of activity and no decisions. A tighter method:</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Pick one or two categories first</strong> and read the playbook for each before you look at a single listing, so you know what normal margins, multiples and risks look like. Start with something like <a href="/acquire/buy-a-laundromat">laundromats</a>, <a href="/acquire/buy-an-auto-repair-shop">auto repair</a>, <a href="/acquire/buy-a-cleaning-business">cleaning</a> or <a href="/acquire/buy-a-hvac-business">HVAC</a>.</li>
          <li><strong>Filter on cash flow, not asking price.</strong> Asking prices are aspirational; reported cash flow at least tells you what the seller is claiming to have earned, which is the number you will verify.</li>
          <li><strong>Set saved-search alerts and check the geo pages</strong> for the markets you would actually move to or operate in &mdash; our state and metro guides cover local conditions, from <a href="/acquire/businesses-for-sale-tx">Texas</a> and <a href="/acquire/businesses-for-sale-fl">Florida</a> to individual metros.</li>
          <li><strong>Get your financing conversation started early.</strong> Talk to an SBA lender before you find a deal, not after. Knowing your realistic price ceiling stops you wasting weeks on listings you cannot fund &mdash; see <a href="/acquire/how-to-buy-a-business-with-an-sba-loan">buying with an SBA loan</a>.</li>
          <li><strong>Expect a high rejection rate and do not fight it.</strong> Most listings should die in the first hour. That is the process working, not the market failing.</li>
        </ul>

        <h2>So, is it worth using?</h2>
        <p>Yes, with the right expectations. If you want a Main Street business in the US, you effectively have to be on it, because that is where the inventory is. It is free to browse and the search tooling does its job. Just do not mistake reach for rigour: the platform gets you in front of listings and does nothing to tell you which are real. That part is yours, and it is where the entire return on an acquisition is decided.</p>
        <p>If you are still deciding between a physical business and an online one, <a href="/acquire/bizbuysell-vs-flippa">BizBuySell vs Flippa</a> is the more useful comparison. If you want the full field of marketplaces, see <a href="/acquire/best-websites-to-buy-a-business">best websites to buy a business</a>, and <a href="/acquire/flippa-vs-empire-flippers">Flippa vs Empire Flippers</a> for the online side.</p>

        <div class="cta-buttons">
          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->
          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">Search Main Street Listings &rarr;</a>
        </div>
""",
    "faqs": [
        ("Is BizBuySell free for buyers?",
         "Browsing and searching are free for buyers. The revenue model sits on the other side of the marketplace: sellers and brokers pay to list and to promote listings. That is worth remembering when you read a listing, because the platform's customer is the person marketing the business, not you. Some listings require you to submit contact details or sign a non-disclosure agreement before financials are released, which is normal practice in Main Street deals, but the platform itself does not charge buyers to look."),
        ("Are BizBuySell listings legitimate?",
         "Most represent real businesses genuinely for sale, and a large share are placed by licensed brokers. But legitimate is not the same as verified. The platform does not audit the financial claims in a listing, so reported cash flow, add-backs and growth claims are the seller's representations relayed by an agent the seller pays. There are also stale listings for businesses already under contract. Treat the listing as an advertisement that tells you a business exists and roughly what is being asked, then verify everything through tax returns, bank statements and the profit and loss with your own accountant."),
        ("What is a good cash flow multiple on BizBuySell?",
         "It varies enormously by industry, size, and how dependent the business is on the current owner, so any single number would be misleading. Smaller owner-operated Main Street businesses generally trade at low multiples of seller's discretionary earnings, and larger businesses with management in place, recurring contracts and clean books command more. The useful exercise is comparative rather than absolute: watch listings in your chosen category and market for several weeks and you will see the band those businesses actually ask within, and which ones sit unsold at the top of it. Then underwrite on your own verified earnings rather than the multiple."),
        ("Do I need a broker if I use BizBuySell?",
         "You will usually be dealing with one, since most listings are broker-placed, but that broker represents the seller. Whether you need your own representation depends on deal size. On a small acquisition, an accountant for quality of earnings and an attorney for the purchase agreement and lease assignment are typically enough. On a larger or more complex deal, a buy-side adviser can be worth the fee. What you should not do is rely on the listing broker for advice about whether the price is fair, because their compensation is tied to the sale closing at that price."),
        ("What is the difference between BizBuySell and BizQuest?",
         "They are both Main Street business-for-sale listing sites and their inventory overlaps heavily, since brokers commonly syndicate the same listing to multiple platforms. BizBuySell is the larger and better-known of the two. For a buyer the practical approach is to set alerts on more than one platform, since it costs nothing, but expect duplicates rather than a materially different market. The more meaningful distinction in this space is between Main Street listing sites generally and online-business marketplaces such as Flippa or Empire Flippers, which sell an entirely different asset class."),
    ],
    "related": [
        ("/acquire/bizbuysell-vs-flippa", "Comparison", "BizBuySell vs Flippa", "Main Street versus online, side by side."),
        ("/acquire/best-websites-to-buy-a-business", "Comparison", "Best Websites to Buy a Business", "All five main marketplaces compared."),
        ("/acquire/business-due-diligence-checklist", "Diligence", "Due Diligence Checklist", "Built around the failure modes in Main Street listings."),
        ("/acquire/how-to-buy-a-business-with-an-sba-loan", "Financing", "Buying With an SBA Loan", "Get the financing conversation started before you search."),
        ("/acquire/how-to-value-a-business", "Valuation", "How to Value a Business", "Turning a claimed cash flow figure into a defensible price."),
    ],
})


if __name__ == "__main__":
    for p in PAGES:
        path = os.path.join(OUT, p["slug"] + ".html")
        with open(path, "w") as f:
            f.write(build(p))
        print("wrote", path)
