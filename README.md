# Portfolio image replacement package

This package replaces the water image under the **Portfolio** menu with the attached layered material palette image.

## Files to upload

Upload the primary image asset:

```text
public/images/portfolio/layered-material-palette.webp
```

A JPG fallback is also included:

```text
public/images/portfolio/layered-material-palette.jpg
```

An optional cropped version for tighter card/menu layouts is included:

```text
public/images/portfolio/layered-material-palette-card-crop.webp
```

## Code change

Find the Portfolio menu/card item that currently points to the water image and update its image source to:

```text
/images/portfolio/layered-material-palette.webp
```

Use this alt text:

```text
Layered material palette
```

## Example JSX / React

```jsx
<img
  src="/images/portfolio/layered-material-palette.webp"
  alt="Layered material palette"
  className="portfolio-card-image"
/>
```

## Example HTML

```html
<img
  src="/images/portfolio/layered-material-palette.webp"
  alt="Layered material palette"
  class="portfolio-card-image"
/>
```

## Recommended CSS

```css
.portfolio-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}
```

## Suggested commit message

```text
Replace Portfolio water image with layered material palette
```

## Preview

A mockup preview is included at:

```text
preview/portfolio-menu-card-preview.png
```
