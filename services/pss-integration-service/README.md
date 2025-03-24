## Amadeus PSS Integration Service
This service interfaces with the Amadeus PSS system to sync inventory data, retrieve flight schedules, and push optimized fare recommendations. It ensures our system stays up-to-date with real-time inventory and fare data from Amadeus, enabling dynamic pricing adjustments.

### Responsibilities
- **PSSClient.py:** Implements a client library to call Amadeus PSS APIs (e.g., to fetch flight availability, publish fare updates).
- **InventorySyncJob.py:** A scheduled job that synchronizes available inventory (e.g., seat counts by booking class) from Amadeus PSS.
- **FarePushJob.py:** A trigger/job to push optimized fare recommendations back to PSS to update fare displays and inventory controls.

### Setup and Running
- Configure using `config.yaml` with API endpoints, auth keys, sync intervals, and retry policies.
- Containerize with the provided `Dockerfile`.
- Run tests using the test suite in the `tests/` directory.
