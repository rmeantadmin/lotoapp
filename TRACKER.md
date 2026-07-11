# LOTO Navigator — Issue Tracker & Changelog

## How to Use This File

- When you fix something, check the box: `[ ]` → `[x]` and add the date
- When you find a new problem, add it to the Open Issues list
- At the bottom of each commit message, note what you changed and reference this file
- Keep resolved items here (don't delete them) so there's a record

---

## Open Issues

### Data / Locations
- [ ] **Yacht Haven (id:62)** — coordinates approximate, fuel types (87/93) unconfirmed. Call marina to verify.
- [ ] **Missing LakeExpo fuel locations** — these appear in the weekly gas report but aren't in the app (or are missing fuel objects): Rock Harbour Resort (MM 8), Premier Advantage Marina (MM 38), Paradise Marina & Water Sports (MM 1)
- [ ] **Franky & Louie's (id:13)** — has restaurant entry but no fuel object; LakeExpo lists them with gas prices
- [ ] **Dog Days (id:15)** — has restaurant entry but no fuel object; LakeExpo lists them with gas prices
- [ ] **Coconuts (id:8)** — verify fuel object is complete; LakeExpo lists gas prices

### Map / Channel Lines
- [ ] **Arm channel lines cut through land** — Gravois Arm and Big Niangua Arm especially have tight bends that need `guide:true` intermediate points added to `armChannelPts`. Same fix pattern as the main channel guide points added Jul 2026.

### Gas Prices
- [ ] **Stale hardcoded prices** — locations not covered by LakeExpo (e.g. The Hatch at Miller's Landing) show old baked-in prices and can incorrectly rank as "cheapest" in the Gas Price Panel. Should be demoted to "Call Ahead" if priceDate is older than ~60 days.
- [ ] **prices.json duplicates** — `scripts/fetch_prices.py` sometimes writes the same marina twice with different prices. Harmless but should be fixed by deduplicating on name+mm before writing.

### General
- [ ] **Spreadsheet not synced** — `LOTO_Navigator_Directory.xlsx` and `LOTO_Data_Gaps.xlsx` are manually maintained and not auto-synced to the HTML. Update manually if requested.

---

## Resolved Issues

- [x] **App wouldn't load at all** — fatal `dateStr` redeclaration syntax error in fetchLakeExpoPrices. Fixed Jul 8 2026.
- [x] **Coffman Marina (id:33) missing website** — added Facebook page URL. Fixed Jul 8 2026.
- [x] **Paradise Tropical not matching LakeExpo prices** — LakeExpo calls it "Paradise Restaurant & Bar". Alias confirmed and hardened. Fixed Jul 8 2026.
- [x] **Wrong prices assigned to Point Randall, Surdyke's Port 20, Premier 54** — prefix-match was too loose; now requires mile-marker proximity. Fixed Jul 8 2026.
- [x] **Gas price CORS proxies blocked by LakeExpo** — corsproxy.io and codetabs return 403/522. Fixed by adding GitHub Action that fetches LakeExpo server-side and commits `prices.json` daily at 9am CT. Jul 7 2026.
- [x] **Gas prices not updating** — LakeExpo had published new reports (June–July 2026) but app wasn't fetching them due to CORS block. Resolved with above fix. Jul 7 2026.
- [x] **Main channel line cuts through land** — added 10 `guide:true` intermediate points at bends MM 27–28, 38–39, 49–50, 53–56, 61–66. Fixed Jul 8 2026.
- [x] **Repo private blocked prices.json fetch** — raw.githubusercontent.com returns 404 for private repos. Made repo public. Jul 2026.
- [x] **Stale prices from May 2026** — resolved once GitHub Action was running and prices.json seeded with Jul 4 data. Jul 7 2026.

---

## Changelog

### Jul 10 2026
- Gas prices auto-updated by GitHub Action (daily 9am CT)

### Jul 9 2026
- Gas prices auto-updated by GitHub Action
- Demoted stale gas prices to "Call Ahead" section in Gas Price Panel

### Jul 8 2026
- Fixed fatal app load bug (dateStr syntax error)
- Added 7 LakeExpo fuel docks (4 new locations + 3 restaurants upgraded to type:"both")
- Added Fill'er Up n Liquor gas dock (id:80, Big Niangua Arm MM 44)
- Added Coffman Marina website (Facebook page)
- Fixed gas price matching (Point Randall, Surdyke's, Premier 54)
- Added channel guide points to fix main channel line cutting through land
- Continued arm channel mapping
- Gas prices auto-updated by GitHub Action

### Jul 7 2026
- Set up GitHub repo (rmeantadmin/lotoapp), pushed all files
- Built GitHub Action for daily gas price auto-update (scripts/fetch_prices.py)
- Seeded prices.json with Jul 4 weekend data (48 locations)
- Fixed fetchLakeExpoPrices to use prices.json first, CORS proxy as fallback
- Added README.md, HANDOFF.md, CLAUDE.md, LICENSE
- Made repo public to enable GitHub Pages and prices.json fetch
