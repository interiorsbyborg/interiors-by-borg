Portfolio image replacement package — FIX V2

Target: Portfolio section > Layered material palette
New image: layered-material-palette.webp
Fallback image: layered-material-palette.jpg
Alt text: Layered material palette
Original dimensions: 1024 × 768

Why this v2 package is different:
- No nested wrapper folder. The files are at the ZIP root.
- Includes JPG and PNG fallbacks in case your website builder rejects WebP.
- Includes an automatic patch script for source-code projects.

Fastest manual fix:
1. Upload layered-material-palette.jpg to your website CMS/media library.
2. Open the Portfolio section.
3. Find the card/project titled “Layered material palette”.
4. Replace only that card’s existing image with layered-material-palette.jpg.
5. Save/publish and hard-refresh the page.

For Next.js / React / static sites:
1. Copy layered-material-palette.webp to public/images/portfolio/.
2. Update the image path for the Layered material palette portfolio item to:
   /images/portfolio/layered-material-palette.webp
3. Use layered-material-palette.jpg as the fallback if needed.

Automatic source-code fix:
1. Unzip this package into the root of your website project.
2. Run: python apply_portfolio_image_update.py
3. Review the changed file(s), then deploy.

For Shopify themes:
1. Upload layered-material-palette.jpg into Online Store > Themes > Edit code > Assets.
2. In the portfolio item/section for “Layered material palette”, set the image to:
   {{ 'layered-material-palette.jpg' | asset_url }}
3. Or use the snippet in shopify-liquid-replacement.liquid.

If it still does not change on the live site:
- Clear the site/CDN cache.
- Make sure the correct environment was published, not only previewed.
- Search the source for “Layered material palette” and check if the image is controlled by CMS data rather than source code.
