## Ancillary & Merchandising Service
The Ancillary & Merchandising Service manages ancillary products (e.g., extra baggage, seat selection, in-flight meals) and dynamically generates bundle offers to increase non-ticket revenue. It applies business rules to combine ancillary products with base fares into attractive bundles for various traveler segments (e.g., family bundles, business traveler bundles).

### Responsibilities
- **BundlingEngine:** Creates dynamic bundles based on passenger profiles, flight data, and current promotions.
- **AncillaryController:** Exposes API endpoints to retrieve available ancillary products or recommended bundles.
- **Data Models:** Defines ancillary items and bundle offers.

### How to Use
- The service provides an API endpoint for clients to request ancillary options or bundle recommendations.
- It integrates with the Pricing Service and Offer Management Service for cohesive offer assembly.

### Running the Service
- Configure via `config.yaml`.
- Use the provided `Dockerfile` to build and deploy the service.
- For local development, refer to `.env.example` for environment variables.
