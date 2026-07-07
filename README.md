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
- **Coffman Marina (id:33)** — needs a website URL (owner was going to provide)
- **Yacht Haven (id:62)** — coordinates are approximate; fuel types (87/93) unconfirmed
- **Gas price staleness** — LakeExpo last published May 23-24, 2026; need to confirm if newer reports exist and if the fetcher is picking them up
- **Paradise Tropical name match** — LakeExpo calls it "Paradise Restaurant & Bar"; confirm in console that it matches correctly

---

## Location Data

All locations live in the `const locs = [...]` array starting around line 362 of `loto-navigator.html`.

- **Next available ID: 64** (last used: 63 for Neon Taco) — wait, IDs 64–75 are now used. Next available: **76**
- Prices are strings: `"3.79"` not `3.79`
- See `CLAUDE.md` for the full location schema

---

## Claude Code Context

For AI-assisted editing, see `CLAUDE.md` — it has the full schema for locations, fuel objects, filter logic, gas price panel, and known gotchas.
