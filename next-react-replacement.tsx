import Image from "next/image";

export function LayeredMaterialPaletteImage() {
  return (
    <Image
      src="/images/portfolio/layered-material-palette.webp"
      alt="Layered material palette"
      width={1024}
      height={768}
      sizes="(max-width: 768px) 100vw, 50vw"
      style={{ width: "100%", height: "100%", objectFit: "cover" }}
    />
  );
}
