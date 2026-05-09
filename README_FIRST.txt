Portfolio Selections image fix

What this package changes
- Adds the new material palette image here:
  public/images/portfolio/selections-layered-material-palette.webp
- Updates the Portfolio > Selections tile in:
  src/App.jsx
- Also includes App.jsx updated as a backup, because your ZIP contained a duplicate root App.jsx.

Why the previous attempts did not show on the website
The Portfolio tile was still using this old image value:
  image: images.texture
That points to an Unsplash water/texture image. This package changes only the Portfolio card titled "Layered material palette" to use:
  image: images.materialPalette
and defines that as:
  /images/portfolio/selections-layered-material-palette.webp

GitHub website upload steps
1. Open your GitHub repository.
2. Upload/replace these files at the same paths shown in this package:
   - src/App.jsx
   - App.jsx
   - public/images/portfolio/selections-layered-material-palette.webp
3. Commit the changes.
4. Wait for your site to rebuild/publish.
5. Hard-refresh the website. On Mac: Cmd + Shift + R. On Windows: Ctrl + F5.

Important
Do not upload this ZIP as one file into the repo. Unzip it first, then upload the files/folders inside it so the paths stay the same.

Sanity check
After upload, GitHub should show this line in src/App.jsx:
  materialPalette: "/images/portfolio/selections-layered-material-palette.webp",

And the Layered material palette portfolio item should show:
  image: images.materialPalette
