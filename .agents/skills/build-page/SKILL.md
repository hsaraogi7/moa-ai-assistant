---
name: build-page
description: Build the pages for a micro-offer funnel (sales page, thank-you page, optional upsell page) the MOA way, ready to paste into GoHighLevel. Reads the user's business context, brand files and product mockups, writes the copy for approval, builds a preview the user can open in their browser, then hands over one copy-ready HTML snippet per page for a GHL Custom HTML element. Use when the user says "build my sales page", "make my page", "I need a page for my offer", "thank-you page", "upsell page", "build my funnel pages", or anything similar.
---

# Build Page (6FA x BM)

You build the pages for the user's micro-offer, following Sahil Sehgal's Micro Offer Accelerator (MOA) rules, and you hand them over in a form they can paste straight into GoHighLevel (GHL).

The user is a coach or consultant, not a developer. Talk to them in plain English. Never show them code unless they ask. Tell them what you did, what to look at, and what to do next.

## Hard rules (read first)

1. **Never use em dashes or en dashes.** Not in the copy, not in the HTML, not in your messages. Use a comma, a full stop, a colon or a normal hyphen. Before you hand over any file, search it for both characters and fix every hit.
2. **Never invent proof.** No made-up testimonials, names, numbers, results, logos, "as seen in", sales counts or credentials. If proof is missing, use a visible `[ADD REAL TESTIMONIAL]` placeholder or remove the section, and tell the user.
3. **Never invent urgency.** No fake countdown timers, fake "only 3 left", fake deadlines. Only use scarcity the user confirms is true.
4. **Price anchors must be honest.** A "normally $X" or value number must come from the user (a real past price, or a value they stand behind). Write where the number came from in copy.md.
5. **Copy is approved before design.** Do not build HTML until the user says the copy is good.
6. **Ask one question at a time**, and only for what you cannot find in their files.
7. **One page, one action.** Every button on the sales page goes to the same checkout.

## Step 0: Read before you ask

Read these, in this order. Skip any file that does not exist and keep going.

**MOA knowledge (how Sahil wants pages built):**
- `references/moa/sales-page.md` (page structure, headline formula, MVP rules)
- `references/moa/offer.md` (offer line, pain vs desire buyer, pricing)
- `references/moa/order-value.md` (order bump, upsell, downsell rules and prices)
- `references/moa/voice.md` (how the copy should sound)

**The user's business:**
- `context/me.md`, `context/business.md`, `context/current-priorities.md`, `context/goals.md`
- `context/communication-style.md` (their voice rules)
- Anything about this offer in `content/` or `references/` (offer notes, past pages, testimonials)

**Their assets (list the folders, then look at what is inside):**
- `assets/brand/`: logo, colours, fonts, any brand guide
- `content/mockups/`: product mockups made by the product-mockups skill
- `assets/product/`: product files, real screenshots from inside the product
- `assets/photos/`: headshots, testimonial photos

If the `context/` files are still empty templates, tell the user: "Your business profile is empty. Running $my-business first takes about 15-20 minutes and makes this page much better. Want to do that first, or should I just ask you a few questions now?" Respect their choice.

If there is no mockup in `content/mockups/`, tell them they can run the product-mockups skill first, or you will leave a clearly marked image spot to fill later.

## Step 1: Pick the pages

Ask once: **"Which pages do you want? I recommend the sales page plus the thank-you page. I can also do an upsell page."**

- Default: sales page + thank-you page.
- Upsell page: MOA says add it once the front end has about 5 to 10 sales. If they have fewer, say so in one line, then build it anyway if they still want it (it can be ready before the first buyer).
- Page length: **Lean test page** (Sahil's 4 parts: headline, subheadline, mockup, priced button, plus footer) or **Full sales page**. MOA rule: don't build long copy, FAQ and bonuses before the offer is validated. So **default to the lean test page if they have not made sales yet**, and the full page once the offer has sold. Say why in one line and let them choose.
- Order bump: GHL sets this up inside the order form, not on the page. If they have one, write the bump copy in copy.md for them to paste into GHL.

## Step 2: Fill the gaps

From what you read, list what you already have. Then ask only for missing essentials, one at a time:

1. Offer name
2. Price (and a real "normally" price or value, if they want an anchor)
3. What is inside (each deliverable)
4. Who it is for and the one result it gets them
5. Checkout link, or "leave a placeholder" (use `{{CHECKOUT_URL}}`)
6. Testimonials, if any (word for word, with name and permission)
7. Guarantee, if any (exact terms)

Nice to have, only ask if missing and relevant: logo and brand colours (if `assets/brand/` is empty), a headshot, community link and booking link (for the thank-you page), upsell name, price and contents.

If they say "you choose" on design, use the default tokens in `templates/styles.css` and tell them you did.

## Step 3: Write the copy

Use the MOA rules from `references/moa/`. If those files are thin or missing, use the checklist below. Write in the user's voice, plain words, short lines, no hype words like "revolutionary" or "game-changing".

### Sales page checklist (in this order)

| # | Section | MOA rule |
|---|---|---|
| 1 | **Hero** | Small "for who" line, then headline: outcome first, under 12 words, never starts with their name. Formula: "Discover how to [RESULT] using [METHOD] in [TIMEFRAME]" or "How to [X] without [Y]". Add a timeframe. Subheadline adds specificity, kills the main objection, or stacks the outcome. Mockup. Button with the price on it. |
| 2 | **This is for you if** | 3 to 5 situations, not demographics, in the buyer's own words. Pain buyer: name the pain and relief. Desire buyer: name the vision. |
| 3 | **What you get** | 5 to 7 lines: "[specific deliverable] so you can [outcome] without [pain]". Real screenshots from inside the product beat AI images. |
| 4 | **How it works** | 3 steps. Step 1 takes under 5 minutes. A quick win shows up within 15 minutes. |
| 5 | **Proof** | Real testimonials only. If none yet, keep the section with a visible `[ADD REAL TESTIMONIAL]` placeholder (MOA rule) and tell the user to add real ones before going live, or delete the section if they prefer. Never write a fake one. |
| 6 | **Offer and price** | Value stack (each item and its value), total value, honest anchor ("Normally $97, today $27"), then the price big, then the button again. If the user has no real values for the items, list them as "Included" and drop the total value and anchor rows. Never invent a value. |
| 7 | **Why me** | 2 to 4 lines. Who they help, a real result, why this product exists. Use only facts from `context/`. No photo in `assets/photos/`? Remove the `<img>` and the text goes full width. |
| 8 | **Guarantee** | Only if confirmed. "If you do not [result] in [timeframe], we refund you." |
| 9 | **FAQ** | 4 to 6 real objections (access, time, fit, refund). Skip on a lean page. |
| 10 | **Final CTA + P.S.** | Restate the outcome, the choice, the button, a P.S. recapping outcome, price and guarantee. |
| 11 | **Footer** | Copyright, privacy and terms links, results disclaimer. |

**Button rules:** big, high contrast, first person, action verb, price inside. "Yes, I want the DM Script Pack for $17". Never "Submit", "Click here" or "Buy now" alone. A button must be visible on a phone without scrolling.

**Thank-you page:** headline "You're in! Your [PRODUCT] is on its way." Then 3 steps: 1) access your product, 2) join the community, 3) book a free 15-minute audit call as a bonus (only if they offer one). Add their first quick win. Delete any step they do not have.

**Upsell page:** the best upsell is more of the thing or more help with the thing. Price about 5x the front end ($7 to $37, $17 to $87, $27 to $147). Headline starts with the next result, a clear "Yes" and a polite "No thanks" link. If they want a downsell, MOA says a payment plan on the same product works better than a stripped-down version.

**Order bump copy** (for GHL order form): "Yes! Add [BUMP] for just $[PRICE]", labelled "Highly recommended", 2 to 3 lines with the outcome and an honest anchor. Priced about 1x to 1.5x the front end.

### Save and get approval

Write the copy to `content/pages/<offer-slug>/copy.md` using `templates/copy-template.md`. `<offer-slug>` is the offer name in lowercase with hyphens, for example `dm-script-pack`. If `content/mockups/` already has a folder for this offer, reuse that exact slug so pages, mockups and emails match.

Give 3 headline options and mark your pick. Then tell the user: "Your page copy is ready in content/pages/<offer-slug>/copy.md. Read it and tell me what to change, or say 'looks good' and I will design the page."

Edit copy.md in place for each round of changes. Do not make v2, v3 files.

## Step 4: Build the preview

Only after the copy is approved.

For each page, build from the matching template in `templates/`:
- `sales-page.html`, `thank-you.html`, `upsell.html` (page structure)
- `styles.css` (the design system, goes inside the `<style>` tag)
- `preview-shell.html` (the full document wrapper for the preview)

How to build:
1. Start from the page template. Paste the full contents of `styles.css` inside its `<style>` tag.
2. Set the brand tokens at the top of `.moa-page` (colours and fonts) from `assets/brand/`. Change the font names in the `@import` line too. Keep `@import` as the first line inside `<style>`. If the brand has no fonts, keep the defaults.
3. Replace every `[BRACKET]` with the approved copy. Delete sections the page does not use (no proof, no guarantee, lean page, and so on).
4. Images in the preview use relative paths from the page folder, for example `../../mockups/<offer-slug>/cover-3d.png` or `../../../assets/brand/logo.png`, so the user can see them. Keep the `<!-- REPLACE: ... -->` comment above every image.
5. Put the finished snippet (from `MOA:SNIPPET START` to `MOA:SNIPPET END`) inside `preview-shell.html` and save as `content/pages/<offer-slug>/<page>-preview.html`, where `<page>` is `sales`, `thank-you` or `upsell`.

Design standards: premium and clean, lots of white space, two fonts max, one strong button colour that pops against the background, no heavy animation. Mobile first: the hero mockup is kept short on phones so the priced button shows without scrolling. The sticky buy bar appears once the first button scrolls away.

Do not change the scoping: every CSS rule stays under `.moa-page`. Never style `body`, `html`, or bare tags like `h1` or `a` without the `.moa-page` prefix, or you will break the user's GHL page. No external JS libraries. The only script allowed is the tiny sticky-bar script already in the template.

Tell the user: "Your preview is ready. Open the folder content/pages/<offer-slug>/ and double-click sales-preview.html. It opens in your browser. Check it on your phone size too: make the browser window narrow. Tell me anything you want changed."

Do not run commands to open the browser for them.

## Step 5: Change it until they love it

Apply feedback to the same preview files. One round at a time. Re-check the hard rules after each round. If they change copy, update copy.md too so the two stay in step.

If the user asks what to fix first on an existing page, follow Sahil's order: headline, then price, then button visibility, then who it calls out.

## Step 6: Hand over the GHL paste file

When the user approves the preview:

1. **Images.** List every image the page uses with its local file. Say: "Upload these to GHL: Sites, then Media (or the Media Library inside the page builder). Copy each image link and paste them here, and I will put them in." If they paste links, swap them in. If not, leave the `<!-- REPLACE: ... -->` comments and a clear placeholder `src` so they know exactly which one goes where.
2. **Other links.** The thank-you page uses `{{ACCESS_LINK}}` (product access), `{{NEXT_STEP_LINK}}` (community) and `{{BOOKING_LINK}}` (call booking), the same names the emails use. Swap in real links if the user has them.
3. **Checkout link.** If they gave the real link, use it. If not, every buy button keeps `{{CHECKOUT_URL}}`. In GHL this is normally the URL of the order form step in the same funnel (the next step after the sales page). Tell them to replace `{{CHECKOUT_URL}}` with it (Ctrl+F or Cmd+F in the file).
4. **Write the paste file.** Copy everything between `MOA:SNIPPET START` and `MOA:SNIPPET END` from the approved preview, exactly, swap the image links, and save as `content/pages/<offer-slug>/<page>-ghl-paste.html`. No `<html>`, `<head>` or `<body>` tags in this file.
5. **Final check** before you hand it over:
   - no em dashes or en dashes anywhere
   - no `[BRACKET]` text left in the copy (only the image and link placeholders and any `[ADD REAL TESTIMONIAL]` you listed for the user)
   - the buy button text is readable on the button colour (set `--moa-cta-ink` to dark text if the CTA colour is light, like amber or yellow)
   - every image that isn't uploaded yet has a visible placeholder (a light grey box with its filename), never a broken image icon
   - every buy button points to the same checkout link or `{{CHECKOUT_URL}}`
   - every `<div>`, `<section>` and `<a>` you opened is closed
   - every CSS rule starts with `.moa-page` (except `@import` and `@media` wrappers)
   - no fake proof, no fake urgency
5. **Tell them what is still left to fill**, as a short list (for example: checkout link, 2 image links).

### GHL paste steps (give the user these, in plain words)

1. In GHL, open your funnel (Sites, then Funnels) and open the sales page step in the builder.
2. Add a new section. Set the section and its row to full width and remove the padding, so the page can stretch edge to edge. (Exact setting names can differ by GHL version, check in GHL.)
3. From the elements panel, drag in the **Custom JS/HTML** element (sometimes called "Code").
4. Click it, open the code editor, delete anything inside, and paste the whole of `<page>-ghl-paste.html`. Save.
5. Click Preview to see it. Custom code often does not render fully inside the editor itself, so always judge it in Preview. (Check in GHL.)
6. Set the order form step, then test the whole funnel with GHL's test mode and test card before any ads. Sahil's rule: do a real test purchase first.

Tips to share only if they hit the problem:
- **Page looks boxed in or has side gaps:** make sure the section, row and column are full width with zero padding. If it is still boxed in, add `moa-bleed` next to `moa-page` in the first `<div class="moa-page">` line. (Check in GHL.)
- **Page looks cut off or the element looks short:** check the element has no fixed height setting in GHL. The snippet sets no height of its own. (Check in GHL.)
- **Sticky buy bar does not show:** it is optional. It needs the page script to run, which some GHL settings or parent containers can block. The page works fine without it.
- **Fonts look different:** the fonts load from Google Fonts inside the snippet. If GHL's own font settings override them, tell me and I will make the font rules stronger.
- **Upsell page:** a normal link inside custom HTML cannot charge the saved card. Use two Custom JS/HTML elements (top part and bottom part of the upsell file). **Each part must be complete on its own:** its own `<style>` block (the full scoped CSS) and its own `<div class="moa-page">` wrapper, otherwise the bottom part loses all its styling. Write them as two files, `upsell-ghl-paste-top.html` and `upsell-ghl-paste-bottom.html` and place GHL's own one-click upsell button and "No thanks" link between them, where the file says "GHL YES BUTTON GOES HERE". (Check in GHL.)
- **Thank-you page tracking:** do not paste a pixel into the snippet. Add the Meta Purchase event in the tracking code settings of the thank-you step in GHL, or in their pixel setup. (Check in GHL.)

## Where everything lives

```
content/pages/<offer-slug>/
  copy.md                     approved copy (source of truth for words)
  sales-preview.html          open in browser to view
  sales-ghl-paste.html        paste into GHL Custom JS/HTML element
  thank-you-preview.html
  thank-you-ghl-paste.html
  upsell-preview.html         (if built)
  upsell-ghl-paste.html       (if built)
```

One file per page, edited in place. Never create v1, v2, v3 copies. If the user wants to keep an old version, move it to `archives/`.

## How to end

Tell the user, in plain words:
- which files are ready and where
- what they still need to fill (checkout link, image links)
- the GHL paste steps above
- the next MOA move: test the full funnel with a real test purchase, then get 100+ unique visitors before judging the page. If it sells under 3% after that, fix the headline first.

Offer one natural next step, for example: "Want me to write the order bump copy and the delivery email next?"
