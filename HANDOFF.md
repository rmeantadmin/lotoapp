# LOTO Navigator — Handoff Guide

*Written for someone taking over the project who may not have built a web app before.*

---

## What This App Is

LOTO Navigator is a map app for Lake of the Ozarks boaters. Open it on your phone or computer, and you see a map with pins for every fuel dock, restaurant, and marina on the lake. You can filter by type, see hours and phone numbers in a popup, and check live gas prices pulled from LakeExpo.com.

The entire app is a **single HTML file**: `loto-navigator.html`. There is no server, no database, no login system. To "run" the app, you just open that file in a web browser.

---

## What You Need to Install

### 1. Claude Code (the AI assistant that helps you edit the app)
- Download at: **https://claude.ai/download**
- This is the tool you'll use to make changes. You type what you want changed in plain English and it edits the code for you.
- When you open a project folder in Claude Code, it reads `CLAUDE.md` automatically to understand the project context — so the AI already knows how this app is built.

### 2. Google Chrome (for testing)
- Download at: **https://www.google.com/chrome**
- Use Chrome specifically (not Edge, Firefox, or Safari) because the developer console works best there for checking if things are working correctly.

### 3. GitHub Desktop (optional but recommended for saving your work)
- Download at: **https://desktop.github.com**
- This saves your work to the cloud and lets you undo changes if something breaks.
- Your brother will give you access to the project repository — see the section at the bottom.

---

## How to Open and Test the App

1. Find the file `loto-navigator.html` in the project folder
2. Right-click it → Open With → Google Chrome
3. The map should load with pins on it
4. Tap or click a pin to see the popup with details
5. Click the "Fuel Docks" tab at the top, then "💰 Gas Prices" to see the gas price panel

**To check if gas prices are loading from LakeExpo:**
1. Press **F12** on your keyboard (this opens the Developer Tools panel)
2. Click the **Console** tab at the top of that panel
3. Look for a line that says something like:
   `[LOTO] LakeExpo prices: parsed 37 marinas, updated 33 locations`
4. If it says that — great, prices are live. If it says "fetch failed" — the automatic price system isn't working and you'll want to ask Claude Code to help debug it.

---

## What Still Needs to Be Done

Here are the known open items, from most to least important:

---

### 1. Confirm "Paradise Tropical" is matching correctly

**What it is:** Paradise Restaurant & Bar at mile marker 24 sells 87 Ethanol-Free fuel. The app tries to match LakeExpo's listing ("Paradise Restaurant & Bar") to our entry ("Paradise Tropical Restaurant & Bar").

**How to check:** Open the app, press F12, look at the console. If Paradise is matching, gas prices for it should appear in the Gas Price Panel under 87 octane.

**If it's not matching**, tell Claude Code:
> "Paradise Tropical (id:20) isn't getting its gas price updated from LakeExpo. LakeExpo calls it 'Paradise Restaurant & Bar'. Add an alias for it in the nameAliases object in fetchLakeExpoPrices."

---

### 3. Coffman Marina — needs a website URL

**What it is:** Coffman Marina is entry id:33 in the app (Upper Lake, MM 51). It currently has `website: null` because the owner was going to find the URL.

**How to fix:** Find their website (try Googling "Coffman Marina Lake of the Ozarks") and then tell Claude Code:
> "Add this website URL to Coffman Marina (id:33): [paste the URL]"

---

### 4. Yacht Haven — confirm coordinates and fuel types

**What it is:** Yacht Haven is entry id:62 (Jennings Branch Cove, MM 1). The map coordinates were estimated and the fuel types (87 and 93) were assumed — neither has been confirmed with the actual marina.

**How to fix:** Call or visit the marina to confirm:
- Do they sell 87 Regular? 93 Premium? Any other grades?
- Drop a pin on Google Maps at their actual dock to get precise coordinates (right-click → "What's here?" gives you lat/lng)

Then tell Claude Code:
> "Update Yacht Haven (id:62) with these confirmed coordinates: lat [X], lng [Y]. Fuel types are [list]. Update accordingly."

---

## Passwords / Credentials Needed

**None.** This app has no login, no backend server, no API keys, and no database. It's a plain HTML file that runs entirely in the browser. The only external service it contacts is LakeExpo.com (to fetch gas prices), which requires no authentication.

The companion Excel file (`LOTO_Navigator_Directory.xlsx`) also has no password.

---

## How to Make Changes with Claude Code

1. Open Claude Code and open the project folder (the one with `loto-navigator.html` in it)
2. Type what you want to change in plain English. Examples:
   - *"Add a new fuel dock called XYZ Marina at mile marker 15. It sells 87 and 93 octane. Phone is (573) 555-1234."*
   - *"The gas price panel isn't showing prices for Toad Cove Marina. Can you check why?"*
   - *"Update the hours for Kelly's Port to Mon–Fri 9am–6pm, Sat–Sun 8am–8pm."*
3. Claude Code will make the change and show you what it did
4. Reload the HTML file in Chrome to see the result

**If something breaks:** Don't panic. If you're using GitHub (see below), you can always revert to the last saved version. Just ask Claude Code:
> "Something broke after the last change. Can you undo it?"

---

## How Gas Prices Work (Nothing to Do — It's Automatic)

Gas prices update themselves every day at 9am automatically. Here's how:

- A **GitHub Action** (a scheduled script that runs in the cloud) fetches the latest LakeExpo Boat Gas Report every morning
- It saves the prices to a file called `prices.json` in the repository
- When anyone opens the app, it reads that file and shows the current prices

You can also trigger it manually if you want fresh prices right now:
1. Go to **github.com/rmeantadmin/lotoapp**
2. Click the **Actions** tab
3. Click **Update Gas Prices** on the left
4. Click **Run workflow** → **Run workflow**

You do NOT need to manually update any prices.

---

## Getting Set Up with GitHub

The project is already on GitHub at **github.com/rmeantadmin/lotoapp** (private). Your brother has invited you as a collaborator — you'll get an email to accept.

**Once invited:**
1. Download **GitHub Desktop** (https://desktop.github.com)
2. Sign in with your GitHub account
3. Click File → Clone Repository → find `lotoapp`
4. Choose where to save it on your computer
5. Open Claude Code and point it at that folder

Whenever you finish a session of changes:
- In GitHub Desktop, you'll see your changed files listed
- Write a short description of what you changed (e.g., "Updated Coffman Marina website")
- Click **Commit to main** then **Push origin**
- Your changes are now saved to the cloud

---

## If You Get Stuck

Just describe the problem to Claude Code in plain English. It has the full technical context of this project loaded automatically from the `CLAUDE.md` file. You don't need to explain how the app works — just describe what you're trying to do or what seems broken.
