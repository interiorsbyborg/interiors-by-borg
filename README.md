# Portfolio image replacement package

This package contains the replacement artwork for the **Portfolio → Selections** tile titled **Layered material palette**.

## Files included

- `public/images/portfolio/selections-layered-material-palette.webp` — tile-ready landscape crop, optimized for the current horizontal card image area.
- `public/images/portfolio/selections-layered-material-palette.jpg` — JPEG fallback of the same tile-ready image.
- `public/images/portfolio/selections-layered-material-palette-full.webp` — optimized full-frame source image, in case your site already crops images with CSS.
- `preview/selections-layered-material-palette-preview.jpg` — quick visual preview of the tile-ready crop.

## GitHub upload steps

1. In GitHub, open your website repository.
2. Upload the `public/images/portfolio/` folder from this package, or upload the files into your existing portfolio image directory.
3. Find the Portfolio menu data/component entry for the Selections tile.
4. Replace the current water image path with:

```js
/images/portfolio/selections-layered-material-palette.webp
```

Typical entry after update:

```js
{
  eyebrow: "SELECTIONS",
  title: "Layered material palette",
  image: "/images/portfolio/selections-layered-material-palette.webp"
}
```

5. Commit with a message like: `Replace selections tile image`.

## Notes

- If your project uses `/assets/...` instead of `/images/...`, keep the filename but place it in your existing image folder and update the path accordingly.
- If your CSS already uses `object-fit: cover` for tile images, you can use `selections-layered-material-palette-full.webp` instead.
