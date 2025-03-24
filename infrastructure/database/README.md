## Database Setup and Migrations
This folder contains scripts and guidelines for initializing and migrating databases used by various services in the Airline Fare Optimization Engine.

### Contents
- **pricing_service_schema.sql:** SQL schema for the Pricing Service database (tables for fare overrides, pricing audit logs, etc.).
- **forecasting_service_schema.sql:** Schema for storing historical data and forecast results for the Forecasting Service.
- **user_service_schema.sql:** Schema for User Management service (user accounts, roles, permissions).
- **migrate_all.sh:** Shell script to run all migration scripts in order for initial setup or full rebuild.

Follow these instructions to set up and migrate your databases.
