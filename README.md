# LOTO Navigator

A mobile-first web app that maps waterfront restaurants, marinas, and fuel docks at Lake of the Ozarks, MO. Built for use on boats and phones to find nearby fuel, food, and amenities.

**Live demo:** Open `loto-navigator.html` in any browser — no install, no server needed.

---

## What It Is

A single self-contained HTML file with:
- Interactive Leaflet.js map with emoji pins for every location
- Filter tabs: All · Restaurants · Fuel Docks · My Places
- Sub-filters: Breakfast / Open Late / Live Music (restaurants), fuel grade (fuel docks)
- Gas Price Panel — live prices pulled automatically from LakeExpo.com on every page load
- Popup detail sheet for each location (hours, phone, website, highlights, fuel prices)
- "My Places" — users can drop custom pins saved to their browser

---

## Files

| File | Purpose |
|------|---------|
| `loto-navigator.html` | The entire app — HTML, CSS, and JS in one file |
| `LOTO_Navigator_Directory.xlsx` | Companion spreadsheet with all location data (not auto-synced) |
| `CLAUDE.md` | Technical context for Claude Code AI assistant |
| `README.md` | This file |

---

## How to Run / Test

1. Open `loto-navigator.html` in Chrome
2. Open Chrome DevTools (F12) → Console tab
3. Look for: `[LOTO] LakeExpo prices: parsed X marinas, updated Y locations`
   - This confirms the live gas price fetch is working
   - If it says `LakeExpo price fetch failed`, the CORS proxies are down

No build step. No npm. No server. Just open the file.

---

## What Still Needs Work

See `HANDOFF.md` for the full list in plain English.

Quick summary:
- **Yacht Haven (id:62)** — coordinates are approximate; fuel types (87/93) unconfirmed
- **Missing fuel locations** — LakeExpo reports gas prices for locations not in the app (or in the app without fuel objects): Rock Harbour Resort (MM 8), Lake Burger (MM 4), Premier Advantage Marina (MM 38), Paradise Marina & Water Sports (MM 1), Franky & Louie's (MM 10), Dog Days (MM 19), Coconuts (MM 7)
- **Stale hardcoded prices** — locations LakeExpo doesn't report keep old baked-in prices (e.g. The Hatch shows Aug 2025) and can wrongly rank as "cheapest"; consider demoting or flagging prices older than ~30 days
- **prices.json duplicates** — `scripts/fetch_prices.py` writes most marinas twice (sometimes with different prices); harmless but worth fixing
- **Private repo blocks price fetch** — `prices.json` is fetched from raw.githubusercontent.com, which 404s while the repo is private; make the repo public (also enables free GitHub Pages hosting)

Resolved Jul 2026: Coffman Marina website added (Facebook page); Paradise Tropical matching confirmed and hardened; fatal `dateStr` redeclaration syntax error fixed (app wouldn't load at all); prefix-match now requires mile-marker proximity (Point Randall, Surdyke's Port 20, and Premier 54 were getting other marinas' prices).

---

## Location Data

All locations live in the `const locs = [...]` array starting around line 362 of `loto-navigator.html`.

- **Next available ID: 64** (last used: 63 for Neon Taco) — wait, IDs 64–75 are now used. Next available: **76**
- Prices are strings: `"3.79"` not `3.79`
- See `CLAUDE.md` for the full location schema

---

## Claude Code Context

For AI-assisted editing, see `CLAUDE.md` — it has the full schema for locations, fuel objects, filter logic, gas price panel, and known gotchas.
