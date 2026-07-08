# LOTO Navigator — Project Context for Claude Code

## What This Is
A single-file mobile-first web app (`loto-navigator.html`) that maps waterfront restaurants, marinas, and fuel docks at Lake of the Ozarks, MO. Built with Leaflet.js + OpenStreetMap tiles. No build system, no dependencies beyond CDN scripts — everything lives in one HTML file.

The app is used on boats/phones to find nearby fuel, food, and amenities by map or filter tabs.

---

## File Structure
Everything is in **one file**: `loto-navigator.html`

Sections (in order):
1. `<head>` — Leaflet CSS + JS CDN links
2. `<style>` — All CSS (minified-ish, organized by component with comments)
3. `<body>` — HTML shell (header, filter tabs, map div, popup sheet, gas price panel, my-places form)
4. `<script>` — All JS:
   - `const locs = [...]` — the location data array (~line 362)
   - `const armMMs = [...]` — mile marker label coordinates for arm channels
   - Map init, marker rendering, popup generation, filter logic, gas price panel, my-places feature

---

## Location Data Schema

Each entry in `const locs` follows this shape:

```javascript
{
  id: 1,                          // Unique integer. Last used: 63 (Neon Taco). Next: 64.
  name: "Example Marina",
  type: "restaurant",             // "restaurant" | "fuel" | "both"
  mm: 19,                         // Mile marker (main channel). Use arm MM for arm locations.
  cove: "Main Channel (MM 19)",   // Human-readable location label shown in popup
  lat: 38.1384,                   // Latitude
  lng: -92.6597,                  // Longitude
  icon: "⛽",                     // Emoji icon shown on map pin
  phone: "(573) 348-4700",        // Or null
  website: "https://...",         // Or null
  address: "123 Lake Rd, ...",    // Or null
  desc: "Short description...",   // 1–2 sentences shown in popup
  hours: "Seasonal Apr–Oct · 11am–11pm",  // Free-form string
  seasonal: true,                 // Boolean — controls seasonal badge on pin
  highlights: ["Item 1", "Item 2"], // Array of strings, or null. Shown as bullets in popup.
  tags: ["breakfast", "late", "music"], // Optional array. Drives restaurant sub-filter tabs.
  menuUrl: "https://...",         // Or null. Shows "View Menu" button in popup.
  gfOptions: ["GF pizza available", "Check with server"], // Array, or null. GF section in popup.
  fuel: { ... },                  // Fuel object (see below), or null for restaurants
  cstore: true,                   // Boolean or null — convenience store on site
  xtow: true,                     // Boolean or null — X-Tow Captain's Club partner
}
```

### Valid `tags` values (drive sub-filter tabs):
- `"breakfast"` — shows under "🍳 Breakfast" tab
- `"late"` — shows under "🌙 Open Late" tab
- `"music"` — shows under "🎵 Live Music" tab

---

## Fuel Object Schema

```javascript
fuel: {
  types: ["87 Regular", "93 Premium", "Diesel"],  // Displayed in popup
  prices: {
    87: "3.79",      // String price like "3.79", or null if unknown
    89: null,
    91: null,
    93: "4.99",
    diesel: "3.99",
  },
  priceDate: "Mar 2026",    // Month + year of last known price, or null
  hours: "Tue–Sat 8:30am–5pm",  // Fuel dock hours (may differ from restaurant hours)
  pricesUrl: "https://...",  // URL to check for weekly price updates (not rendered in UI — just for reference)
  note: "No-wake cove. X-Tow members save 10¢/gal."  // Shown in popup
}
```

### Known `pricesUrl` references (for weekly gas price updates):
- Paradise Tropical: `https://www.paradiseatthelake.com/gas-dock`
- Formula Boats: `https://formulaboatsmo.com/gas-dock.asp`
- Point Randall: `https://pointrandallresort.com/Gas-Dock-and-Mini-Mart.html`

---

## Filter Tab System

**Main tabs** (`#filter-tabs`): All · Restaurants · Fuel Docks · My Places

**Restaurant sub-tabs** (`#sub-filter-tabs`, visible when Restaurants active):
All · 🍳 Breakfast · 🌙 Open Late · 🎵 Live Music

**Fuel grade sub-tabs** (`#fuel-filter-tabs`, visible when Fuel Docks active):
All Grades · 87 · 89 · 91 · 93 · Diesel · 💰 Gas Prices

Clicking "💰 Gas Prices" opens the **Gas Price Panel** (full-screen overlay) instead of filtering the map.

---

## Gas Price Panel

- Full-screen overlay: `#gas-price-panel`, `position:fixed; z-index:1100`
- **Must be z-index > 1000** — the header is `z-index:1000` and will cover the panel otherwise
- Grade tabs at top (87 / 91 / 93 / Diesel), each showing only locations with that grade
- Sorted cheapest first; 🥇🥈🥉 medals for top 3
- "Call Ahead" section at bottom for locations with null prices
- Tapping a row: closes panel → `map.flyTo([lat,lng], 16)` → opens that location's marker popup
- Close button: `#gpp-close` (white circle X in top-right of panel header)

---

## Popup Sheet

Bottom sheet (`#popup-sheet`) slides up when a map pin is tapped. Populated dynamically by `buildPopup(loc)`. Sections rendered (if data present):
- Name, type badge, cove/MM label
- Phone link, website button
- Address
- Hours + seasonal badge
- Description
- Highlights (bullet list)
- GF options (bullet list, shown if `gfOptions` is non-null)
- Fuel info (types, prices, hours, note, X-Tow badge)
- Menu URL button
- C-Store badge

---

## My Places Feature

Users can drop custom pins on the map (purple FAB button). Stored in `localStorage` under key `myPlaces`. Not part of `locs` array.

---

## Arm Mile Marker Labels

`const armMMs` array provides coordinates for rendering mile marker labels on arms (Gravois, Big Niangua, Little Niangua, etc.). These are display-only — used to render channel labels on the map at appropriate zoom levels.

Pin labels (name text under emoji) are zoom-gated: only visible at zoom ≥ 13 to avoid clutter.

---

## Conventions & Gotchas

- **Next available ID: 76** (last used was 75 for Hiawatha Beach)
- **Always read the file before editing** — the Edit tool requires a prior read of the section being changed
- **Edit tool "Found 2 matches" error**: If `old_string` matches more than once, add more surrounding context (the full entry block with `id:XX`) to make it unique
- **Prices are strings**, not numbers: `prices:{87:"3.79"}` not `prices:{87:3.79}`
- **`seasonal: false`** = year-round (no seasonal badge). **`seasonal: true`** = shows seasonal indicator on pin
- **`gfOptions: null`** = GF section hidden entirely. `gfOptions: ["Check with your server..."]` = shows default message
- **`fuel: null`** for pure restaurants; fuel object required for `type:"fuel"` or `type:"both"`
- **`type:"both"`** = location has both restaurant and fuel dock (e.g. Paradise Tropical, Ozark Yacht Club). Shows up in both Restaurant and Fuel Dock filters.
- Website URLs: some locations use Facebook pages as their "website" — this is intentional

---

## Gas Price Auto-Update System

Prices are updated automatically — no manual edits to `loto-navigator.html` needed.

### How it works
1. **GitHub Action** (`.github/workflows/update-prices.yml`) runs every day at 9am CT
2. It runs `scripts/fetch_prices.py`, which fetches the latest LakeExpo Boat Gas Report and writes `prices.json` to the repo
3. **On every page load**, the app fetches `prices.json` from GitHub and updates the Gas Price Panel in-memory
4. If `prices.json` is unavailable or stale (>8 days), the app falls back to direct CORS proxy fetching (often blocked by LakeExpo — unreliable)

### Manual trigger
Go to **github.com/rmeantadmin/lotoapp** → Actions tab → **Update Gas Prices** → **Run workflow**

### prices.json format
```json
{
  "updated": "2026-07-07T14:00:00Z",
  "articleUrl": "https://www.lakeexpo.com/...",
  "locations": [
    { "mm": 1, "name": "Bergers Marina", "prices": { "87": "4.39" } }
  ]
}
```

### Name matching
`fetchLakeExpoPrices()` in the HTML matches LakeExpo names to `locs[]` entries by name similarity + aliases. The `nameAliases` map in that function handles known name mismatches. If a location stops updating, check the alias map.

### Workflow file caveat
Editing `.github/workflows/update-prices.yml` requires a GitHub token with `workflow` scope. If a push is rejected with "workflow scope" error, edit the file directly on github.com using the web editor.

---

## Pending / Known Issues

- **Coffman Marina (id:33)**: No website — owner was going to find it
- **Yacht Haven (id:62)**: Coordinates (`lat:38.2020, lng:-92.6470`) are approximate — may need correction. Fuel types (87/93) are assumed — confirm with owner
- **Spreadsheet**: `LOTO_Navigator_Directory.xlsx` exists as a companion file — not auto-synced to the HTML; manual updates needed if requested
