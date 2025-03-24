#!/bin/bash
# migrate_all.sh
# Script to run all database migration scripts in order.
# Usage: ./migrate_all.sh

set -e

echo "Running Pricing Service migrations..."
psql -U $DB_USER -d $DB_NAME -f pricing_service_schema.sql

echo "Running Forecasting Service migrations..."
psql -U $DB_USER -d $DB_NAME -f forecasting_service_schema.sql

echo "Running User Management migrations..."
psql -U $DB_USER -d $DB_NAME -f user_service_schema.sql

echo "All migrations applied successfully."
