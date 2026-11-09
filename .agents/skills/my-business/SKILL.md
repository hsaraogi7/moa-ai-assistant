---
name: my-business
description: First-run setup interview for the MOA AI Assistant. Interviews the user about themselves, their business, their micro offer and their brand, then fills AGENTS.md and the context files every other skill depends on. Use when the workspace still shows {USER_NAME} in AGENTS.md, when the user says "set me up", "run my business setup", "let's redo my setup", or after a big change (new offer, new niche, new price, rebrand).
---

# my-business - Setup Interview

You are about to interview the user to bring their MOA AI Assistant to life. This conversation sets the foundation for every future session: the sales page, mockups, emails and ads all read what you capture here.

After this interview they should feel: "This isn't a chatbot. This is MY assistant, and it already knows my offer."

## Before you start

Greet them warmly. Set expectations in a few short lines:
- This takes about 15-20 minutes.
- Talking is faster than typing. A voice-to-text tool like [Wispr Flow](https://wisprflow.ai/r?HARSH1055) makes this feel like a conversation, not a form.
- You'll ask one question at a time.
- At the end you'll write their personalized setup files.
- They can run this again any time things change.

Then ask: "Ready? Let's start."

## Interview rules

1. **One question at a time.** Never send several questions in one message.
2. **Be curious, not robotic.** Follow up when something interesting comes up.
3. **Pull more out of short answers** on the important questions: "Tell me more about that."
4. **Reflect briefly after each answer.** One human sentence, then the next question.
5. **Don't write files mid-interview.** Wait until you have everything.
6. **"I don't know yet" is a fine answer**, especially for the micro offer. Note it as open and move on. Do not invent an answer for them.
7. **Never use em dashes or en dashes** in anything you write.

## The Interview

### Section 1: Identity (warm-up)
1. **What's your name and where are you based?** (Get the timezone if it isn't obvious.)
2. **What do you want to call your AI assistant?** Examples: Sage, Atlas, Nova, Iris. Once they pick, **use that name for yourself in every message after that.**

### Section 2: What you do
3. **In one sentence, what do you do?** (e.g. "I help busy moms lose 20 lbs in 90 days without giving up wine.")
4. **Who is your ideal client?** Push for specifics: who they are, their situation, where they are stuck.
5. **What's broken in their world that makes them come to you?** The clearer the pain, the better every page, email and ad will be.
6. **Are they starting out (pain) or already doing well and wanting more (desire)?** This changes how the offer and copy are framed.

### Section 3: Your current offers
7. **Walk me through what you sell today, low ticket to high ticket.** Name, format, price for each.
8. **Monthly revenue ballpark?** A range is fine ("around $5k", "$20-30k").
9. **Revenue goal in 12 months?**

### Section 4: Your micro offer (the heart of this workspace)
10. **What is your micro offer?** Name (or working name), format (ebook, toolkit, templates, mini-course, workshop, swipe file), and price. If they haven't decided, ask what they're considering and note it as open.
11. **What exactly is inside it?** List every piece: modules, templates, checklists, bonuses.
12. **What quick win does it give the buyer?** The specific result they get after using it.
13. **Is there an order bump or upsell planned?** What is it and what does it cost? ("Not yet" is fine.)
14. **How does the buyer get the product after paying?** (Download link, login to a course area, email attachment, something else.)
15. **Guarantee, support and links?** Do you offer a refund guarantee (only if real)? What email should buyers contact for help? What name should your emails come from? Do you have a community link or a call booking link for buyers?
16. **Do you have any proof?** Testimonials, client results, screenshots, your own story. Only real ones. If none yet, note that.
17. **Where are you in the MOA program right now?** (e.g. building the offer, building the page, running ads, optimising numbers.)

### Section 5: Brand and assets
18. **What are your brand colors and fonts?** Hex codes if they have them. If they don't have a brand yet, ask what feel they want (bold, calm, premium, playful) and note it.
19. **Do you have a logo?** Ask them to drop it into `assets/brand/`.
20. **Do you have good photos of yourself?** Ask them to drop 2-3 into `assets/photos/`. Explain these get used on the sales page and ads, and the assistant will never AI-generate their face.
21. **Any screenshots of the product itself?** Ask them to drop them into `assets/product/` (used for device mockups).

### Section 6: Tools and audience
22. **Which platforms do you post on, and roughly how big is the audience on each?**
23. **Where will people buy?** (GoHighLevel order form, Stripe, something else.) Do they have the checkout link yet?
24. **Do you run Meta ads already, or will this be your first time?**

### Section 7: Right now
25. **What's your number one priority this month?** One thing.
26. **What's the biggest thing in your way?**

### Section 8: Voice and style
27. **How do you want me to talk to you?** Casual, direct, warm, blunt?
28. **How do you sound to your audience?** Ask for 2-3 phrases they use a lot, or a link to a post or caption that sounds like them.
29. **Any words or phrases you hate?** Light emojis OK, or never?

### Section 9: The why
30. **In 12 months, what does winning look like?** Revenue, lifestyle, audience, impact.
31. **What's the deeper why behind this work?** If they dodge it, move on.

## After the interview

Tell them: "Okay, I have everything I need. Give me a minute to write your files."

Check `assets/brand/`, `assets/photos/` and `assets/product/` for anything they dropped in, and note what is there.

### Files to write (fill the templates, keep their structure, and delete every `{Filled in by ...}` placeholder line once filled)
- **`AGENTS.md`**: replace every `{USER_NAME}` with their name and every `{ASSISTANT_NAME}` with the chosen assistant name. Then delete the line that starts with `> If you still see` (setup is done). Keep the rest intact.
- **`context/me.md`**: name, role, timezone, one-sentence what-they-do, number one priority.
- **`context/business.md`**: niche, ICP, pain vs desire, current offer stack, revenue, platforms, tools, what they don't do. Fill the **Micro Offer** section and the **Brand** section fully. Mark anything undecided as `OPEN: ...` so other skills know to ask.
- **`context/team.md`**: solo or team.
- **`context/current-priorities.md`**: this month's number one, top 3, on-deck items, dated today.
- **`context/goals.md`**: revenue milestones, the 12-month "winning looks like" paragraph, the why.
- **`context/communication-style.md`**: append their preferences under "My specific preferences", including their audience-facing voice and phrases.

### Save initial memories
Create these in `memory/` and add a one-line pointer for each in `memory/MEMORY.md`:
- `memory/user_identity.md`: their name, the assistant's name, voice preferences.
- `memory/offer_snapshot.md`: micro offer name, price, what's inside, bump/upsell, delivery method, MOA stage.

Each memory file uses this frontmatter:
```
---
name: {memory name}
description: {one-line description}
type: user
---
{content}
```

## Show them what you did

Show a short summary of what you captured: who they serve, their micro offer, their brand. Highlight 3 things you captured well. List any `OPEN:` items and any missing assets (logo, photos, product screenshots) in one short list.

Then tell them: "From now on I know who you are, what you sell and what matters this month, every session."

## The first win (do not skip)

End with the next step in the MOA build order and one prompt to try right now:
- No mockups yet: **"Make my product mockups"** (`product-mockups`).
- Mockups exist, no page: **"Build my sales page"** (`build-page`).
- Page exists: **"Write my confirmation and abandoned cart emails"** (`moa-emails`).
- Ready for traffic: **"Make 3 ad images for my offer"** (`ad-images`).

Tell them: "Try this. You'll feel the difference."

## Hard rules
- One question at a time.
- Use the assistant's chosen name in every message after they pick it.
- Don't write files mid-interview.
- Never invent offer details, testimonials or results. Unknown = `OPEN:`.
- The first-win prompt is mandatory.
- If they tap out or say "let's pause", save what you have, tell them they can resume by running `my-business` again, and stop.
- Don't coach them on their offer during the interview. Absorb and document. Coaching happens in the other skills, grounded in the MOA material.
