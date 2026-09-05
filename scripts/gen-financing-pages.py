#!/usr/bin/env python3
"""Generate the /acquire/ acquisition-financing page family.

Same skeleton as the deal-structure batch (asset-vs-stock / LOI / purchase
agreement): BreadcrumbList + Article + FAQPage JSON-LD, clean-URL canonical,
affiliate disclosure line, CTAs with rel="nofollow sponsored" target="_blank"
behind <!-- AFFILIATE: --> swap comments.

Token substitution uses {{TOKEN}} + str.replace so the inline JSON-LD braces
survive untouched.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "acquire")
DATE = "2026-08-08"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{{TITLE}}</title>
  <meta name="description" content="{{DESC}}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://wholesmb.com/acquire/{{SLUG}}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{{OG_TITLE}}">
  <meta property="og:description" content="{{SHORT_DESC}}">
  <meta property="og:url" content="https://wholesmb.com/acquire/{{SLUG}}">
  <meta property="og:site_name" content="WholeSMB">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{OG_TITLE}}">
  <meta name="twitter:description" content="{{SHORT_DESC}}">

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
  {{BREADCRUMB_JSON}}
  </script>

  <!-- Schema: Article -->
  <script type="application/ld+json">
  {{ARTICLE_JSON}}
  </script>

  <!-- Schema: FAQPage -->
  <script type="application/ld+json">
  {{FAQ_JSON}}
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
      {{CRUMB}}
    </div>
  </div>

  <!-- ===== Page Header ===== -->
  <section class="page-header" style="padding-top:24px">
    <div class="container">
      <h1>{{H1}}</h1>
      {{INTRO}}
      <p style="font-size:.813rem;color:var(--color-text-light);margin-top:8px">
        &#8505; <em>This page may contain affiliate links. See our <a href="/disclosure.html">disclosure</a>. This is general education, not legal, tax, or financial advice &mdash; loan programs and their rules change, so confirm current terms with your lender and advisors before you commit.</em>
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
            <h3>{{VERDICT_A_H}}</h3>
            <p>{{VERDICT_A_P}}</p>
          </div>
          <div class="verdict-col">
            <h3>{{VERDICT_B_H}}</h3>
            <p>{{VERDICT_B_P}}</p>
          </div>
        </div>
      </div>

      <div class="content-body" style="max-width:100%">

{{BODY}}

        <!-- FAQ -->
        <div class="faq-section">
          <h2>Frequently Asked Questions</h2>
{{FAQ_HTML}}
        </div>

        <!-- Related -->
        <h2>Related Guides</h2>
        <div class="comparisons-grid" style="margin-top:20px">
{{RELATED}}
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
          <li><a href="/acquire/best-websites-to-buy-a-business">Best Websites to Buy a Business</a></li>
          <li><a href="/acquire/bizbuysell-vs-flippa">BizBuySell vs Flippa</a></li>
          <li><a href="/acquire/how-to-buy-a-business">How to Buy a Business</a></li>
          <li><a href="/acquire/how-to-buy-a-business-with-an-sba-loan">Buy With an SBA Loan</a></li>
          <li><a href="/acquire/businesses-for-sale-nj">Businesses for Sale by State</a></li>
          <li><a href="/acquire/businesses-for-sale-online">Online Businesses for Sale</a></li>
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

CTA_LENDER = """        <div class="cta-buttons">
          <!-- AFFILIATE: replace with Lendio (FlexOffers) affiliate link once approved -->
          <a href="https://www.lendio.com/business-loans/sba-loans/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">Compare Acquisition Lenders &rarr;</a>
          <!-- AFFILIATE: replace with BizBuySell affiliate link once approved -->
          <a href="https://www.bizbuysell.com/businesses-for-sale/" class="btn btn-outline btn-lg" rel="nofollow sponsored" target="_blank">Browse Businesses for Sale &rarr;</a>
        </div>
"""

CTA_MARKET = """        <div class="cta-buttons">
          <!-- AFFILIATE: replace with Empire Flippers affiliate link once approved -->
          <a href="https://empireflippers.com/marketplace/" class="btn btn-primary btn-lg" rel="nofollow sponsored" target="_blank">See Vetted Online Businesses &rarr;</a>
          <!-- AFFILIATE: replace with Flippa affiliate link once approved -->
          <a href="https://flippa.com/search" class="btn btn-outline btn-lg" rel="nofollow sponsored" target="_blank">Browse Listings on Flippa &rarr;</a>
        </div>
"""

RELATED_CARDS = {
    "sba": ('/acquire/how-to-buy-a-business-with-an-sba-loan', 'Financing', 'Buy With an SBA Loan',
            '7(a) down payment rules, standby seller notes, underwriting, and the real 60&ndash;90 day timeline.'),
    "seller": ('/acquire/seller-financing-business-purchase', 'Financing', 'Seller Financing Explained',
               'Typical note terms, SBA standby rules, and the buyer protections worth negotiating.'),
    "nomoney": ('/acquire/how-to-buy-a-business-with-no-money', 'Financing', 'Buy With No Money Down',
                'The six low-cash structures that actually close &mdash; and the three that never do.'),
    "downpay": ('/acquire/sba-loan-down-payment', 'Financing', 'SBA Loan Down Payment',
                'How much cash you really need, and the seller-note trick that halves it.'),
    "acqloan": ('/acquire/business-acquisition-loan', 'Financing', 'Business Acquisition Loans',
                'SBA 7(a), conventional, seller notes, and search-fund debt compared side by side.'),
    "robs": ('/acquire/use-401k-to-buy-a-business', 'Financing', 'Use a 401(k) to Buy a Business',
             'How a ROBS rollover works, what it costs, and the compliance load it creates.'),
    "value": ('/acquire/how-to-value-a-business', 'Valuation', 'How to Value a Business',
              'SDE and EBITDA multiples and a defensible price range.'),
    "dd": ('/acquire/business-due-diligence-checklist', 'Diligence', 'Due Diligence Checklist',
           'What to request and what each document is actually testing.'),
    "loi": ('/acquire/letter-of-intent-to-buy-a-business', 'Deal Docs', 'Letter of Intent',
            'What an LOI locks in, and the clauses buyers regret skipping.'),
    "struct": ('/acquire/asset-purchase-vs-stock-purchase', 'Deal Docs', 'Asset vs Stock Purchase',
               'Liability, tax basis, contract assignment, and licensing.'),
    "howto": ('/acquire/how-to-buy-a-business', 'Guide', 'How to Buy a Business',
              'The full process from search through closing, step by step.'),
}


def faq_html(faqs):
    out = []
    for q, a in faqs:
        out.append(
            '          <div class="faq-item">\n'
            f'            <h3>{q}</h3>\n'
            f'            <p>{a}</p>\n'
            '          </div>'
        )
    return "\n".join(out)


def faq_json(faqs):
    import re
    def plain(s):
        s = re.sub(r'<[^>]+>', '', s)
        return (s.replace('&mdash;', '—').replace('&ndash;', '–')
                 .replace('&rsquo;', '’').replace('&amp;', '&').replace('&nbsp;', ' '))
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": plain(q),
             "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
            for q, a in faqs
        ],
    }, indent=2, ensure_ascii=False)


def related_html(keys):
    out = []
    for k in keys:
        href, badge, title, blurb = RELATED_CARDS[k]
        out.append(
            f'          <a href="{href}" class="comparison-card">\n'
            f'            <span class="comparison-card-badge">{badge}</span>\n'
            f'            <h3>{title}</h3>\n'
            f'            <p>{blurb}</p>\n'
            '          </a>'
        )
    return "\n".join(out)


def build(page):
    breadcrumb = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://wholesmb.com/"},
            {"@type": "ListItem", "position": 2, "name": "Buy a Business", "item": "https://wholesmb.com/acquire"},
            {"@type": "ListItem", "position": 3, "name": page["crumb"]},
        ],
    }, indent=2, ensure_ascii=False)

    article = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": page["title"].split(" | ")[0],
        "description": page["desc"],
        "author": {"@type": "Organization", "name": "WholeSMB editorial team"},
        "publisher": {"@type": "Organization", "name": "WholeSMB", "url": "https://wholesmb.com"},
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": f"https://wholesmb.com/acquire/{page['slug']}",
    }, indent=2, ensure_ascii=False)

    html = TEMPLATE
    for token, value in [
        ("{{TITLE}}", page["title"]),
        ("{{DESC}}", page["desc"]),
        ("{{SHORT_DESC}}", page["short_desc"]),
        ("{{OG_TITLE}}", page["og_title"]),
        ("{{SLUG}}", page["slug"]),
        ("{{CRUMB}}", page["crumb"]),
        ("{{H1}}", page["h1"]),
        ("{{INTRO}}", page["intro"]),
        ("{{VERDICT_A_H}}", page["verdict"][0]),
        ("{{VERDICT_A_P}}", page["verdict"][1]),
        ("{{VERDICT_B_H}}", page["verdict"][2]),
        ("{{VERDICT_B_P}}", page["verdict"][3]),
        ("{{BODY}}", page["body"]),
        ("{{BREADCRUMB_JSON}}", breadcrumb),
        ("{{ARTICLE_JSON}}", article),
        ("{{FAQ_JSON}}", faq_json(page["faqs"])),
        ("{{FAQ_HTML}}", faq_html(page["faqs"])),
        ("{{RELATED}}", related_html(page["related"])),
    ]:
        html = html.replace(token, value)

    path = os.path.join(OUT, page["slug"] + ".html")
    with open(path, "w") as fh:
        fh.write(html)
    words = len(page["body"].split()) + len(page["intro"].split())
    print(f"wrote {path} (~{words} body words)")


# ---------------------------------------------------------------- page 1
P1 = {
    "slug": "sba-loan-down-payment",
    "crumb": "SBA Loan Down Payment",
    "h1": "SBA Loan Down Payment to Buy a Business",
    "title": "SBA Loan Down Payment (2026): How Much Cash Do You Really Need? | WholeSMB",
    "desc": "How much down payment an SBA 7(a) business acquisition really requires, how a standby seller note can cover part of it, which sources of cash count as a qualifying equity injection, and the closing costs buyers forget to budget for.",
    "short_desc": "The 10% rule, the seller-note carve-out, and the cash buyers forget to budget.",
    "og_title": "SBA Loan Down Payment: How Much Cash a Buyer Actually Needs",
    "verdict": (
        "Budget 10% of the total project cost&hellip;",
        "SBA rules require a minimum 10% equity injection on a change-of-ownership 7(a) loan, measured against total project cost &mdash; purchase price plus working capital, closing costs, and any fees rolled into the loan. On a $1,000,000 project that is $100,000 before you have bought a single week of runway.",
        "&hellip;but only half of it has to be your own cash",
        "Up to half of the required injection can come from a seller note on full standby for the life of the loan. That can take a $100,000 requirement down to $50,000 of buyer cash &mdash; if the seller will accept it and your lender allows it. Individual lenders routinely require more than the SBA floor.",
    ),
    "intro": """      <p>The most common reason a promising acquisition dies is not valuation and not diligence. It is that the buyer discovers, four weeks in, that the cash required at closing is roughly double what they had planned for. The headline number &mdash; "SBA loans only need 10% down" &mdash; is true and also incomplete, because the 10% is measured against the whole project rather than the purchase price, because your lender is free to want more than the SBA's floor, and because the equity injection is not the only cash you have to show up with.</p>
      <p>This page walks through what the down payment requirement actually is on a 7(a) change-of-ownership loan, which sources of money count toward it, the standby seller note that can cut your cash in half, and the additional closing costs that belong in your budget from day one.</p>""",
    "faqs": [
        ("How much down payment do you need for an SBA loan to buy a business?",
         "SBA rules set a minimum equity injection of 10% of total project cost on a complete change of ownership under the 7(a) program. Total project cost includes the purchase price plus working capital, closing costs, and any fees financed into the loan, so the dollar figure is normally larger than 10% of the sticker price. Lenders may and often do require more than the 10% floor based on the industry, the buyer's experience, and the strength of the cash flow."),
        ("Can a seller note count as the down payment?",
         "Partly. Up to half of the required equity injection can be satisfied by a seller note, but only if that note is on full standby &mdash; no principal and no interest paid to the seller &mdash; for the entire term of the SBA loan. A note that starts paying in year three is not on full standby and does not count toward the injection, though it can still be part of the capital stack."),
        ("Can you borrow the SBA down payment?",
         "Not from a loan you have to repay out of the business. The injection has to be genuine equity, so a personal loan serviced by business cash flow will be rejected. A home equity line of credit is sometimes accepted when you can document that you can service it from income outside the business, and a gift from a family member is accepted with a signed gift letter confirming there is no repayment obligation."),
        ("What sources of cash count as an equity injection?",
         "Personal savings and taxable brokerage accounts, retirement funds you have properly withdrawn or rolled over, documented gifts, proceeds from selling an asset such as a property or vehicle, cash from an investor taking equity in the buying entity, and a fully standby seller note for up to half the requirement. Everything must be seasoned and traceable, which in practice means two to three months of statements showing where it came from."),
        ("How much total cash should a buyer have at closing?",
         "Plan on the equity injection plus roughly 3% to 5% of the loan amount in closing costs &mdash; the SBA guaranty fee, lender packaging fee, appraisal or business valuation, legal fees, lien searches, and title work &mdash; plus post-closing working capital. Many lenders will finance the closing costs and some working capital into the loan, which raises the project cost and therefore raises the injection, so run the math both ways before you choose."),
    ],
    "related": ["sba", "acqloan", "robs", "seller", "nomoney", "value"],
    "body": """        <h2>The 10% rule, stated precisely</h2>
        <p>For a 7(a) loan financing a complete change of ownership, the SBA requires a minimum equity injection of 10% of the total project cost. Two details in that sentence do most of the damage to buyer budgets.</p>
        <p>First, <strong>total project cost</strong> is not the purchase price. It is everything the loan is funding: the price of the business, the working capital you are borrowing to run it, the closing costs you roll in, and the SBA guaranty fee itself. A $900,000 purchase with $60,000 of working capital and $40,000 of financed costs is a $1,000,000 project, and the injection is measured on the million.</p>
        <p>Second, <strong>10% is a floor, not a target</strong>. The SBA sets the minimum; your lender sets its own credit policy on top of it. It is entirely normal for a bank to want 15% from a first-time owner buying into an industry they have never worked in, or from a business whose cash flow only barely clears the debt service coverage test. Ask the lender for their required injection early, in writing, and treat the SBA's number as trivia until you do.</p>

""" + CTA_LENDER + """
        <h2>The standby seller note &mdash; the single biggest lever</h2>
        <p>The rule that matters most to a cash-constrained buyer: up to half of the required equity injection may be met with a seller note, provided the note is on <strong>full standby for the life of the SBA loan</strong>. Full standby means the seller receives nothing at all &mdash; no principal, no interest &mdash; until the SBA debt is retired. Interest may accrue, but it cannot be paid.</p>
        <p>On a $1,000,000 project the arithmetic is stark. A $100,000 injection funded entirely by you is $100,000 out of your account. A $100,000 injection funded half by a standby seller note is $50,000 out of your account and a $50,000 note the seller cannot touch for ten years.</p>
        <p>Two cautions. A note that pays interest from month one, or that begins amortizing in year three, is <em>not</em> on full standby and does not reduce your injection requirement &mdash; it is simply additional debt in the stack, which the lender will fold into your coverage calculation. And a seller who agrees to a decade of silence on half their proceeds is a seller who will want something in return, usually price. Our <a href="/acquire/seller-financing-business-purchase">seller financing guide</a> covers how those notes are typically structured and the offset rights worth negotiating.</p>

        <h2>Which sources of cash actually count</h2>
        <p>Underwriters do not just want to see a balance. They want to see where it came from and that it is yours to spend.</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Personal savings and brokerage accounts.</strong> The cleanest source. Expect to provide two to three months of statements so the lender can confirm the funds are seasoned rather than borrowed last week.</li>
          <li><strong>Retirement funds.</strong> Usable either by taking a distribution &mdash; with the tax and penalty consequences that implies &mdash; or through a <a href="/acquire/use-401k-to-buy-a-business">ROBS rollover</a> that capitalizes the buying entity without triggering tax.</li>
          <li><strong>Gifts.</strong> Accepted with a signed gift letter stating explicitly that repayment is not expected. If it is really a loan, saying otherwise on a federally guaranteed application is not a corner worth cutting.</li>
          <li><strong>Asset sales.</strong> Selling a rental property, a vehicle, or a stake in another business works; keep the closing statement and the deposit trail.</li>
          <li><strong>Investor equity.</strong> An outside investor can fund the injection in exchange for ownership in the buying entity. Note that owners above a threshold ownership stake are generally required to guarantee the loan, so an investor with a meaningful position may need to sign personally &mdash; a conversation to have before you promise them a passive role.</li>
          <li><strong>A fully standby seller note</strong>, for up to half the requirement, as above.</li>
        </ul>
        <p>What does <em>not</em> count: a personal loan or credit line that will be serviced out of the business, because that is debt wearing an equity costume, and the whole point of the injection is that it absorbs loss before the guaranteed lender does. A HELOC sometimes passes when you can document outside income sufficient to service it independently, but treat that as a lender-by-lender question rather than a rule.</p>

""" + CTA_MARKET + """
        <h2>The cash nobody budgets for</h2>
        <p>The injection is the number buyers fixate on. It is not the number that determines whether you can close.</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>SBA guaranty fee.</strong> A percentage of the guaranteed portion, scaled by loan size and term. It is real money on a seven-figure loan and it is frequently financed &mdash; which increases the project cost and therefore the injection.</li>
          <li><strong>Lender packaging and closing fees</strong>, plus lien searches, UCC filings, and title work if real estate is involved.</li>
          <li><strong>Business valuation.</strong> Required by the SBA on change-of-ownership loans above a size threshold, and paid by you regardless of whether the deal closes.</li>
          <li><strong>Your attorney.</strong> A transaction attorney reviewing the purchase agreement, lease assignment, and loan documents is the least regrettable spend in the process.</li>
          <li><strong>Post-closing working capital.</strong> Payroll runs before your first collections do. If you are not financing working capital into the loan, it comes from the same account as the injection, and this is where deals quietly become fragile.</li>
        </ul>
        <p>A defensible rule of thumb: injection, plus 3% to 5% of the loan amount in closing costs, plus one to three months of operating expenses in reserve. If that total is more than you have, the answer is a smaller business rather than a thinner cushion.</p>

        <h2>A worked example</h2>
        <p>Suppose a business is listed at $850,000 and you and the seller agree on the price. You want $75,000 of working capital, and closing costs and the guaranty fee come to about $45,000, financed. Total project cost: $970,000. The SBA minimum injection at 10% is $97,000.</p>
        <p>If you fund all of it yourself, you need $97,000 of equity plus whatever costs are not financed plus a reserve. If the seller agrees to a $48,500 note on full standby, your cash injection drops to $48,500 &mdash; and you still want that reserve, because a standby note does not pay your first payroll.</p>
        <p>Now assume the lender's own policy requires 15% rather than 10% because you have not operated in the industry. The injection becomes $145,500, the seller-note half becomes $72,750, and your cash requirement is back near $73,000. Same business, same price, different bank. This is why the lender conversation belongs before the <a href="/acquire/letter-of-intent-to-buy-a-business">letter of intent</a>, not after it.</p>

        <h2>How to lower the cash requirement honestly</h2>
        <p>There are legitimate levers and there are fictions. The legitimate ones: negotiate a full-standby seller note for half the injection; shop at least three SBA lenders, because injection policy varies more than rate does; buy a business whose working capital cycle collects fast enough that you can borrow less of it; and consider a slightly smaller target, since the injection scales with the project. The fictions: a "loan" from a relative that everybody understands will be repaid, a personal line you intend to service from the business, or a seller note dressed as standby with a side agreement. Misrepresenting the source of an equity injection on an SBA application is fraud, and it is the kind that surfaces later, when the business is already yours and the loan is already in default.</p>
        <p>If the cash simply is not there yet, the honest paths are documented in our guide to <a href="/acquire/how-to-buy-a-business-with-no-money">buying a business with little or no money down</a> &mdash; most of which come down to a motivated seller, a smaller deal, or a partner. And before you commit to any structure, run the target through a <a href="/acquire/business-due-diligence-checklist">due diligence checklist</a>: the fastest way to lose an injection is to buy a business whose earnings were never what the listing claimed.</p>
""",
}

# ---------------------------------------------------------------- page 2
P2 = {
    "slug": "business-acquisition-loan",
    "crumb": "Business Acquisition Loans",
    "h1": "Business Acquisition Loans: The Five Ways Buyers Fund a Deal",
    "title": "Business Acquisition Loan (2026): SBA vs Conventional vs Seller Financing | WholeSMB",
    "desc": "A comparison of the five ways small-business buyers finance an acquisition &mdash; SBA 7(a), conventional bank debt, seller notes, unsecured and online lenders, and investor equity &mdash; with the terms, tradeoffs, and qualification tests for each.",
    "short_desc": "SBA 7(a), conventional debt, seller notes, online lenders, and equity &mdash; compared.",
    "og_title": "Business Acquisition Loans Compared: SBA, Conventional, Seller, Equity",
    "verdict": (
        "For most Main Street deals, SBA 7(a) wins",
        "Ten-year amortization on a goodwill-heavy business, a 10% minimum injection, and no balloon. Nothing else in the market lends against intangible value on those terms. The cost is a longer timeline, a personal guarantee, and a document load that makes buyers miserable.",
        "The capital stack usually beats a single source",
        "The deals that close on the least buyer cash are almost never one loan. They are an SBA note plus a standby seller note plus a small earnout &mdash; each piece doing what it is best at. Design the stack before you name a price, not after.",
    ),
    "intro": """      <p>"Business acquisition loan" is not one product. It is a category containing at least five genuinely different instruments, each with its own qualification test, price, and failure mode. Buyers who treat them as interchangeable tend to spend three months in the wrong process and then discover their deal was never fundable on that path.</p>
      <p>This page lays out the five real options for financing the purchase of an operating small business, what each one will and will not lend against, roughly what it costs, and how experienced buyers stack them together to close on less cash than any single source would allow.</p>""",
    "faqs": [
        ("What is a business acquisition loan?",
         "It is financing used to buy an existing operating business rather than to fund working capital in one you already own. The main forms are SBA 7(a) loans, conventional bank term loans, seller notes carried by the departing owner, unsecured or online term debt, and investor equity in the buying entity. Most closed deals use two or three of these together rather than one alone."),
        ("Is it hard to get a loan to buy a business?",
         "It is harder than getting a mortgage and easier than raising venture capital. Lenders underwrite three things: whether the business's historical cash flow covers the new debt with a margin, usually expressed as a debt service coverage ratio of at least 1.15 to 1.25; whether the buyer has relevant management experience and clean personal credit; and whether there is collateral or a guarantee behind the loan. A profitable, well-documented business with an experienced buyer is a routine approval. Weakness in any of the three is where deals stall."),
        ("How long does an SBA acquisition loan take to close?",
         "Sixty to ninety days from a complete application is the realistic range, and that clock starts after you have a signed letter of intent and three years of the seller's tax returns and financials in hand. Preferred Lender Program banks can move faster because they approve in-house rather than sending the file to the SBA. Deals with real estate, liquor licenses, or franchise agreements should assume the long end."),
        ("Can you get an acquisition loan with no collateral?",
         "Under the SBA 7(a) program, a loan is not declined for collateral shortfall alone if the cash flow supports it &mdash; the lender takes what collateral exists, typically including a lien on your home if you have meaningful equity, and proceeds. Conventional bank lending is far less forgiving: banks lend against assets, so a service business whose value is almost entirely goodwill is usually not a conventional deal at any price."),
        ("What credit score do you need to buy a business?",
         "Most SBA lenders look for a personal credit score in the high 600s at minimum, with 700 and above making the file comfortable. Score is a screen rather than the decision. Underwriters care more about the business's debt service coverage, your management experience in the industry, and the size of your equity injection, and a strong file on those three can survive a merely acceptable score."),
    ],
    "related": ["sba", "downpay", "seller", "nomoney", "robs", "value"],
    "body": """        <h2>1. SBA 7(a) &mdash; the default for Main Street</h2>
        <p>The 7(a) program is the reason ordinary buyers can purchase profitable service businesses at all. A conventional bank lends against assets; a 7(a) lender, with a federal guaranty behind part of the loan, will lend against <em>cash flow</em>, which is what a business made mostly of goodwill actually has.</p>
        <p>What it looks like in practice: up to $5 million, ten-year amortization for a business acquisition without real estate (longer when significant real estate is included), no balloon payment, a variable rate typically pegged to prime plus a spread, a minimum 10% equity injection, and a personal guarantee from every owner above the ownership threshold. There is a guaranty fee that scales with loan size and term, and it is usually financed.</p>
        <p>What it costs you that is not money: time and paperwork. Sixty to ninety days from a complete file is normal. You will produce three years of the seller's returns, interim financials, a business valuation, a lease or lease assignment, your personal financial statement, and a business plan with projections. The <a href="/acquire/how-to-buy-a-business-with-an-sba-loan">full 7(a) walkthrough</a> covers the underwriting tests in detail; the <a href="/acquire/sba-loan-down-payment">down payment page</a> covers how much cash you actually need to produce.</p>
        <p>Use it when: the target is a profitable operating business with two or three years of documented earnings and the value sits in goodwill, customer relationships, or contracts rather than equipment.</p>

""" + CTA_LENDER + """
        <h2>2. Conventional bank term debt</h2>
        <p>A straight commercial loan from a bank, with no federal guaranty. Faster than SBA, cheaper in fees, often a lower rate, and frequently a shorter amortization &mdash; five to seven years is common &mdash; sometimes with a balloon.</p>
        <p>The catch is what the bank will lend against. Without a guaranty absorbing part of the loss, a bank wants collateral coverage. That works for a manufacturer with machinery, a trucking company with a titled fleet, or any acquisition that includes real estate. It works poorly for an agency, a services firm, or a route business whose balance sheet is thin, because the bank is being asked to lend against something it cannot repossess.</p>
        <p>The shorter amortization also compresses coverage. The same purchase price over seven years instead of ten means a materially larger annual payment, and a business that clears a 1.25 coverage ratio on a ten-year SBA note can fail it on a seven-year conventional one. Run the coverage math on the actual term before you assume the cheaper loan is the better loan.</p>
        <p>Use it when: there are hard assets or real estate in the deal, your relationship bank already knows you, and the cash flow has enough headroom for a shorter schedule.</p>

        <h2>3. Seller financing</h2>
        <p>The seller carries a note for part of the price and you pay them over time. This is the most underrated instrument in small-business acquisition, for three reasons: it is available on almost every deal, it costs nothing to originate, and it is the only form of financing that makes the seller's ongoing cooperation a matter of self-interest.</p>
        <p>Typical structures run from 10% to 30% of the price at rates in the neighborhood of prime, amortized over three to seven years, sometimes with a standby period. Inside an SBA deal there are two distinct roles a seller note can play: on <strong>full standby</strong> for the life of the SBA loan, it can count toward up to half of your required equity injection; on partial standby or normal amortization, it does not count toward the injection but still reduces the amount of bank debt you need. Our <a href="/acquire/seller-financing-business-purchase">seller financing page</a> covers the terms in detail, including the right of offset that lets you reduce note payments if the seller's representations turn out to be false.</p>
        <p>Use it when: always ask. A seller unwilling to carry any paper is telling you something about their confidence in the business, and that information is worth the awkward question.</p>

        <h2>4. Unsecured, online, and revenue-based lenders</h2>
        <p>Fast money at a real price. Online term lenders and revenue-based financiers can fund in days rather than months, with light documentation, but the effective cost is far above bank pricing and terms are short &mdash; often 6 to 24 months, sometimes with daily or weekly debits rather than monthly payments.</p>
        <p>As the primary financing for an acquisition, this is almost always a mistake: the payment schedule is designed for a merchant smoothing receivables, not for a buyer absorbing an ownership transition. As a small, deliberate slice &mdash; funding an equipment repair discovered in diligence, or bridging a working capital gap in month two &mdash; it can be defensible. Be aware that an SBA lender will scrutinize any other debt in the buying entity, and taking on a high-cost line during underwriting can damage your coverage ratio and your credibility at once.</p>
        <p>Use it when: small, short, and specific. Never as the foundation of the stack.</p>

""" + CTA_MARKET + """
        <h2>5. Investor equity and search-fund style capital</h2>
        <p>Rather than borrowing the gap, sell part of it. An investor funds some or all of the equity injection in exchange for ownership in the buying entity. This is the standard model for search funds and it appears constantly in independent acquisitions dressed as a "partner."</p>
        <p>The advantages are real: no payment obligation, no personal exposure on that slice, and often an experienced partner who has done this before. The costs are equally real. You are giving away a permanent share of the upside on the thing you are about to spend five years building, governance gets complicated, and &mdash; the detail buyers miss &mdash; an investor whose stake crosses the ownership threshold will generally be required to personally guarantee the SBA loan. Investors who expected to be passive frequently decline at that point, which is why the guarantee question belongs in the first conversation.</p>
        <p>Use it when: the deal is bigger than your cash, the business genuinely benefits from the partner's expertise, and you would rather own less of something good than all of something small.</p>

        <h2>Stacking: how deals actually close</h2>
        <p>Almost no acquisition of consequence is financed by one instrument. The common shape on a Main Street deal is roughly 80% SBA 7(a), 10% standby seller note counting toward the injection, and 10% buyer cash &mdash; occasionally with a modest earnout tied to retention of a concentrated customer.</p>
        <p>Each piece is doing something the others cannot. The SBA note supplies long amortization against goodwill. The standby seller note supplies cheap capital and keeps the seller invested in a clean handoff. The earnout moves the risk of a specific uncertainty onto the party who knows the answer. Buyer cash supplies the lender's proof that you have something to lose.</p>
        <p>Design the stack before you negotiate the price, because the structure and the price are the same conversation. A seller who will not carry paper is effectively asking for a lower number, and a seller who will carry a decade of standby paper has earned a higher one.</p>

        <h2>What underwriters are actually testing</h2>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Debt service coverage.</strong> Adjusted historical cash flow divided by total new annual debt service, with lenders typically wanting 1.15 to 1.25 or better. Note that the coverage test uses <em>historical</em> earnings, not your projections &mdash; an optimistic plan does not fix a business that cannot cover the note today.</li>
          <li><strong>Owner compensation.</strong> The lender subtracts a reasonable salary for you before testing coverage. Buyers modelling their deal without that deduction routinely overestimate how much debt the business supports.</li>
          <li><strong>Management experience.</strong> Direct industry experience is the strongest form. Adjacent operating experience plus a retained key manager is often enough. No relevant experience at all is where injections get raised.</li>
          <li><strong>The quality of the seller's books.</strong> Cash-basis records, unexplained add-backs, and revenue concentrated in two customers all reduce what a lender will advance &mdash; and all show up in a <a href="/acquire/business-due-diligence-checklist">proper diligence process</a> before they show up in a declination letter.</li>
          <li><strong>The lease.</strong> On a location-dependent business, lenders generally want the lease term (including options) to run at least as long as the loan. An unassignable or short lease can stop an otherwise clean file.</li>
        </ul>

        <h2>Sequence that saves you a month</h2>
        <p>Get pre-qualified before you write an offer. Bring a lender a rough profile of what you are looking for and your personal financial statement, and get their injection policy and coverage requirements in writing. Then when a target appears, you already know whether it is fundable and on what terms &mdash; and your <a href="/acquire/letter-of-intent-to-buy-a-business">letter of intent</a> can specify a structure the bank has already told you it will accept. Buyers who reverse that order spend their exclusivity period discovering that the deal they signed cannot be financed the way they promised.</p>
""",
}

# ---------------------------------------------------------------- page 3
P3 = {
    "slug": "use-401k-to-buy-a-business",
    "crumb": "Use a 401(k) to Buy a Business",
    "h1": "Using a 401(k) to Buy a Business (ROBS Explained)",
    "title": "Use a 401(k) to Buy a Business (2026): How ROBS Works and What It Costs | WholeSMB",
    "desc": "How a Rollover for Business Startups (ROBS) lets you fund a business purchase with retirement savings without tax or penalty, the five-step mechanics, the real costs, the ongoing compliance load, and when a distribution or a 401(k) loan is the better answer.",
    "short_desc": "ROBS mechanics, real costs, compliance load, and the safer alternatives.",
    "og_title": "Using a 401(k) to Buy a Business: How ROBS Actually Works",
    "verdict": (
        "ROBS works &mdash; and it is genuinely risky",
        "A Rollover for Business Startups moves retirement money into a business purchase without a distribution, so no income tax and no early-withdrawal penalty. It is a real, established structure. It also puts your retirement savings and your income behind the same single business, and it creates a permanent compliance obligation.",
        "Consider the smaller tools first",
        "A 401(k) loan from a current employer's plan &mdash; capped, repaid with interest to yourself, no new corporate structure &mdash; solves a modest gap far more cheaply. If you only need to top up an SBA equity injection rather than fund the whole purchase, start there.",
    ),
    "intro": """      <p>Most first-time buyers of a small business have more money in a 401(k) or IRA than they have in cash. The obvious question follows: can that money buy the business? The answer is yes, through a structure called a Rollover for Business Startups &mdash; ROBS &mdash; that moves retirement funds into the company without triggering income tax or the early-withdrawal penalty.</p>
      <p>It is legal, it has been in use for decades, and it is also the most consequential financing decision on this site. A ROBS concentrates your retirement savings and your livelihood into one illiquid asset and adds a permanent compliance obligation on top. This page explains the mechanics honestly, prices it, lays out the ongoing requirements, and covers the two simpler alternatives most buyers should rule out first.</p>""",
    "faqs": [
        ("Can I use my 401(k) to buy a business without paying a penalty?",
         "Yes, through a ROBS structure. You form a C corporation, the corporation sponsors a new retirement plan, you roll your existing 401(k) or IRA into that plan, and the plan purchases stock in the corporation. Because the money moves between qualified plans rather than being distributed to you, there is no income tax and no early-withdrawal penalty. The corporation then uses the proceeds to buy the business."),
        ("What does a ROBS cost?",
         "Expect roughly $4,000 to $6,000 in setup fees to a ROBS provider, plus ongoing administration of around $130 to $200 per month for plan recordkeeping and compliance. On top of that are the costs of running a C corporation: a separate corporate tax return every year, and an annual Form 5500 filing for the plan once it crosses the reporting threshold. Budget for a business valuation as well, since the plan's stock purchase should be supported by one."),
        ("Is ROBS legal?",
         "Yes. The IRS has acknowledged the structure and it has been used for decades, but the agency has also run a dedicated compliance project on it because a meaningful share of ROBS companies fall out of compliance. Legality depends on continuing to satisfy the requirements: a real C corporation, a qualified plan that is genuinely offered to eligible employees, reasonable compensation, no prohibited transactions, and the required annual filings."),
        ("Can I pay myself a salary from a ROBS-funded business?",
         "Yes, and you generally should &mdash; you must be a bona fide employee of the corporation for the structure to hold, and reasonable W-2 compensation is part of that. What you cannot do is take money out in ways that amount to using plan assets for personal benefit, such as unsecured loans to yourself, rent paid to an entity you own on non-market terms, or compensation so far above market that it is effectively a distribution of the plan's investment."),
        ("Is it better to use a 401(k) loan instead?",
         "For smaller amounts, usually yes. A loan from a current employer's plan is capped at the lesser of $50,000 or half your vested balance, is repaid with interest to your own account, and requires no new corporate structure, no C corporation tax return, and no plan administration. Its weaknesses are the cap, the fact that most former-employer plans do not permit loans, and that leaving the job can accelerate repayment. If your gap is a partial SBA equity injection, the loan is the cheaper tool; if you are funding an entire purchase, only ROBS reaches that scale."),
    ],
    "related": ["downpay", "sba", "nomoney", "seller", "acqloan", "howto"],
    "body": """        <h2>What ROBS actually is</h2>
        <p>A Rollover for Business Startups is not a loan and not a withdrawal. It is a sequence of legitimate transactions that ends with your retirement plan owning stock in a corporation that owns a business. Because the money never passes to you personally, there is no taxable distribution and no 10% early-withdrawal penalty.</p>
        <p>The five steps, in order:</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Form a C corporation.</strong> The structure requires a C corp specifically, because the plan has to be able to hold qualifying employer securities. An LLC or S corporation will not work &mdash; an S corp cannot have a retirement plan as a shareholder.</li>
          <li><strong>The corporation adopts a retirement plan</strong> whose documents permit the plan to invest in employer stock. This is a real qualified plan, not a formality.</li>
          <li><strong>Roll your existing funds into the new plan.</strong> A 401(k) from a former employer, a traditional IRA, or another eligible account moves in as a direct trustee-to-trustee rollover. Roth accounts are generally not usable this way.</li>
          <li><strong>The plan buys stock in the corporation.</strong> The plan now holds shares; the corporation now holds cash. This is the step that should be supported by a valuation.</li>
          <li><strong>The corporation buys the business</strong> with that cash &mdash; either outright or, more commonly, as the equity injection alongside an <a href="/acquire/business-acquisition-loan">acquisition loan</a>.</li>
        </ul>
        <p>That last point is where ROBS is most often used well. Funding an entire purchase from retirement savings puts everything on one square. Using $80,000 of rolled funds as the equity injection on an SBA-financed acquisition, while keeping the rest of your savings invested, is a materially different risk posture &mdash; and SBA lenders are accustomed to seeing ROBS-funded injections.</p>

""" + CTA_LENDER + """
        <h2>What it costs</h2>
        <p>The sticker cost is modest relative to a business purchase, and the recurring cost is the part buyers underweight.</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>Setup:</strong> roughly $4,000 to $6,000 to a ROBS provider for entity formation, plan documents, and the rollover mechanics.</li>
          <li><strong>Ongoing administration:</strong> roughly $130 to $200 per month for plan recordkeeping, testing, and compliance support. That is $1,500 to $2,400 a year, indefinitely, for as long as the structure exists.</li>
          <li><strong>Corporate tax return:</strong> a C corporation files its own return every year, which is a real accounting expense and a real tax posture &mdash; profits are taxed at the entity level, and money you take out beyond salary is taxed again as a dividend.</li>
          <li><strong>Form 5500:</strong> an annual plan filing once the plan crosses the reporting threshold, with penalties for late filing that are not trivial.</li>
          <li><strong>Valuation:</strong> the plan's purchase of stock, and subsequent annual valuations of a plan asset with no public market, should be supported by defensible numbers.</li>
        </ul>
        <p>Compare that against a straight distribution. Taking $100,000 out of a 401(k) before 59&frac12; means ordinary income tax on the full amount plus a 10% penalty &mdash; a combined bite that can easily exceed $35,000, before considering that the withdrawal may push you into a higher bracket. Against that, $5,000 of setup and $2,000 a year is cheap. The reason to hesitate about ROBS is not its price.</p>

        <h2>The compliance load is the real cost</h2>
        <p>The IRS has run a dedicated compliance project on ROBS arrangements, and the recurring findings are instructive: plans that were never actually offered to eligible employees, missing annual filings, promoters' entities that never operated a real business, and valuations that were never performed. The structure is legal; sloppy execution of it is not.</p>
        <p>Ongoing obligations worth understanding before you sign anything:</p>
        <ul style="list-style:disc;padding-left:24px;margin:16px 0;line-height:1.8;">
          <li><strong>The plan must be a real plan.</strong> If the business has employees who meet the eligibility rules, they must be able to participate &mdash; including the ability to invest in employer stock on the same terms. A plan that exists solely for the owner is a classic audit finding.</li>
          <li><strong>You must be a bona fide employee</strong> of the corporation, drawing reasonable W-2 compensation. Not a consultant, not an absentee owner.</li>
          <li><strong>No prohibited transactions.</strong> No unsecured loans from the company to you, no personal use of company assets, no above-market rent to an entity you control. The penalties for prohibited transactions are severe and can unwind the whole structure.</li>
          <li><strong>Annual filings and annual valuation.</strong> Form 5500 when required, and a supportable value for the stock the plan holds.</li>
        </ul>
        <p>The worst-case failure mode is not a fine. If the arrangement is disqualified, the rollover can be recharacterized as a distribution &mdash; retroactively, with tax, penalty, and interest, on the full amount, at a moment when the money is locked inside a business you cannot quickly sell.</p>

""" + CTA_MARKET + """
        <h2>The concentration problem</h2>
        <p>Set the tax mechanics aside for a moment. A ROBS takes savings that were diversified across an entire market and puts them into a single privately held small business &mdash; the same business that is now also your entire income. If it struggles, you lose the paycheck and the retirement account in the same quarter. There is no diversification left to cushion it and no unemployment claim behind a business you own.</p>
        <p>That is not an argument against ever doing it. It is an argument for two disciplines. First, do not roll everything: use what the injection requires and leave the rest invested. Second, apply harder diligence than you otherwise would &mdash; a business bought with borrowed bank money and a business bought with your retirement are not the same decision, and the <a href="/acquire/business-due-diligence-checklist">diligence checklist</a> deserves to be worked line by line. Confirm the earnings are real and the <a href="/acquire/how-to-value-a-business">valuation is defensible</a> before the plan writes a check for stock.</p>

        <h2>The two alternatives to rule out first</h2>
        <p><strong>A 401(k) loan.</strong> If your current employer's plan permits loans, you can borrow the lesser of $50,000 or half your vested balance and repay it with interest to your own account. No C corporation, no plan administration, no annual 5500, no prohibited-transaction exposure. The limitations are the cap, the fact that plans from former employers usually do not allow loans, and that separating from the employer can accelerate repayment &mdash; which matters if the plan is to quit and run the business you just bought. Still: if the gap is $40,000 of an SBA injection, this is the cheaper and simpler instrument.</p>
        <p><strong>A straight distribution.</strong> Expensive, but occasionally rational &mdash; if you are past 59&frac12;, the penalty disappears and only ordinary income tax applies, which for a modest amount may cost less than years of ROBS administration. Run the arithmetic rather than assuming.</p>
        <p>And the broader alternative: a larger <a href="/acquire/seller-financing-business-purchase">seller note</a> or a smaller target. A buyer who needs a ROBS to reach a deal is sometimes a buyer reaching for a deal one size too large. The <a href="/acquire/sba-loan-down-payment">down payment math</a> is worth running against a business 30% smaller before you restructure your retirement to buy this one.</p>

        <h2>If you go ahead</h2>
        <p>Use an established ROBS provider rather than assembling the structure from templates &mdash; the ongoing administration is the product, and the cheap version is cheap because it omits the part that keeps you compliant. Have your own CPA review the arrangement independently of the promoter selling it, because the promoter's incentive ends at setup and yours does not. Keep the plan genuinely available to eligible employees from the first hire. File on time, every year. Pay yourself a reasonable salary through payroll. And keep the annual valuation current, so that when you eventually sell the business and the plan converts stock back to cash, the record supports the numbers.</p>
        <p>Done properly, a ROBS is the difference between owning a profitable business at 42 and waiting until you are 60 to have the cash. Done carelessly, it converts a retirement account into a tax bill. The gap between those outcomes is administration, not luck.</p>
""",
}

for page in (P1, P2, P3):
    build(page)
