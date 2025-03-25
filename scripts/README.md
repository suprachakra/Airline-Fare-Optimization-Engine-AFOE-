## Utility Scripts
This folder contains assorted utility scripts to aid development, setup, and maintenance of the Airline Fare Optimization Engine. These scripts automate tasks such as environment initialization, running tests, linting code, and backing up databases.

### Available Scripts
- **init_local_env.sh:** Initializes the local development environment (creates virtual environments, installs dependencies, and sets up Git hooks).
- **start_all.sh:** Convenience script to start all services locally using Docker Compose or individual commands.
- **run_tests.sh:** Aggregates and runs the entire test suite across all services.
- **lint_and_format.sh:** Runs linters and code formatters for all languages to maintain code quality.
- **backup_db.sh:** Backs up all databases for disaster recovery; can be scheduled via cron or CI.
