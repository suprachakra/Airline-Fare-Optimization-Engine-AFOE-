## Demand Forecasting Service
The Demand Forecasting Service predicts future passenger demand (on an origin-destination pair basis) and load factors for flights. This data is used to inform dynamic pricing decisions in real time.

### Responsibilities
- **ForecastModel:** Implements time-series or machine learning models to forecast demand.
- **ModelTrainer:** Trains and periodically updates the forecasting model with new historical data.
- **ForecastController:** Exposes APIs for retrieving forecasts and triggering model updates.
- **DataPreprocessor:** Prepares and normalizes input data (historical bookings, special events).

### Dependencies
- **External Data Feeds:** Integrates with external systems like PROS O&D.
- **Shared Utilities:** Uses common utilities for date handling, logging, and configuration.
- **Storage:** Reads historical data from the Data Layer (e.g., Data Lake).

### How to Use
- Call the ForecastController API with required parameters (route, date) to retrieve demand forecasts.
- Use model training routines to update forecasts on a periodic basis.

### Running the Service
- Configure using `config.yaml`.
- Containerize with the provided `Dockerfile`.
- For local development, use `.env.example` for environment variables.
