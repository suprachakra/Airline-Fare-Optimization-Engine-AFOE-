## Internal APIs Documentation
This document describes the internal APIs used for service-to-service communication within the Airline Fare Optimization Engine. It includes endpoint definitions, data formats, and communication protocols to ensure consistency and reliability across the system.

### Endpoints

#### Pricing Service API
- **GET /api/pricing/fares**
  - Description: Retrieves current dynamic fare quotes.
  - Response Schema: See `Fare` schema in the OpenAPI specification.

#### Forecasting Service API
- **GET /api/forecast**
  - Description: Retrieves demand forecast for a specified route and date.
  - Parameters: 
    - `route`: string (required)
    - `date`: string (required)
  - Response Schema: See `Forecast` schema in the OpenAPI specification.

#### Offer Management API
- **GET /api/offer**
  - Description: Retrieves a complete travel offer combining base fare and ancillary bundle.
  - Parameters:
    - `flight_id`: string (required)
  - Response Schema: See `Offer` schema in the OpenAPI specification.

### Communication Protocols
- All internal APIs use RESTful communication with JSON payloads.
- Authentication between services is handled via mutual TLS and API tokens.
- Consistency is maintained via centralized configuration and shared data models.

### Message Protocols
- Internal events (e.g., price updates) are published on the event bus.
- Refer to `event_schema.json` for the format of price update events.
