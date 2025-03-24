## Promotion & Campaign Service
The Promotion & Campaign Service manages marketing promotions and fare sale campaigns. It enables marketing teams to define special offers, promo codes, and flash sales that adjust pricing dynamically. The service integrates with the Pricing and Offer Management services to ensure that promotions are applied consistently and transparently.

### Responsibilities
- **PromotionEngine:** Applies promotional adjustments (e.g., percentage discounts, flash sale overrides) to fares.
- **PromotionController:** Provides APIs for creating, updating, and querying active promotions.
- **PromotionCampaign Model:** Represents a promotional campaign with details such as discount percentage, applicable routes, start/end dates, and conditions.

### Setup and Running
- Configure service-specific settings in `config.yaml`.
- Build and run the service using the provided Dockerfile.
- Run the tests located in the `tests/` directory to verify promotion logic.

### How to Use
- Marketing can create or update promotions via the PromotionController API.
- The PromotionEngine automatically applies these promotions to fare data when requested.
