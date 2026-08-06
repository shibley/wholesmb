#!/usr/bin/env python3
"""Audit every /acquire/ page for affiliate-compliance basics.

Checks, per page:
  1. an affiliate disclosure line linking to /disclosure.html
  2. every outbound link to a monetized partner carries rel="nofollow sponsored"
     and target="_blank"

Exit code 1 if anything fails, so this can gate a sprint before commit.
Run: python3 scripts/audit-affiliate-attrs.py
"""
import os
import re
import sys

ACQUIRE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "acquire")

# Domains we do (or will) monetize. Outbound links to these must be tagged.
PARTNER_DOMAINS = (
    "bizbuysell.com",
    "flippa.com",
    "empireflippers.com",
    "smartbizloans.com",
    "acquire.com",
    "microacquire.com",
    "quietlight.com",
    "loopnet.com",
)

ANCHOR_RE = re.compile(r"<a\b[^>]*href=\"(https?://[^\"]+)\"[^>]*>", re.I)

failures = []
pages = 0
tagged_links = 0

for name in sorted(os.listdir(ACQUIRE)):
    if not name.endswith(".html"):
        continue
    pages += 1
    path = os.path.join(ACQUIRE, name)
    html = open(path, encoding="utf-8").read()

    if "/disclosure.html" not in html:
        failures.append("%s: no link to /disclosure.html" % name)
    elif not any(p in html.lower() for p in ("affiliate link", "affiliate commission")):
        failures.append("%s: disclosure link present but no disclosure sentence" % name)

    for match in ANCHOR_RE.finditer(html):
        url = match.group(1)
        if not any(d in url for d in PARTNER_DOMAINS):
            continue
        tag = match.group(0)
        if "nofollow" not in tag or "sponsored" not in tag:
            failures.append('%s: partner link missing rel="nofollow sponsored" -> %s' % (name, url))
        elif 'target="_blank"' not in tag:
            failures.append('%s: partner link missing target="_blank" -> %s' % (name, url))
        else:
            tagged_links += 1

print("audited %d pages, %d compliant partner links" % (pages, tagged_links))
if failures:
    print("\nFAILURES (%d):" % len(failures))
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("PASS: disclosure + rel/target attributes correct on every page")
