#!/usr/bin/env python3
"""the-plan-make-fun-will-carry-20261122-2138

Writes one plan (1-280 chars) to /output/entry.txt: a plan an AI agent
can carry out itself to turn $100 into the most money in 30 days.

Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "Scan Shopify/Etsy listings for stores with missing/thin "
    "descriptions. Email 50 already-selling owners/day: $39 for 20 "
    "rewritten SEO descriptions in 24h, paid via Stripe link. Spend $100 "
    "on a domain and email volume; reinvest sales into outreach. "
    "Day 1: scan 200 stores, email 50."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry must not be whitespace-only")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
