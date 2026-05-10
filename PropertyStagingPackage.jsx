export default function PropertyStagingPackage() {
  const points = [
    "Styling brief tailored to the property, buyer profile and sales goals",
    "Room-by-room furniture, décor, art and soft furnishing direction",
    "Practical staging recommendations that balance presentation, scale and budget",
  ];

  return (
    <section className="service-package property-staging">
      <h3>Property staging</h3>
      <ul className="service-package__ticks">
        {points.map((point) => (
          <li key={point}>
            <span aria-hidden="true">✓</span> {point}
          </li>
        ))}
      </ul>
    </section>
  );
}
