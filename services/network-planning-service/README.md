## Network Planning & Codeshare Service
This service synchronizes schedule changes and codeshare partner flight data. It ingests new route plans, flight schedules, and partner codeshare information, ensuring the system’s data on flight availability and partnerships is current.

### Responsibilities
- **ScheduleImporter.py:** Fetches and processes updated flight schedules (new flights, cancellations, capacity changes).
- **PartnerSync.py:** Handles data from codeshare partners, including joint fare agreements and partner flight availability.
- **Integration:** Updates internal databases with new schedule and codeshare data.

### How to Use
- Run scheduled jobs to periodically update flight schedules and codeshare data.
- API endpoints (if exposed) allow retrieval of current network planning information.
- Configure using `config.yaml`, and containerize with the provided `Dockerfile`.
