# GHL setup note (template for `ghl-setup.md`)

Use this to write the short setup note saved next to the emails. Fill in the offer's details. Keep it plain and short.

**Honesty rule:** GoHighLevel changes its menus often and accounts differ. Only name a menu, trigger or action if you are sure it exists. Mark everything else "check in GHL". It is better to say "look for a trigger that fires when an order is paid" than to give a menu name that is wrong.

---

## What MOA material says about the setup

- Use a **2-step order form** (name and email on step 1, payment on step 2). Without step 1 you cannot see who started checkout, so you cannot run abandoned cart.
- Tag people on step 1 as leads, and tag them as buyers when they pay. Then "lead tag but no buyer tag" = abandoned cart. (MOA's own funnels run this way: a `-lead` tag on opt-in, a `-buyer` tag on purchase, plus a separate tag for bump buyers.)
- Run a **test purchase** before going live (test mode in the funnel settings, Stripe test card 4242 4242 4242 4242) and check that the delivery email arrives and the tags fire.

---

## Note template

```
# GHL setup - [Product name]

## 1. Confirmation email
Trigger: when an order for [Product name] is paid.
- In GHL Workflows, look for an "Order Submitted" or payment-type trigger
  and filter it to this product / funnel. (check in GHL: the exact trigger
  names and filters in your account)
- Alternative: trigger on the buyer tag "[product]-buyer" being added, if
  your funnel already adds it on purchase.
Action: send email -> paste confirmation.md.
Optional: if bump buyers get a tag like "[product]-bump-buyer", add an
If/Else branch and send the bump version to them. (check in GHL)

## 2. Abandoned cart sequence
Trigger: someone submits step 1 of the order form (name + email) for
[Product name].
- Look for an order form / form submission trigger tied to this funnel step,
  or trigger on the lead tag "[product]-lead" being added. (check in GHL)
Steps:
1. Wait [30 minutes]
2. Check: has this contact bought? (If/Else on the buyer tag or on an order
   for this product.) If yes -> end the workflow. If no -> send Email 1.
3. Wait [~24 hours] -> same check -> Email 2
4. Wait [~24 hours] -> same check -> Email 3
5. Wait [~24 hours] -> same check -> Email 4
Also: GHL workflows may have a "goal" setting that removes a contact the
moment they buy. If you see it, set it to "buyer tag added" or "order
paid" as a safety net. (check in GHL)

## 3. Before you switch it on
- Replace every {{ACCESS_LINK}}, {{CHECKOUT_URL}} and {{NEXT_STEP_LINK}}
  with your real links. These are not GHL fields.
- Insert the first name from GHL's merge field picker so it matches your
  account (normally {{contact.first_name}}).
- Send yourself a test: start checkout and stop at step 2, then wait for
  Email 1. Then do a full test purchase and check the confirmation arrives
  and the cart emails stop.
- Make sure the "from" name and email are yours and your sending domain is
  set up, so emails do not land in spam. (check in GHL)
```

---

## When the user asks for help inside GHL

Walk them through it one step at a time and ask them to tell you what they see on screen. If what they see does not match what you expected, believe their screen, not your memory. Suggest GHL's own help docs or support for anything you cannot confirm.
