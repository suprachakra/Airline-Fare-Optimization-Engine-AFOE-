-- forecasting_service_schema.sql
-- Schema for the Forecasting Service database

CREATE TABLE IF NOT EXISTS forecast_data (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    forecast_date DATE NOT NULL,
    predicted_demand INT NOT NULL,
    actual_demand INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
