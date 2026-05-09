# Portfolio image update — Layered material palette

This add-file package replaces the existing image for the Portfolio item titled **“Layered material palette”** with the supplied material-palette image.

## Primary asset

Use this as the new Portfolio image:

```text
/public/images/portfolio/layered-material-palette.webp
```

Recommended public URL/path after adding to a typical static or Next.js-style site:

```text
/images/portfolio/layered-material-palette.webp
```

Recommended alt text:

```text
Layered material palette with neutral stone, marble, woven textiles, timber, and circular tile samples.
```

## Files included

```text
public/images/portfolio/layered-material-palette.webp          Primary replacement image, 1024×768
public/images/portfolio/layered-material-palette.jpg           JPG fallback, 1024×768
public/images/portfolio/layered-material-palette-800.webp      Responsive variant, 800×600
public/images/portfolio/layered-material-palette-640.webp      Responsive variant, 640×480
public/images/portfolio/layered-material-palette-square.webp   1:1 crop for square cards only, 768×768
public/images/portfolio/layered-material-palette-square.jpg    JPG square fallback, 768×768
snippets/html-picture.html                                     Drop-in HTML picture snippet
snippets/react-next-image.tsx                                  React / Next.js image snippet
snippets/shopify-liquid.liquid                                 Shopify Liquid snippet
snippets/portfolio-data-update.json                            Data-object replacement reference
snippets/css-object-fit.css                                    Optional image-fit CSS
manifest.json                                                  Asset manifest with dimensions and checksums
source/                                                        Original uploaded WebP source file
```

## Implementation notes

1. Copy the `public/images/portfolio/` files into your website’s matching public/static image folder.
2. Find the Portfolio entry where the title equals **“Layered material palette”**.
3. Replace its current image path with:

```text
/images/portfolio/layered-material-palette.webp
```

4. Set/update the image alt text to:

```text
Layered material palette with neutral stone, marble, woven textiles, timber, and circular tile samples.
```

5. Keep the full 4:3 image unless your Portfolio grid explicitly requires a square card. If it does, use:

```text
/images/portfolio/layered-material-palette-square.webp
```

## Common data update example

```json
{
  "title": "Layered material palette",
  "image": "/images/portfolio/layered-material-palette.webp",
  "imageAlt": "Layered material palette with neutral stone, marble, woven textiles, timber, and circular tile samples."
}
```
