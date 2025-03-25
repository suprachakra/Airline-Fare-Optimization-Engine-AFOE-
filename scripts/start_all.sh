#!/bin/bash
# start_all.sh
# Convenience script to start all services locally.
# This script checks if a docker-compose.yml file exists; if so, it uses Docker Compose to start all services.
# Otherwise, it will attempt to start individual services in development mode.
#
# Usage:
#   ./start_all.sh
#
# Requirements:
#   - Docker and docker-compose must be installed.
#   - Environment variables can be loaded via an .env file if needed.
#
# This script is designed to work across multi-service architectures and ensure all services start properly.

set -e

# Check if docker-compose.yml exists in the current directory
if [ -f docker-compose.yml ]; then
    echo "Starting all services using docker-compose..."
    docker-compose up --build
else
    echo "docker-compose.yml not found. Starting services individually..."
    # Example: Start each service manually (customize these commands as per your project structure)
    echo "Starting Pricing Service..."
    (cd services/pricing-service && python -m src.controllers.PricingController &)

    echo "Starting Forecasting Service..."
    (cd services/forecasting-service && python -m src.controllers.ForecastController &)

    echo "Starting Ancillary Service..."
    (cd services/ancillary-service && python -m src.controllers.AncillaryController &)

    echo "Starting Offer Service..."
    (cd services/offer-service && python -m src.controllers.OfferController &)

    echo "Starting PSS Integration Service..."
    (cd services/pss-integration-service && python -m src.InventorySyncJob &)

    echo "Starting PROS Integration Service..."
    (cd services/pros-integration-service && python -m src.PROSClient &)

    echo "Starting Network Planning Service..."
    (cd services/network-planning-service && python -m src.ScheduleImporter &)

    # Add other services as needed.
    echo "All services started. Press [CTRL+C] to stop."
    # Wait indefinitely to keep the script running
    wait
fi
