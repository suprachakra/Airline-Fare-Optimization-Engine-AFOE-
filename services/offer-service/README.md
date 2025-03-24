## Offer Management Service
The Offer Management Service assembles personalized travel offers by combining dynamic fares and ancillary products. It integrates with both the Pricing and Ancillary Services to generate complete offers that adhere to airline industry standards (e.g., NDC format) and provide clear, personalized options to customers.

### Responsibilities
- **OfferAssembler:** Combines base fares from the Pricing Service and ancillary bundles from the Ancillary Service.
- **PersonalizationEngine:** Applies rules based on loyalty status, travel type, and historical behavior to tailor offers.
- **OfferController:** Exposes API endpoints to retrieve offers for a given flight search or booking context.

### How to Use
- Call the OfferController API with search parameters to receive a complete offer (fare plus bundled ancillaries).
- Offers are designed to be integrated into the booking flow of the airline's reservation system.

### Running the Service
- Configure using `config.yaml`.
- Containerize with the provided `Dockerfile`.
- For local development, refer to `.env.example` for environment variables.
