# Published Portfolio image update

This package is for the **published/static version** of the site, not the source `public/` folder.

## What changed

The replacement material-palette image is included at the published site path:

```txt
/images/portfolio/selections.webp
```

Inside the ZIP, that file lives at:

```txt
images/portfolio/selections.webp
```

Upload the **contents** of this package to the root of the published branch/build so the final URL becomes `/images/portfolio/selections.webp`.

## GitHub steps

1. Open the branch/folder that is actually published, for example `gh-pages`, `docs/`, or the static output branch used by your host.
2. Upload the `images/portfolio/` folder from this package at the root of that published version.
3. In the published HTML/JS/data for the Portfolio menu, update the Selections tile image path to:

```js
"/images/portfolio/selections.webp"
```

or, in HTML:

```html
<img src="/images/portfolio/selections.webp" alt="Layered material palette">
```

4. Commit the change and wait for the site to redeploy.
5. Hard-refresh the published site, or clear the site/CDN cache if the old water image still appears.

## Why the earlier package may not have worked

The earlier package used this source-project path:

```txt
public/images/portfolio/...
```

That works only when the site is rebuilt from source. A published/static site usually needs:

```txt
images/portfolio/...
```

at the published root. If the site is using a hashed build file such as `/assets/index-abc123.js` or `/assets/water-abc123.webp`, you must update the source and rebuild, or overwrite the exact hashed asset that the published page references.

## Included files

- `images/portfolio/selections.webp` — recommended published tile image.
- `images/portfolio/selections.jpg` — JPEG fallback.
- `images/portfolio/selections-layered-material-palette.webp` — descriptive duplicate.
- `images/portfolio/selections-layered-material-palette.jpg` — descriptive JPEG duplicate.
- `images/portfolio/selections-full.webp` — full uncropped source image for CSS cropping.
- `preview/selections-published-preview.jpg` — quick visual preview only.
