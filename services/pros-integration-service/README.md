## PROS O&D Integration Service
This service integrates with the PROS O&D system to retrieve demand forecasts and fare optimization outputs. It supports our core services by providing accurate demand and optimization data.

### Responsibilities
- **PROSClient.py:** Fetches data from PROS using API calls or file imports.
- **PROSDataAdapter.py:** Transforms raw PROS data into the internal format used by DFAE.
- **Tests:** Ensures that the integration correctly handles data retrieval and error scenarios.

### Setup and Running
- Configure using `config.yaml` with API endpoints, file paths, and authentication info.
- Containerize with the provided `Dockerfile`.
- Run tests via the test suite in the `tests/` directory.
