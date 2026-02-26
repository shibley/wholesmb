# WholeSMB

**Independent, data-driven software comparisons for small and mid-size businesses.**

A project by [Bity LLC](https://bity.com).

## Overview

WholeSMB is a static content site that publishes side-by-side comparisons of B2B SaaS tools, focused on the needs of teams with 1–200 employees. Think Wirecutter meets G2, but simpler and built for SMBs.

## Structure

```
wholesmb/
├── index.html              # Homepage
├── about.html              # About + methodology
├── privacy.html            # Privacy policy
├── disclosure.html         # FTC-compliant affiliate disclosure
├── template-comparison.html # Reusable comparison page template
├── css/
│   └── style.css           # All styles (mobile-first, no framework)
├── js/
│   └── main.js             # Minimal JS (nav toggle, smooth scroll)
├── img/                    # Images & OG images
│   └── comparisons/        # Per-comparison OG images
├── comparisons/            # Published comparison pages go here
├── favicon.svg             # SVG favicon
├── robots.txt
├── sitemap.xml
├── vercel.json             # Vercel deployment config
└── package.json
```

## Development

```bash
# Local dev server
npx serve .
```

## Creating a New Comparison

1. Copy `template-comparison.html` to `comparisons/[tool-a]-vs-[tool-b].html`
2. Replace all `{{PLACEHOLDER}}` values with real content
3. Add OG image to `img/comparisons/[slug]-og.png`
4. Add URL to `sitemap.xml`
5. Link from homepage and category pages

## Template Placeholders

The comparison template uses `{{PLACEHOLDER}}` syntax for all dynamic content:

- `{{TOOL_A}}` / `{{TOOL_B}}` — tool names
- `{{CATEGORY}}` / `{{CATEGORY_SLUG}}` — category name and URL slug
- `{{YEAR}}` / `{{MONTH}}` — current date
- `{{SLUG}}` — URL slug (e.g., `hubspot-vs-salesforce`)
- Plus pricing, features, pros/cons, FAQ answers, and schema data

## Deployment

Static site on Vercel. Push to deploy.

## Categories

- CRM
- Payroll & HR
- Project Management
- Marketing Tools
- Finance & Payments
