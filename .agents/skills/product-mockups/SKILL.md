---
name: product-mockups
description: Create professional product mockups for the user's micro offer - a flat ebook or toolkit cover, 3D book and box shots, device mockups (laptop, tablet, phone showing their real product pages), and bundle or stack shots that show everything inside for value stacking. Designs and approves the flat cover first, then renders every mockup from that exact cover so the title text stays correct. Saves clean, page-ready PNGs for sales pages, checkout pages and ads. Use when the user says "make a cover for my ebook", "I need a mockup", "3D book image", "show my product on a laptop", "make a bundle image", "value stack image", or needs product visuals before building a sales page or ad.
---

# $product-mockups - Covers and Mockups for Your Micro Offer

A micro offer is usually digital, which means buyers cannot hold it. A good mockup makes it feel real and worth more than the price. Your job: design a clean cover, then turn it into the 3D, device and bundle shots their sales page and ads need.

The person you are helping is not technical. Plain English, one question at a time, no code or tool names unless they ask.

---

## Hard rules (read first, never break)

1. **Cover first, mockups second.** Never render a 3D or bundle shot until the user has approved the flat cover. Every mockup is built from that approved cover file, passed in as a reference image, so the text stays exactly the same.
2. **Short titles on covers.** Image models misspell long text. Keep the cover to: title (ideally 2-6 words), optional subtitle (under 10 words), author name. No paragraphs, no bullet lists on the cover.
3. **Check spelling after every single render.** Open the image and read every word. A mockup with a typo on the cover is unusable.
4. **Never fake the product.** Device mockups show the user's real screenshots from `assets/product/`. Do not invent dashboard screens, lesson pages or worksheet content and present them as the real product. If you need screenshots and have none, ask.
5. **Never AI-regenerate a real person's face.** If the cover uses the user's photo, use their real photo from `assets/photos/` as-is (cut out and placed, not redrawn).
6. **No em dashes or en dashes. Ever.** Not on covers, not in filenames, not in chat.
7. **No invented claims on covers.** No "bestseller", "#1", "10,000 students" unless the user gave you that fact.

---

## Step 0 - Read the workspace (silently)

Read whatever exists; skip what does not.

| File / folder | What you take from it |
|---|---|
| `context/business.md`, `context/me.md` | Offer name, what is inside, audience, the user's name as it should appear |
| `references/moa/offer.md` | How MOA frames micro offers (deliverables, value stack, naming) |
| `references/moa/00-moa-overview.md` | The program's overall approach to micro offers |
| `references/moa/voice.md` | Tone for titles and subtitles |
| `content/pages/` | Sales page, if built: the real product name, what is inside, the value stack |
| `assets/brand/` | Logo, colors, fonts |
| `assets/product/` | Screenshots of their product (pages, lessons, templates, worksheets) |
| `assets/photos/` | Real photos, if they want themselves on the cover |
| `content/mockups/` | Earlier mockups, so you keep the look consistent |

If the offer is still unknown (empty `context/business.md` and no sales page), ask: "What is the product called, what format is it (ebook, toolkit, templates, mini-course), and what is inside?" Or suggest running $my-business first.

---

## Step 1 - Agree what they need

Ask which of these they want (suggest a default based on their offer):

| Mockup | Best for | File |
|---|---|---|
| Flat cover | Everything starts here, also used as a thumbnail | `cover-flat.png` |
| 3D book / ebook shot | Ebooks, guides, workbooks | `cover-3d.png` |
| 3D box / product box | Toolkits, template packs, bundles | `box-3d.png` |
| Laptop screen | Mini-courses, Notion or Canva templates, dashboards | `device-laptop.png` |
| Tablet screen | Workbooks, planners, ebooks | `device-tablet.png` |
| Phone screen | Mobile-friendly content, audio, checklists | `device-phone.png` |
| Bundle / stack shot | Value stacking: main product plus bonuses in one image | `bundle-stack.png` |

Default suggestion for most micro offers: flat cover, one 3D shot, one bundle shot. Add a device shot if the product is something they use on a screen.

For the bundle shot, list every item that goes in it (main product + each bonus) and confirm the list. These names come from the sales page or `context/`, never invented.

---

## Step 2 - Design the flat cover

**Gather first:**
- Title (push for short: if the product name is long, suggest a short cover title and keep the full name for the sales page)
- Subtitle (optional, one line, the promise)
- Author name exactly as they want it shown
- Brand colors (from `assets/brand/`, or ask for 1-2 colors they like, or propose a palette that fits their audience)
- Logo (optional, only from `assets/brand/`)

**Design rules (your call, do not ask):**
- Portrait 2:3 ratio for ebooks and guides. Square for template packs or toolkits if it suits better.
- Title is the hero: big, bold, readable at thumbnail size (imagine it 150px tall on a phone).
- One or two fonts max, high contrast between text and background.
- One simple visual idea (a bold color block, a clean icon, an abstract shape, or their real photo). Not a busy collage.
- Leave clear margins; nothing important near the edges.

**Generate:** Generate images with Codex's built-in image generation (include `$imagegen` in the request; it needs ChatGPT Plus or higher). Image turns use up Codex usage 3-5x faster than text, so lock every word and color first, then generate. If built-in generation is not available in your Codex, use the fallback script:

```
python3 scripts/generate_image.py --prompt "..." --ref assets/brand/logo.png --out content/mockups/<offer-slug>/cover-flat.png --size 1024x1536
```

(sizes: 1024x1024, 1024x1536 portrait, 1536x1024 landscape; needs `OPENAI_API_KEY` in `.env`). If neither works, tell the user plainly and stop. Never claim an image was made when it was not.

**Reference images:** workspace files (cover, screenshots, photos, logo) can be passed by path. If the user has an image outside the workspace, ask them to Shift+drag it into the Codex prompt box or drop it into `assets/product/`.

**Saving:** every final image must be on disk in `content/mockups/<offer-slug>/`. If an image only shows in the Codex canvas and is not on disk, ask the user to download it and save it there with the exact filename you give them.

**Size:** for a 2:3 cover, use 1024x1536 (that is already 2:3). For square toolkit covers, 1024x1024.

In the prompt, put every word in quotes exactly as it should appear and say "render this text exactly, no other text, no typos". Describe layout, colors and style in plain words. If the user's photo is used, pass it as an input image and ask the model to keep the person exactly as photographed.

**If the title text comes out wrong after one retry:** generate the cover artwork with no text, then add the text yourself (a simple HTML page at the cover size screenshotted with headless Chrome, or Python Pillow if `python3 -c "import PIL"` works; do not assume it is installed). Correct text matters more than anything else on a cover.

**Check, then show:**
- [ ] Every word spelled correctly and matches what was agreed
- [ ] No stray or extra text anywhere
- [ ] Title readable at thumbnail size
- [ ] No dashes, no invented claims

Save as `content/mockups/<offer-slug>/cover-flat.png` (slug: the offer name, lowercase, hyphens, e.g. `client-onboarding-toolkit`; if `content/pages/` already has a folder for this offer, reuse that exact slug). Show it and ask: "Happy with this cover? Once you approve it, I'll build the 3D and bundle shots from this exact file."

Change one thing per round of feedback. Do not move on until they approve.

---

## Step 3 - Render the mockups from the approved cover

Every mockup uses the approved `cover-flat.png` (and screenshots, where relevant) as an **input image**, so the model places the existing artwork instead of retyping it.

**Prompt pattern for each mockup:**
- "Use the attached cover image exactly as it is. Do not change, redraw or retype any of its text or design. Place it onto [a 3D hardcover book / a product box / a tablet screen]..."
- Describe the angle (slight three-quarter view reads well), soft realistic shadow, lighting, and background.
- Ask for no extra text anywhere in the scene.

**Per mockup type:**

- **3D book / ebook:** three-quarter angle, visible spine (repeat the title on the spine only if it is short), soft shadow underneath.
- **3D box:** front face shows the cover, side face in the brand color, clean studio lighting.
- **Device shots:** pass the user's real screenshot from `assets/product/` and ask for it to be shown on the device screen exactly as supplied. Modern, unbranded device (no visible Apple logo). If the screenshot has lots of small text, that is fine: it is their real screen, not retyped. Check the screen was not redrawn with fake text.
- **Bundle / stack:** main product in front and largest, bonuses arranged behind and around it (fanned books, a box, a tablet, printed sheets). Pass the cover and any bonus covers as input images. If bonuses have no covers yet, make simple matching flat covers for them first (same Step 2 rules, short titles, get approval) before the stack shot. A bundle with 3-6 items reads best; more becomes clutter.

**Background guidance (for GHL and other page builders):**
- **Default for the sales page: transparent PNG** (MOA page guide asks for a transparent background so the mockup sits on any section).
- **Clean background** (plain white or very light neutral, soft shadow) for ads and anywhere a transparent file won't work.
- **Transparent PNG** if the user wants to place it on a colored section. Ask the image tool for a transparent background if it supports it. If it does not, render on plain white and remove the background afterwards (for example with Python `rembg` if installed, check first, or tell the user to use the free background remover in Canva). Check the edges look clean and the shadow still looks natural.
- If they want it on a colored background, use their brand color so it matches the page.
- Ask once which they prefer if unclear; otherwise give a transparent version of the main 3D shot for the page plus the clean-background versions.

**Check after every render (do not skip):**
- [ ] Cover text identical to the approved cover, every word spelled right
- [ ] No new random text, labels or logos added by the model
- [ ] Device screens show the real screenshot, not invented content
- [ ] Perspective looks natural (no warped book, no melted edges, no extra fingers if a hand is in shot)
- [ ] Background clean and consistent across the set
- [ ] No dashes anywhere

If a render garbles the cover, regenerate once with a stronger "do not alter the attached image" instruction. If it fails again, change approach: render the 3D object with a blank cover and place the flat cover onto it yourself (perspective-warp with Python Pillow if installed, check first), or offer a simpler flat-on-shadow version.

---

## Step 4 - Save and hand over

```
content/mockups/<offer-slug>/
  cover-flat.png
  cover-3d.png
  cover-3d-transparent.png   (if made)
  box-3d.png                 (if made)
  device-laptop.png          (if made)
  device-tablet.png          (if made)
  device-phone.png           (if made)
  bundle-stack.png           (if made)
  notes.md
```

`notes.md` records: offer name, cover title/subtitle/author exactly as approved, colors used (hex), what is in the bundle, and which files are transparent. This keeps future mockups and ads consistent.

Tell the user, short and plain:
- Where the files are
- Where each one works best: `cover-3d.png` in the sales page hero, `bundle-stack.png` next to the price or value stack section, device shots in the "what's inside" section, the flat cover as the checkout or email thumbnail
- That `$ad-images` can now use these mockups in their ads
- One question: "Any tweaks, or are these good to go?"
