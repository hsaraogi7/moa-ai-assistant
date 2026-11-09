# Email craft for confirmation and abandoned cart emails

Read this before writing. It is the writing standard for `$moa-emails`.

You are writing AS the user (the coach or consultant), in first person, to one buyer. "I" is the user. "You" is one reader. Write like a person typing an email to someone they know, not like a brand.

**The bar:** the user could send it after changing a line or two.

**The question behind every line:** does this help the reader at this exact moment, or does it just look like effort? Anything that only looks like effort comes out. Restraint reads as confidence.

---

## 1. Only true things

- Every price, deliverable, bonus, result, testimonial, quote, date, deadline and guarantee comes from the user or their files. Nothing else.
- No made-up students, results or quotes. A line in quotation marks was really said.
- If you need proof you do not have, make the point through something every reader recognises ("most people who buy something like this...") or leave a `[PLACEHOLDER: add a real testimonial]`.
- Urgency must be real. If there is no real deadline, do not invent one. An honest "this is my last email about it" is enough.
- Numbers stay exactly as true as the source. If the source says "50+", write "50+", not "50".

## 2. How the email reads

- **Open inside a moment.** Not "I hope this email finds you well" or "I wanted to reach out". Start with the thing: "Your order just came through, {{contact.first_name}}, and here's how to get in."
- **Name inside a living first line**, never a bare "Hi {{contact.first_name}}," on its own line. Vary the opener across the sequence.
- **One beat per line.** People read on phones. Short paragraphs, lots of white space.
- **No choppy fragments.** "No fluff. No theory. Just steps." reads like an AI ad. Write "There's no fluff or theory in it, just the steps." Join one thought with "and", "but", "so", a comma or a hyphen.
- **Plain words.** No "transform your business", "take it to the next level", "game-changer", "unlock your potential". If a line could appear in any coach's email, cut it or make it specific.
- **Do not assume they remember.** Name the product and what it does in a few words when you mention it.
- **What they get is stated plainly.** A short list of complete statements, each ending in a full stop. One list per email at most.
- **"..." only before a real pause or reveal.** Not between two plain facts.
- **Emojis add a feeling the words do not already carry.** A few, in the body, on emotional beats. Never one on every line. No full stop before an emoji ("you're in 🎉", not "you're in. 🎉").
- **Bold one or two anchors** (the access line, the key point). Never a whole paragraph.
- **Times:** "7 PM", not "7:00 PM". Always say the time zone for live sessions.
- **Never an em dash or an en dash.** Use a hyphen, a comma or two sentences.

## 3. Subject lines and preview text

- **4-6 words.** Sentence case, not Title Case.
- **Curiosity first.** It should make them need to open, not summarise the email. If someone can guess the whole email from the subject, it is too plain.
- **Mix the styles across a sequence, never the same style twice in a row:**
  - Curiosity: a strange or specific fragment from inside the email ("Did something go wrong? 🤔")
  - Question: something the reader is already asking themselves ("Is this really for you?")
  - Proof: a real name or number does the work (only if real)
  - Plain news: reads like a note from a friend ("Your login is inside")
- **The confirmation email is the exception: clarity wins.** The buyer is looking for their access, so the subject must make it obvious this is the email with their product ("You're in, here's your access 🎉"). Still keep it short.
- **The final cart email can also lean clear** ("Last note about [product]") because by then clarity beats cleverness.
- **Preview text** is the second half of the pull: one short line that adds a detail or raises the stakes. Never a repeat of the subject. Never gives away the whole email.

## 4. Links and CTA

- **One main CTA per email**: ✅ then the action in CAPS and bold, with the link on those words, ending in →
  - Confirmation: ✅ **GET INSTANT ACCESS TO [PRODUCT] →** (linked to `{{ACCESS_LINK}}`)
  - Cart: ✅ **FINISH YOUR ORDER HERE →** (linked to `{{CHECKOUT_URL}}`)
- **The CTA words say what they get when they click**, and make sense to someone who only reads the button. Word it differently in each email.
- **Never a naked URL**, anywhere, including the P.S. Every link sits on words ("tap here", "your login page").
- A longer cart email can link the checkout once inline near the top and once as the ✅ button at the end. Word them differently.
- The ✅ is only for the CTA, never a bullet.

## 5. P.S.

- Written as "P.S.:" with the colon. Not italic.
- Use it only when it earns its place: help for someone stuck ("hit reply if the link doesn't work"), the one next step in the confirmation email, or one last specific in a cart email.
- A P.S. that only repeats the CTA comes out.
- Never a naked link in the P.S.

## 6. Sign-off

- Two short lines: a warm closer in the user's voice, then their name exactly as they gave it.

## 7. Confirmation email specifics

- Access first. The buyer opened this email for one reason. The access link sits in the first 3-4 lines.
- Say exactly what happens when they click (a page opens, they log in with the email they used, a download starts). If it is a login, say which email to log in with and what to do if they cannot.
- Give one quick win they can do today with the product.
- Ask them to reply with one word so the next emails reach the inbox (MOA's own confirmation emails do this).
- Mention the bump only if they bought it (deliver it), and the upsell / next step only if the user has one, in one or two lines at the end or in the P.S. Never let it compete with the access link.
- Never resell the product they just bought.

## 8. Abandoned cart specifics

- **Email 1 (reminder):** short, helpful, no pressure. Assume something got in the way. Offer to help if they hit a problem.
- **Email 2 (objection):** pick the single biggest hesitation for this product and answer it honestly. Do not list five objections.
- **Email 3 (proof / FAQ):** one real result told as that person's result, or 2-3 short Q&As if there is no proof yet.
- **Email 4 (final nudge):** shortest. What they get, why it is worth it, link, and an honest "this is my last email about it".
- **Never discount the main offer.** (MOA rule.)
- Never shame the reader for not buying. Never guilt-trip.
- Each email works on its own, because some readers only open one.

## 9. Formatting for GHL

- Plain text friendly: no tables, no columns, no images required.
- Bold with `**double asterisks**` in the markdown file. The user will apply bold in the GHL editor.
- Links shown as `[words](placeholder)` in the file so the user knows which words to link.
