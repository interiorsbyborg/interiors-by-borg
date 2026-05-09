# Interiors By Borg — Portfolio image update package

This package updates the Portfolio card:

- Type: `Home styling`
- Title: `Coastal dining refresh`
- New image: `public/images/portfolio/coastal-dining-refresh.webp`

It also keeps the previous Portfolio → Selections fix included:

- Type: `Selections`
- Title: `Layered material palette`
- Image: `public/images/portfolio/selections-layered-material-palette.webp`

## Upload instructions for GitHub

1. Download and unzip this package.
2. In GitHub, open your website repository.
3. Upload the **unzipped contents** into the repository root.
4. Let GitHub replace the existing files when it asks.
5. Commit the changes.
6. Wait for the site to publish/redeploy.
7. Hard-refresh the website:
   - Mac: `Cmd + Shift + R`
   - Windows: `Ctrl + F5`

## Files included

```txt
src/App.jsx
App.jsx
public/images/portfolio/coastal-dining-refresh.webp
public/images/portfolio/selections-layered-material-palette.webp
CHANGES.patch
README_FIRST.txt
```

## Code change made

The Portfolio item changed from:

```jsx
{ title: "Coastal dining refresh", type: "Home styling", image: images.dining }
```

to:

```jsx
{ title: "Coastal dining refresh", type: "Home styling", image: images.coastalDiningRefresh }
```

and the new image is referenced as:

```jsx
coastalDiningRefresh: "/images/portfolio/coastal-dining-refresh.webp"
```

Do **not** upload this ZIP file itself to GitHub. Upload the unzipped files/folders.
