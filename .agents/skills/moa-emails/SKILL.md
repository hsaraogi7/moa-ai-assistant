---
name: moa-emails
description: Write the two emails every micro offer needs in GoHighLevel (GHL) - the purchase CONFIRMATION email (order confirmed, how to get the product, the one next step) and the ABANDONED CART sequence (people who started checkout and did not buy). Use when the user says "write my confirmation email", "thank you email", "delivery email", "abandoned cart emails", "cart recovery", "people are not finishing checkout", or "set up my order emails". Only these two jobs. For anything else (nurture, broadcasts, launches) say this skill does not cover it.
---

# $moa-emails - Confirmation + Abandoned Cart emails (6FA x BM)

You write two things for a coach or consultant selling a low-ticket micro offer through GoHighLevel:

1. **The confirmation email** - sent right after someone buys.
2. **The abandoned cart sequence** - sent to people who started checkout (gave name and email on step 1) but did not pay.

Nothing else. If the user asks for a nurture sequence, a broadcast, a launch series, ad copy or email angles, tell them plainly that this skill only writes confirmation and abandoned cart emails, and stop.

The user is not technical. Talk in plain English, ask short questions, explain GHL steps simply, and never pretend to know a GHL menu name you are not sure of.

---

## HARD STYLE RULE

**Never use an em dash or an en dash, anywhere.** Not in the emails, subject lines, preview text, notes, file names or your chat replies. Use a hyphen (-), a comma, a colon, or split the thought into two sentences. Check every draft for them before saving.

---

## Step 1: Read before you ask

Read these files in full if they exist. Skip any that do not exist, do not invent their contents.

1. `context/business.md`, `context/me.md`, `context/current-priorities.md` - the user's business, offer stack, audience and name. These are filled in by `$my-business`. If `context/business.md` is still an empty template, suggest running `$my-business` first, but you can still continue by asking the essentials below.
2. `references/moa/offer.md` - how MOA thinks about micro offers, bumps and upsells.
3. `references/moa/emails.md` - MOA's guidance on these emails. **Its MOA hard rules (marked as Sahil's) win over anything in this skill.** The "team draft patterns" and "general best practice" sections in it are inspiration only and do not override this skill.
4. `references/moa/voice.md` - how the emails should sound.
5. `references/craft.md` (inside this skill folder) - the writing rules. Read it every time.
6. `references/ghl-setup.md` (inside this skill folder) - how to explain the GHL setup.
7. Any existing emails in `content/emails/` for this offer, so you do not repeat yourself or contradict what is already live.

**Facts come only from these files and from what the user tells you.** Never invent a price, a bonus, a result, a testimonial, a deadline, a guarantee or a name. If you need something you do not have, ask or leave a clear `[PLACEHOLDER]`.

---

## Step 2: Ask only what is missing

After reading, list what you still do not know from this checklist and ask ONLY those, in one short message (numbered, max 8 questions). Give a suggested answer where you can, so the user can just say "yes".

- **Product name** (exactly as on the sales page)
- **Price** (and currency)
- **What they get** (the deliverables, in one or two lines)
- **How access is delivered**: a link to a page or Google Doc, a login to a members area / GHL course, an attachment, or a live session (date, time, time zone, Zoom link)
- **Checkout link** (the order page URL, for the cart emails)
- **Order bump and upsell**: is there one? Name, price, and how it is delivered if bought
- **Next step after buying**: community, a free call, the upsell page, or nothing (MOA suggests a simple 3-step next step on the delivery side: access the product, join the community, book a call. Use only the ones the user actually has.)
- **Sender name** and **sign-off**
- **Tone**: warm and casual, or direct and short (default: match `references/moa/voice.md` and the user's own writing)
- **Guarantee or refund policy**, only if they have one (never invent one)

If the user says "just write it", write it with `[PLACEHOLDER]` for what is missing and list the gaps at the end.

---

## Step 3: Plan before writing

### Confirmation email (1 email, sometimes 2)

Its jobs, in this order:
1. **Reassure**: the order went through, they made a good decision.
2. **Deliver**: exactly how to get the product, with the access link on words. This must be impossible to miss and should sit near the top.
3. **Quick win**: one small thing they can do in the next 10 minutes with the product.
4. **One next step**: only if the user has one (community, call, upsell page). Keep it secondary, usually in the P.S. The product access always comes first.
5. **Deliverability**: ask them to reply with one word (MOA uses "CONFIRMED") so future emails land in the inbox. MOA's own confirmation emails use this.

If there is an order bump, deliver it too. If the user's GHL can tell bump buyers apart (a separate tag or product), suggest a second version of the confirmation for bump buyers, or one email with a clear line for the bump. Ask which they prefer.

### Abandoned cart sequence (default 4 emails)

**Recommended timing.** Tell the user this is a recommendation, not a fixed rule, and that the MOA hard rules in `references/moa/emails.md` win if they say otherwise.

| # | When | Angle | Why this timing |
|---|---|---|---|
| 1 | ~30 min after step 1, no purchase | **Helpful reminder**: "did something go wrong?" Card issue, page timed out, got pulled away. Link straight back to checkout. | They still remember the page. MOA material uses 20-30 min for this email. |
| 2 | ~24 hours later | **Objection handling**: answer the biggest reason people hesitate (price, time, "will this work for me"). | They have slept on it. Doubts are now the blocker, not the tech. |
| 3 | ~48 hours later | **Proof and FAQ**: a real result or testimonial (only if the user has one), plus 2-3 short answers to common questions. | Proof works once they are thinking about it seriously. |
| 4 | ~72 hours later | **Final nudge**: honest, short, last email about this offer. Name what they get, link to checkout. | Ends the sequence cleanly so the list is not annoyed. |

Adjust the plan when it makes sense, and say why:
- **Very cheap offer** (under ~$10): 3 emails can be enough (drop email 3 or merge it into 2).
- **Live event offer** (workshop, masterclass): time the emails to the event date, and the last one goes out a few hours before it starts. Never send cart emails after the event if the product no longer exists.
- **No proof yet**: email 3 becomes an FAQ email only. Never fake proof.

**Rules for the sequence:**
- **Never discount the main offer in abandoned cart emails.** This is a MOA rule. It trains buyers to abandon carts on purpose.
- **Never invent urgency.** Only mention a deadline or price change if the user confirms it is real.
- **Every email links back to the checkout** with `{{CHECKOUT_URL}}`.
- **Each email has a different angle, opener, subject style and length.** They must not read like one template four times.
- **The sequence stops the moment they buy.** Tell the user how in the GHL note (see `references/ghl-setup.md`).

Share the plan in 3-5 lines before writing if the user seems unsure. If they already gave you everything, write straight away and include the plan at the top of the file.

---

## Step 4: Write the emails

Follow `references/craft.md` for every line. The essentials:

- **Format for each email:**
  ```
  ## Email #N - [angle]
  **Send:** [timing]
  **Subject:** ...
  **Preview text:** ...

  [body]

  [CTA]

  [sign-off]

  P.S.: ... (only if it earns its place)
  ```
- **Subject lines: 4-6 words, curiosity first.** Not a summary of the email. Different style for each email.
- **Preview text**: one short line that adds to the subject, never repeats it.
- **First line uses the name inside a real sentence**: `{{contact.first_name}}`, not a bare "Hi {{contact.first_name}},".
- **No naked links.** Every link sits on words. Use placeholders: `{{ACCESS_LINK}}` for the product, `{{CHECKOUT_URL}}` for checkout, `{{NEXT_STEP_LINK}}` for the community / call / upsell page.
- **One main CTA per email**, written as: ✅ **ACTION IN CAPS ON THE LINKED WORDS →**
- **No choppy fragments.** Join one thought with "and", "but", "so" or a comma instead of breaking it into punchy bits.
- **Emojis**: a few, where they add feeling. Never on every line.
- **Plain text friendly**: short lines, white space, no tables, no images required for the email to make sense.
- **Short.** Confirmation: under ~200 words. Cart emails: 80-200 words each, the final one shortest.
- **No em dashes or en dashes.**

**Merge fields:** use `{{contact.first_name}}` for the first name. Add this note in the file: "Check the first name field in your GHL: insert it from the merge field / custom values picker in the GHL email editor rather than typing it, so the spelling matches your account. `{{ACCESS_LINK}}`, `{{CHECKOUT_URL}}` and `{{NEXT_STEP_LINK}}` are NOT GHL fields, replace them with your real links before sending, or GHL may send them blank."

---

## Step 5: Self-review before handing over

Fix anything that fails. Do not hand over a draft with a known failure.

1. Any em dash or en dash anywhere? Remove.
2. Is every fact (price, deliverables, bonus, result, quote, deadline, guarantee) from the user or their files? Anything else becomes a `[PLACEHOLDER]` or comes out.
3. Confirmation: is the access link near the top and impossible to miss? Does it say exactly what to click and what happens next?
4. Cart emails: does each one link to `{{CHECKOUT_URL}}`? Is there zero discount on the main offer and zero fake urgency?
5. Subject lines 4-6 words, curiosity, a different style for each email?
6. Any naked URL, including in the P.S.? Put it on words.
7. Any two short sentences that are really one thought? Join them.
8. Does each email have one main CTA, in the ✅ CAPS → format?
9. Do the 4 cart emails each feel different (opener, angle, length)? Read them back to back.
10. Read each email as a buyer on a phone. Does every emoji and bold add something? If not, remove it.
11. Is the tone a match for `references/moa/voice.md` and the user's own words?
12. Is the GHL note clear about what to check, and does it avoid made-up menu names?

---

## Step 6: Save and hand over

Save to `content/emails/<offer-slug>/` (slug = product name in lowercase with hyphens, e.g. `content/emails/7-day-content-kit/`; if `content/pages/` or `content/mockups/` already has a folder for this offer, reuse that exact slug):

1. `confirmation.md` - the confirmation email (and the bump-buyer version if written).
2. `abandoned-cart.md` - the plan table at the top, then each email.
3. `ghl-setup.md` - the short setup note, built from `references/ghl-setup.md` and filled in with this offer's details (product name, tags, timings).

If files already exist for this offer, ask before overwriting, or save as a new dated file (e.g. `abandoned-cart-2026-11-10.md`).

Then reply in chat with:
- Where the files are.
- The cart sequence plan in 3-4 lines (timing + angle).
- Anything still marked `[PLACEHOLDER]` that they need to fill in.
- The 2-3 things to check in GHL before turning the workflows on, including sending a test order to themselves.

Keep the reply short. The emails live in the files, not in a long chat message.
