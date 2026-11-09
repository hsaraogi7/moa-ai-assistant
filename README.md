# MOA AI Assistant

**A 6FA x BM build** - Six Figure Accelerator x Bloody Marketers

Your own AI assistant for the **Micro Offer Accelerator**. It learns your business once, then helps you build and sell your micro offer using Sahil's MOA method:

- **Product mockups** - ebook and toolkit covers, 3D shots, device screens, bundle images
- **Sales page** - written and designed for you, delivered as copy-ready HTML for GoHighLevel
- **Confirmation email + abandoned cart sequence** - ready to drop into your GHL workflows
- **Ad images** - bring a reference ad (and your copy if you have it), get finished Meta ad images

This isn't a chatbot. It's a workspace your assistant lives inside, with your offer, your brand, your voice and the MOA playbook built in.

---

## What you need
- A **ChatGPT Plus** plan or higher (image generation is not on the free plan)
- The **ChatGPT desktop app** (Codex lives inside it), on Mac or Windows
- 20 minutes for the setup interview

## Setup (one time)

**1. Install the ChatGPT desktop app**
- **Mac:** download it from https://learn.chatgpt.com/docs/app and drag it into Applications.
- **Windows:** install it from the Microsoft Store using this link: https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi . Don't search the Store for "Codex" by name, an unrelated app can come up.
- **Windows only:** also install Git from https://git-scm.com/download/win (just click Next through the installer).

**2. Download this workspace**
- On this GitHub page, click the green **Code** button, then **Download ZIP**.
- Unzip it and move the folder somewhere you'll keep it (Documents is fine).

**3. Open it in Codex**
- Open the ChatGPT desktop app, sign in, and switch to **Codex**.
- Open the `moa-ai-assistant` folder you just unzipped as your project.

**4. Run the setup interview**
- Type: `$my-business` (if that doesn't pop up, type `@` or `/skills` and pick **my-business**, or just say "run my business setup")
- Answer one question at a time. Talking is faster than typing: a voice-to-text tool like [Wispr Flow](https://wisprflow.ai/r?HARSH1055) helps a lot.
- When it asks, drop your logo into `assets/brand/`, 2-3 photos of you into `assets/photos/`, and screenshots of your product into `assets/product/`.

That's it. Your assistant now knows you, your offer and your brand.

---

## Build your funnel, in this order

| Step | Type this | What you get |
|---|---|---|
| 1 | `$product-mockups` | Cover, 3D shots, device and bundle images in `content/mockups/` |
| 2 | `$build-page` | Sales page + thank-you page, preview first, then a GHL paste file per page |
| 3 | `$moa-emails` | Confirmation email + abandoned cart sequence in `content/emails/` |
| 4 | `$ad-images` | Ad images + Meta copy in `content/ads/` |

You can also just ask in plain English ("make my sales page") and the assistant will pick the right skill.

### Putting your page into GoHighLevel
1. Upload your images (mockups, photos, logo) to your GHL **Media** library and copy their links.
2. Ask your assistant: "Here are my image links, swap them into the page." Paste the links.
3. Open `content/pages/<your-offer>/sales-ghl-paste.html`, copy everything.
4. In your GHL funnel step, drag in a **Custom JS/HTML** element (sometimes called "Code") and paste. Save and preview.

### Making ad images
- Drop an ad you like into `assets/reference-ads/` (or hold Shift and drag it into the prompt box).
- Have copy already? Paste it in. No copy? Your assistant writes angles from your offer and the MOA playbook, you pick one, then it designs.
- Images use Codex's built-in image generation, which uses up your Codex limit faster than text. Pick angles first, then generate.

---

## What's inside

| Folder / file | What it is |
|---|---|
| `AGENTS.md` | Your assistant's brain. Codex reads it every session |
| `context/` | Your business, offer, brand, priorities (filled by `$my-business`) |
| `memory/` | What your assistant remembers across sessions |
| `references/moa/` | Sahil's MOA method. Every page, email and ad is grounded in this |
| `.agents/skills/` | The 5 skills |
| `assets/` | Your logo, photos, product screenshots, reference ads |
| `content/` | Everything your assistant makes |
| `scripts/generate_image.py` | Backup image generator if built-in images ever don't work for you (needs an OpenAI API key) |
| `decisions/`, `archives/`, `temp/` | Decision log, old work, scratch files |

## Tips
- Tell it "remember that..." and it saves it for every future session.
- Offer changed? Run `$my-business` again.
- Never let it invent testimonials or results. It's told not to, but always check.

---

Built by **Bloody Marketers** for **Six Figure Accelerator's** Micro Offer Accelerator.
