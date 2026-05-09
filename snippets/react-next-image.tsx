import Image from "next/image";

export function LayeredMaterialPaletteImage() {
  return (
    <Image
      src="/images/portfolio/layered-material-palette.webp"
      alt="Layered material palette with neutral stone, marble, woven textiles, timber, and circular tile samples."
      width={1024}
      height={768}
      sizes="(min-width: 1024px) 50vw, 100vw"
      priority={false}
    />
  );
}

// Data-entry replacement reference:
export const layeredMaterialPalettePortfolioUpdate = {
  title: "Layered material palette",
  image: "/images/portfolio/layered-material-palette.webp",
  imageAlt:
    "Layered material palette with neutral stone, marble, woven textiles, timber, and circular tile samples.",
};
