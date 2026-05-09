# GitHub fix: replace the Portfolio water image

The first package was an asset upload package. GitHub will not automatically change the website just because a ZIP is uploaded. You need either to overwrite the old water image file, or commit the new image and update the code path that renders the Portfolio menu.

## Fastest fix: overwrite the existing water image

1. In GitHub, open the repo.
2. Search for the current water image filename or open the component that renders the `Portfolio` menu.
3. Find the current image path, for example something like:
   - `/images/portfolio/water.webp`
   - `/assets/water.jpg`
   - `/images/selections/layered-material-palette.jpg`
4. Go to that same folder in GitHub.
5. Upload `public/images/portfolio/RENAME-TO-EXISTING-WATER-IMAGE-FILENAME.webp` from this package, but rename it to the exact existing water image filename.
6. Commit the change.

This method usually works because the site code keeps pointing to the same path, but the file content changes.

## Cleaner fix: add the new file and update the code

Upload this file to your repo:

```text
public/images/portfolio/layered-material-palette.webp
```

Then find the Portfolio menu/card image and change its image source to:

```text
/images/portfolio/layered-material-palette.webp
```

Use this alt text:

```text
Layered material palette
```

## JSX example

```jsx
<img
  src="/images/portfolio/layered-material-palette.webp"
  alt="Layered material palette"
/>
```

## HTML example

```html
<img
  src="/images/portfolio/layered-material-palette.webp"
  alt="Layered material palette"
/>
```

## Common reasons it still does not show

- The ZIP itself was uploaded instead of the image file being placed in the repo folder.
- The ZIP extracted into a nested folder, so the image ended up at `portfolio-image-replacement-github/public/...` instead of `public/...`.
- The code still points to the old water image path.
- The app uses `src/assets`, `app/assets`, or `public/media` instead of `public/images`.
- The change was committed to the wrong branch.
- The GitHub Pages, Netlify, or Vercel deployment has not rebuilt yet.
- The browser is showing a cached image; hard refresh or open an incognito window.
