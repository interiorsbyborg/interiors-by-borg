#!/usr/bin/env python3
"""
Apply the Portfolio > Layered material palette image update.

Run this from the root of your website project after unzipping this package:
    python apply_portfolio_image_update.py

Optional:
    python apply_portfolio_image_update.py --root /path/to/site --asset-dir public/images/portfolio --asset-url /images/portfolio/layered-material-palette.webp

What it does:
1) Copies layered-material-palette.webp and .jpg into your chosen asset directory.
2) Searches common website source files for "Layered material palette".
3) Replaces the nearest image URL/path in that portfolio item with the new image URL.
4) Creates .bak-layered-material-palette backups before editing.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

IMAGE_EXTS = r"(?:png|jpe?g|webp|avif|gif|svg)"
TEXT_EXTS = {
    ".html", ".htm", ".liquid", ".json", ".js", ".jsx", ".ts", ".tsx", ".mdx",
    ".astro", ".vue", ".svelte", ".css", ".scss", ".yml", ".yaml"
}
SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", "coverage", ".vercel"}
TARGET_RE = re.compile(r"layered\s+material\s+palette", re.I)

# Matches common JS/JSON/HTML/Liquid image assignments or plain image strings.
IMG_PATTERNS = [
    re.compile(r"((?:src|image|imageSrc|img|thumbnail|thumb|photo|cover|url|poster)\s*[:=]\s*[\"'])([^\"']+\." + IMAGE_EXTS + r"(?:\?[^\"']*)?)([\"'])", re.I),
    re.compile(r"(<img\b[^>]*?\bsrc\s*=\s*[\"'])([^\"']+\." + IMAGE_EXTS + r"(?:\?[^\"']*)?)([\"'][^>]*>)", re.I),
    re.compile(r"([\"'])([^\"']+\." + IMAGE_EXTS + r"(?:\?[^\"']*)?)([\"'])", re.I),
]

def iter_source_files(root: Path):
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_EXTS:
            yield path

def nearest_replacement(text: str, asset_url: str):
    targets = [m.start() for m in TARGET_RE.finditer(text)]
    if not targets:
        return text, False

    candidates = []
    for pat in IMG_PATTERNS:
        for m in pat.finditer(text):
            image_path = m.group(2)
            # Avoid replacing the image we're adding or non-content icons/logos where possible.
            low = image_path.lower()
            if "layered-material-palette" in low:
                continue
            dist = min(abs(m.start() - t) for t in targets)
            # Require the image path to be reasonably close to the target portfolio title.
            if dist <= 3000:
                candidates.append((dist, m.start(), m.end(), m.group(1), m.group(2), m.group(3)))
    if not candidates:
        return text, False

    candidates.sort(key=lambda x: (x[0], x[1]))
    _, start, end, before, old, after = candidates[0]
    new = before + asset_url + after
    return text[:start] + new + text[end:], True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Website project root")
    parser.add_argument("--asset-dir", default="public/images/portfolio", help="Where to copy the image inside the project")
    parser.add_argument("--asset-url", default="/images/portfolio/layered-material-palette.webp", help="URL/path to write into source files")
    args = parser.parse_args()

    package_dir = Path(__file__).resolve().parent
    root = Path(args.root).resolve()
    asset_dir = (root / args.asset_dir).resolve()
    asset_dir.mkdir(parents=True, exist_ok=True)

    for name in ["layered-material-palette.webp", "layered-material-palette.jpg"]:
        src = package_dir / name
        if not src.exists():
            raise SystemExit(f"Missing {name} next to this script.")
        shutil.copy2(src, asset_dir / name)
        print(f"Copied {name} -> {asset_dir / name}")

    edited = []
    checked = 0
    for path in iter_source_files(root):
        checked += 1
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = path.read_text(encoding="latin-1")
            except Exception:
                continue
        except Exception:
            continue

        if not TARGET_RE.search(text):
            continue
        new_text, changed = nearest_replacement(text, args.asset_url)
        if changed and new_text != text:
            backup = path.with_suffix(path.suffix + ".bak-layered-material-palette")
            if not backup.exists():
                backup.write_text(text, encoding="utf-8")
            path.write_text(new_text, encoding="utf-8")
            edited.append(path)
            print(f"Updated {path}")

    print(f"\nChecked {checked} source files.")
    if edited:
        print("Success. Updated files:")
        for p in edited:
            print(f" - {p}")
    else:
        print("No source file was changed automatically.")
        print("Search your site files for 'Layered material palette' and replace that card's image with:")
        print(f"  {args.asset_url}")
        print("For Shopify assets, use the shopify-liquid-replacement.liquid snippet in this package.")

if __name__ == "__main__":
    main()
