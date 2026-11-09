#!/usr/bin/env python3
"""Backup image generator for the MOA AI Assistant (6FA x BM).

You only need this if Codex's built-in image generation ($imagegen) is not
available to you. It calls the OpenAI Images API with your own API key.

Setup (one time):
  1. Create an API key at https://platform.openai.com/api-keys
  2. Create a file called .env in the workspace root with this line:
       OPENAI_API_KEY=sk-...
     Optional, if your account uses a different image model name:
       OPENAI_IMAGE_MODEL=gpt-image-2

Usage (on Windows type `python` or `py` instead of `python3`):
  New image from a prompt:
    python3 scripts/generate_image.py --prompt "..." --out content/ads/test/ad-1.png

  Image using reference images (style reference, product mockup, your photo):
    python3 scripts/generate_image.py --prompt "..." --ref assets/reference-ads/ad.png --ref content/mockups/x/cover-flat.png --out content/ads/test/ad-1.png

  Sizes: 1024x1024, 1024x1536 (portrait), 1536x1024 (landscape). Default portrait.

Only uses the Python standard library, nothing to install.
"""
import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid

API = "https://api.openai.com/v1/images"


def load_env():
    here = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(os.path.dirname(here), ".env")
    if os.path.exists(env_path):
        with open(env_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def multipart(fields, files):
    boundary = uuid.uuid4().hex
    body = bytearray()
    for name, value in fields.items():
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode()
    for name, path in files:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as f:
            data = f.read()
        body += (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; "
            f"filename=\"{os.path.basename(path)}\"\r\nContent-Type: {mime}\r\n\r\n"
        ).encode()
        body += data + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def main():
    load_env()
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--ref", action="append", default=[], help="reference image, can repeat")
    p.add_argument("--size", default="1024x1536")
    p.add_argument("--quality", default="high")
    a = p.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("No OPENAI_API_KEY found. Add it to a .env file in the workspace root (see the top of this script).")
    model = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2")
    headers = {"Authorization": f"Bearer {key}"}

    if a.ref:
        for r in a.ref:
            if not os.path.exists(r):
                sys.exit(f"Reference image not found: {r}")
        body, ctype = multipart(
            {"model": model, "prompt": a.prompt, "size": a.size, "quality": a.quality},
            [("image[]", r) for r in a.ref],
        )
        req = urllib.request.Request(f"{API}/edits", data=body, headers={**headers, "Content-Type": ctype})
    else:
        body = json.dumps({"model": model, "prompt": a.prompt, "size": a.size, "quality": a.quality}).encode()
        req = urllib.request.Request(f"{API}/generations", data=body, headers={**headers, "Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")
        hint = ""
        if "model" in msg.lower():
            hint = "\nHint: your account may use a different image model name. Set OPENAI_IMAGE_MODEL in .env."
        sys.exit(f"OpenAI API error {e.code}: {msg}{hint}")

    item = result["data"][0]
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    if item.get("b64_json"):
        with open(a.out, "wb") as f:
            f.write(base64.b64decode(item["b64_json"]))
    elif item.get("url"):
        urllib.request.urlretrieve(item["url"], a.out)
    else:
        sys.exit("No image returned.")
    print(f"Saved: {a.out}")


if __name__ == "__main__":
    main()
