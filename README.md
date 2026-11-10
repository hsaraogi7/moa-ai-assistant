# MOA AI Assistant

**A 6FA x BM build** - Six Figure Accelerator x Bloody Marketers

Your own AI executive assistant for running a one-person business. It learns your business once, remembers it every session, and helps with any task you hand it: planning your week, thinking through a decision, drafting posts and messages, replying to customers, research.

On top of that, it comes with 4 ready-made skills for your micro offer, built on Sahil's MOA method:

- **Product mockups** - ebook and toolkit covers, 3D shots, device screens, bundle images
- **Sales page** - written and designed for you, delivered as copy-ready HTML for GoHighLevel
- **Confirmation email + abandoned cart sequence** - ready to drop into your GHL workflows
- **Ad images** - bring a reference ad (and your copy if you have it), get finished Meta ad images

This isn't a chatbot. It's a workspace your assistant lives inside, with your offer, your brand, your voice and the MOA playbook built in.

**What's included and what isn't:** the 4 micro offer skills are the ready-made part. For everything else (planning, content, customer replies) just ask in plain English and it works from what it knows about you. It does not connect to your email inbox or calendar out of the box.

**The names:** MOA = Micro Offer Accelerator, Sahil Sehgal's program. 6FA = Six Figure Accelerator, Sahil's company. BM = Bloody Marketers, the agency that built this workspace.

---

## What you need
- A **ChatGPT Plus** plan or higher (image generation is not on the free plan)
- The **ChatGPT desktop app** (Codex lives inside it), on Mac or Windows
- 25-30 minutes for the setup interview (31 short questions)
- **No API key needed.** Images are made with ChatGPT's built-in image generation, included in your plan. Making images uses up your plan's Codex limit faster than text does, so pick your angles first, then generate.

**About the backup image script (most people never need it):** `scripts/generate_image.py` is a spare way to make images, only for when built-in image generation isn't working for you. It talks to OpenAI directly using an OpenAI API key. An API key is a separate account at https://platform.openai.com with its own pay-per-image billing, not covered by ChatGPT Plus. Check current prices at https://openai.com/api/pricing before using it. If built-in images work, ignore this script.

## Setup (one time, about 5 minutes plus the interview)

**1. Install the ChatGPT desktop app**
- **Mac:** download it from https://learn.chatgpt.com/docs/app and drag it into Applications.
- **Windows:** install it from the Microsoft Store using this link: https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi . Don't search the Store for "Codex" by name, an unrelated app can come up.
- **Windows only:** also install Git from https://git-scm.com/download/win (just click Next through the installer).

**2. Make an empty folder** on your computer, for example `Documents/My AI Assistant`.

**3. Open it in Codex**
- Open the ChatGPT desktop app, sign in, and switch to **Codex**.
- Go to **Projects**, choose to open a local folder, and pick the folder you just made.
- Start a **new chat** inside that project.

**4. Paste the setup prompt below** and press Enter. If it asks permission to download or create files, approve it.

```
Set up my AI assistant in this folder.

1. Download this workspace into the current folder:
   https://github.com/hsaraogi7/moa-ai-assistant/archive/refs/heads/main.zip
   - Unzip it, then move everything from inside the "moa-ai-assistant-main" folder into this folder, INCLUDING hidden files and folders like ".agents" (that's where the skills live). Then remove the zip and the empty "moa-ai-assistant-main" folder.
   - Use whatever works on my computer. Mac: curl + unzip. Windows: curl + tar -xf, or PowerShell Invoke-WebRequest + Expand-Archive.
   - If this folder already has files in it, don't overwrite anything. Tell me first.
2. Check it worked: this folder should now have AGENTS.md, README.md, context/, memory/, references/moa/ and .agents/skills/ with 5 skills (my-business, product-mockups, build-page, moa-emails, ad-images). Tell me if anything is missing.
3. Read AGENTS.md and README.md, then give me a short summary in plain English:
   - What you are and what you can help me with
   - The 5 skills, one line each
   - What happens next
   Keep it under 15 lines. No technical jargon.
4. Then start my setup interview right away by following .agents/skills/my-business/SKILL.md exactly. One question at a time.
```

That's it. It downloads everything, tells you what it is, and starts the interview. Answer one question at a time. Talking is faster than typing: a voice-to-text tool like [Wispr Flow](https://wisprflow.ai/r?HARSH1055) helps a lot. When it asks, drop your logo into `assets/brand/`, 2-3 photos of you into `assets/photos/`, and screenshots of your product into `assets/product/`.

When the interview is done, your assistant updates all its files, shows you what it learned, lists what it can do, and asks what you want to do first.

**Prefer to download by hand?** Click the green **Code** button on this page, then **Download ZIP**. Unzip it and open the `moa-ai-assistant-main` folder as your project in Codex. Then type `$my-business` (or `@` / `/skills` and pick **my-business**, or just say "run my business setup").

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
| `scripts/generate_image.py` | Backup image generator, only if built-in images don't work for you (needs a paid OpenAI API key, see "What you need") |
| `decisions/`, `archives/`, `temp/` | Decision log, old work, scratch files |

## Tips
- Tell it "remember that..." and it saves it for every future session.
- Offer changed? Run `$my-business` again.
- Never let it invent testimonials or results. It's told not to, but always check.

---

Built by **Bloody Marketers** for **Six Figure Accelerator's** Micro Offer Accelerator.
