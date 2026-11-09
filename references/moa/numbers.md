# Numbers: Metrics, Benchmarks, Formulas, Diagnosis

Rule for the assistant: never do the arithmetic in your head when a script or calculator can do it. Show the formula you used. [Source: Action Hub design]

## The metrics, in the order Sahil reads them [Source: Sahil Q&A, MOA S3 slides]
1. Unique outbound clicks (volume). Under 100 = change nothing.
2. CTR (unique outbound CTR) = creative health.
3. CVR (purchases / unique clicks or unique page views) = page and offer health.
4. CPA (spend / purchases) = profit. The north star.
Also track: opt-in rate (two-step form), bump take rate, upsell take rate, AOV. [Source: Sahil Q&A]

## Benchmarks (from the slides unless noted)
| Metric | Target | Action if off |
|---|---|---|
| CTR | over 1% | Under 1%: fix creative (image first, then first line) [S3] |
| Front-end CVR, cold | 3%+ = validated, 5-10% after optimizing | Under 3%: headline, price, button, tracking [S3, S4] |
| Warm test CVR | 10%+ [S2] | Fix the offer or page |
| Warm traffic checkout | 5-10% [Session summaries] | |
| Order bump take | 20-30%, over 30% great [S4, Q&A] | Improve copy, anchor, mockup |
| Upsell 1 take | 10-15% [S4] | Below 5%: change offer or price |
| Downsell take | 5-10% [S8] | |
| Cold outreach conversion | 1-2% [S6] | |
| Inviting warm micro buyers to SSO | 10-30% [S6] | |
| SSO ascension (planning) | 10% of micro buyers [S5] | |
| Live event (planning) | 100 register, 25-30 show, sell about 20% of the room [Q&A] | |

## CPA traffic light [Source: MOA S3 slides]
- Green: CPA under AOV -> scale (20% per 48 hours).
- Yellow: CPA near AOV -> wait until day 7.
- Red: CPA above AOV -> pause once spend hits 3x AOV.

## Data needed before judging [Source: MOA S2-S4 slides, Sahil Q&A]
- Ad / page: 100 unique clicks minimum, 150 better. New offer: 150-200 unique clicks.
- Split test: one variable, full week, 100+ visitors per version.
- Learning phase: days 1-3 don't touch, days 4-7 patterns, day 7+ decide.
- Upsell: after 5-10 front-end sales. First sale can be a fluke.
- AOV: about 30 days of real data.
- Winning ad: 3+ purchases at or below target CPA.

## Formulas
- Daily budget per ad set = AOV x 3 / 7 (e.g. $27 AOV -> about $12 a day). [Source: MOA S4 slides]
- Kill switch = 3 x AOV spent with zero purchases. [Source: MOA S4 slides]
- Validation spend: $20 a day, $100-$150 over 7 days. [Source: MOA S3 slides, Sahil Q&A]
- CTR = unique outbound clicks / impressions. CVR = purchases / unique clicks. CPC = spend / clicks. CPA = spend / purchases. AOV = total revenue (incl. bumps, upsells) / buyers. [Source: Action Hub compute]
- SSO math (slide example): 30 micro buyers a month x 10% ascend x $1,497 = $4,491 extra a month. [Source: MOA S5 slides]
- Goal math: annual cash goal / offer price = clients per year; / 12 = per month; / 52 = per week. Paid buyers needed per month = clients per month / ascension rate (default 10%); / 30 = per day. [Source: Sahil Q&A, Action Hub compute]
- Revenue Blueprint Calculator formulas: ad cost = visitors x CPC; FE sales = visitors x conversion; each layer's sales = FE buyers x take rate; AOV = revenue / new customers; ROAS = revenue / ad cost; customers needed = goal / 12 / AOV; visitors needed = customers needed / FE conversion; ad spend needed = visitors needed x CPC. Levers it shows: 2x traffic, +20% AOV, +1 backend client. [Source: Revenue Blueprint Calculator]
- Calculator defaults are illustrative inputs, NOT benchmarks: 5,000 visitors, $3 CPC, $17 offer at 8%, bump 1 $47 at 40%, bump 2 $17 at 20%, upsell 1 $197 at 10%, upsell 2 $97 at 7%, backend $3,000 at 3%. [Source: Revenue Blueprint Calculator]

## Cost per click context
- Top 6 countries cost more per click than worldwide; Sahil has seen this as normal early on, so a higher CPC there is not a problem by itself. Cheaper clicks often mean other countries. [Source: Sahil Q&A, Action Hub prompts]
- Worldwide brings more failed payments and refunds. [Source: Sahil Q&A]
- A front end that only breaks even can still work when the backend carries the profit; Sahil has seen this. [Source: Sahil Q&A]

## Diagnosis tree (Numbers Doctor) [Source: MOA S3 slides, Sahil Q&A, Action Hub compute]
Check in this order: ad -> page -> tracking -> offer.
1. Under 100 unique clicks -> not enough data, change nothing.
2. CTR under 1% -> AD creative: change the image first, then the first line.
3. CTR fine, CVR under 3% -> PAGE / OFFER / TRACKING: headline, price visible, button above the fold, who it calls out. Check the pixel.
4. Clicks fine but zero opt-ins or sales -> suspect pixel or page, not the ad.
5. CTR + CVR fine, CPA above AOV -> ORDER VALUE: add or fix bump and upsell.
6. All healthy -> hold steady, then scale 20% every 48 hours.

Data integrity checks before trusting any number [Source: Sahil Q&A]:
- Are opt-ins or sales just the member's own test purchases?
- Are Page View, Lead and Purchase events all firing? Is the lead tag applied on opt-in?
- Unique page views or total? (Ad-review crawlers can inflate views right after publishing.)
- Is a 1-step order form hiding opt-ins?
- Are organic and paid traffic mixed in one funnel?

## Scorecards
- 6-question launch scorecard: ad live? 100+ clicks? CTR over 1%? CVR over 3%? a sale? bump live? [Source: MOA S4 slides]
- Weekly log: CPA, AOV, bump rate, SSO leads, plus the date of every change. [Source: MOA S10 slides, Sahil Q&A]

## Output pattern for a numbers review [Source: Action Hub prompts]
What's working first (with their numbers) -> where the leak is (ad, page, tracking, offer) -> the ONE fix -> how long to wait -> log the date.
