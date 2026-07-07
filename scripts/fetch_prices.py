#!/usr/bin/env python3
"""
Fetches the latest LakeExpo Boat Gas Report and writes prices.json.
Called by GitHub Actions every Saturday and Sunday morning.
"""
import json
import re
import sys
from datetime import datetime, timezone
import urllib.request

LISTING_URL = "https://www.lakeexpo.com/boating/boat_gas_report/"
BASE_URL = "https://www.lakeexpo.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; LOTO-Navigator/1.0)"}


def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def get_latest_article_url(html):
    match = re.search(
        r'href="(/boating/boat_gas_report/[^"]+article_[^"]+\.html)"',
        html
    )
    if not match:
        raise ValueError("No article link found on listing page")
    return BASE_URL + match.group(1)


def parse_prices(html):
    clean = re.sub(r"<[^>]+>", " ", html)
    clean = re.sub(r"&amp;", "&", clean)
    clean = re.sub(r"&nbsp;", " ", clean)
    clean = re.sub(r"\s+", " ", clean)

    price_pattern = re.compile(
        r"\((\d+)\s*MM\)\s*([^–—$]+?)\s*[–—]\s*(.+?)(?=\(\d+\s*MM\)|$)",
        re.IGNORECASE,
    )
    fuel_pattern = re.compile(
        r"\$(\d+\.\d{2})\s*(87|89|91|93|diesel)\s*(?:octane)?",
        re.IGNORECASE,
    )

    locations = []
    for m in price_pattern.finditer(clean):
        name = m.group(2).strip().strip("•").strip()  # strip bullet •
        prices = {}
        for fm in fuel_pattern.finditer(m.group(3)):
            prices[fm.group(2).lower()] = fm.group(1)
        if prices:
            locations.append({"mm": int(m.group(1)), "name": name, "prices": prices})

    return locations


def main():
    print("Fetching listing page...")
    article_url = get_latest_article_url(fetch(LISTING_URL))
    print(f"Latest article: {article_url}")

    print("Fetching article...")
    locations = parse_prices(fetch(article_url))

    if not locations:
        print("ERROR: No prices parsed", file=sys.stderr)
        sys.exit(1)

    with open("prices.json", "w") as f:
        json.dump({
            "updated": datetime.now(timezone.utc).isoformat(),
            "articleUrl": article_url,
            "locations": locations,
        }, f, indent=2)

    print(f"Done: {len(locations)} locations written to prices.json")


if __name__ == "__main__":
    main()
