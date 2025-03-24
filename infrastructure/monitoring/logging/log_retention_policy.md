## Log Retention Policy
This document outlines the log retention and rotation policy for the Airline Fare Optimization Engine infrastructure. The goal is to comply with data governance and privacy requirements while ensuring that critical logs are available for troubleshooting and auditing.

### Retention Periods
- **Critical Logs (e.g., errors, alerts):** Retain for 90 days.
- **General Logs (e.g., access logs, debug logs):** Retain for 30 days.
- **Audit Logs:** Retain for 180 days.

### Rotation Policy
- Logs are rotated daily using Fluentd and underlying log management system settings.
- Old logs are compressed and stored in secure, encrypted storage.
- Automatic deletion of logs older than the retention period is configured.

### Compliance
This policy complies with GDPR, CCPA, and relevant local data privacy regulations.
