## Dynamic Pricing Service
The Dynamic Pricing Service calculates optimal fares for flight itineraries using real-time demand, historical booking data, and business rules. It leverages a Dynamic Pricing Engine and a Rules Engine to provide accurate, competitive fare quotes.

### Responsibilities
- **DynamicPricingEngine:** Computes fares using machine learning models, demand forecasts, and historical data.
- **RulesEngine:** Applies business rules (e.g., minimum/maximum fare, competitive matching, yield management) to adjust the computed fares.
- **PricingController:** Exposes HTTP or gRPC APIs for receiving pricing requests and returning fare quotes.

### Dependencies
- **Forecasting Service:** To supply demand forecasts.
- **Integration Services:** For real-time data from external systems (e.g., Amadeus PSS, PROS O&D).
- **Shared Utilities:** Currency conversion, date/time utilities, logging.

### How to Use
- Import the PricingController in your API layer.
- Call the dynamic pricing endpoint with required parameters.
- The service returns a fare quote that has passed through both the dynamic pricing calculation and business rule validation.

### Running the Service
- Use `config.yaml` for environment-specific settings.
- Dockerize with the provided `Dockerfile`.
- For local development, use `.env.example` to configure environment variables.
