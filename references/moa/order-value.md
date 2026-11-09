# Order Value: Bumps, Upsells, Downsells, AOV Stack

## Why
- "Same traffic. More revenue." The front end alone usually can't pay for ads; the stack makes cold traffic profitable. [Source: MOA S8 slides, 1SAD masterclass]
- Slide example: 100 buyers x $7 = $700 -> +30% take a $27 bump = +$810 -> +10% take a $97 upsell = +$970 -> $2,480 total (3.5x, zero extra ad spend). [Source: MOA S4 slides]
- Good CTR + good CVR but no profit -> add a bump. [Source: MOA S3 slides]

## When to add each layer (slides win)
- Order bump: once the front end converts 3%+. [Source: MOA S2 slides]
- Upsells and the full funnel: once the bump converts 20%+. [Source: MOA S2 slides]
- Supporting Q&A guidance: don't add an upsell before about 5-10 front-end sales. "Three can be a fluke. Five is the sweet spot. Seven is better validation. Ten is the greatest." [Source: Sahil Q&A]
- The upsell product doesn't need to exist first. Build the page; after someone buys, build and deliver within 24 hours. [Source: Sahil Q&A]

## The stack at a glance [Source: MOA S8 slides]
| Layer | Price | Target take rate |
|---|---|---|
| Front end | $7-$47 | 3% cold, 5-10% optimized |
| Order bump | $17-$67 (about 1x-1.5x FE) | 20-30% (over 30% is great) |
| Upsell 1 | about 5x FE (ecosystem map: $97-$197) | 10-15% (below 5% change offer or price) |
| Upsell 2 | ecosystem map: $297-$497 | not specified in slides |
| Downsell | payment plan, lite, trial | 5-10% |
Flow: checkout + bump -> Upsell 1 -> YES: Upsell 2 / NO: Downsell -> Thank you. [Source: MOA S8 slides]

## Order bumps
- Checkbox before payment. [Source: MOA S8 slides]
- Good bumps: speed bump (done-for-you, template, prompts), companion resource, extended access. Never unrelated. [Source: MOA S8 slides]
- Bundle bump: 2-3 items at a discount. [Source: MOA S8 slides]
- Price about 1x to 1.5x the front end (same price class). [Source: MOA S5 slides, Sahil Q&A]
- Copy rules [Source: Sahil Q&A]:
  - Title "Highly recommended".
  - Outcome language and a clear benefit (common fault: copy too short).
  - Quantity framing: "you get 4 things".
  - Price anchor: "Normally $97, today only $27" (only if the normal price is real).
  - Add a mockup, break lines properly, make the value obvious.
- If the take rate is strong, you can test raising the bump price. Never touch a bump that is already converting well. [Source: Sahil Q&A]

## Upsells
- One-click (card already stored). Needs Stripe or PayPal. [Source: MOA S8 slides, Sahil Q&A]
- Best upsells: more of the thing, or more help with the thing. [Source: MOA S8 slides]
- 5x rule: $7 -> $37, $17 -> $87, $27 -> $147, $47 -> $247. [Source: MOA S8 slides] (The slides win over the "3x-10x" range in one call summary.)
- Upsell price must fit: $37 after a $17 front end is bump pricing, not upsell pricing. Raise perceived value to $67-$97 or sell it separately. [Source: Sahil Q&A]
- Big jumps lower the take rate, which can be fine: 5% on a big jump is acceptable, 8-10% is the aim. [Source: Sahil Q&A]
- A paid strategy call can work as an upsell; keep the price flow gradual, "not a crazy jump". [Source: Sahil Q&A]
- Two valid upsell sequences: high-low-highest, or low-high-higher. "Both work, pick one." [Source: Sahil Q&A]
- Burger + fries (bump, same class) vs meal combo (upsell, bigger package). [Source: Sahil Q&A]

## Downsells
- Shown to people who say no to the upsell. "No often means not at that price." [Source: MOA S8 slides]
- Slide options: payment plan (e.g. 3x$57 for $147), feature-stripped (40-50% of price), free trial. [Source: MOA S8 slides]
- Sahil's tested lesson: a stripped-down half version converted badly. Prefer a payment plan on the same product, or a coupon to get the rest after they buy the small one. [Source: Sahil Q&A]

## Abandoned cart link
- Keep a standalone upsell page so abandoned-cart emails can link to it. [Source: MOA S8 slides]
- Never discount the main offer in abandoned-cart emails. See emails.md. [Source: Sahil Q&A]

## Estimating AOV
- Real AOV needs about 30 days of data. Before that, model bad / good / excellent scenarios. [Source: Sahil Q&A]
- Use the Revenue Blueprint Calculator (offer-analyzer-kit.lovable.app) to model the stack. See numbers.md. [Source: Revenue Blueprint Calculator]

## Stack review scorecard [Source: Action Hub prompts]
| Row | Green when |
|---|---|
| Bump price | About 1x-1.5x the front end, related to it |
| Bump take rate | 20-30%+ |
| Upsell price | About 5x the front end, bigger package |
| Upsell take rate | 10-15% (5% acceptable on a big jump) |
| Flow of prices | Gradual, logical order, no "crazy jump" |
Rules: never touch what already converts. One fix, in Sahil's order (headline, price, bump, upsell, button, layout).

Output patterns [Source: Action Hub prompts]:
- Bump request: 3 ideas (name, contents, price at 1x-1.5x, checkout copy with "Highly recommended", "you get N things", price anchor), pick one, target 20-30%, next move = add it and wait for 100-150 views.
- Upsell request: 3 ideas at about 5x (name, contents, price, page headline) + a payment-plan downsell. If under 5 front-end sales, say wait.
