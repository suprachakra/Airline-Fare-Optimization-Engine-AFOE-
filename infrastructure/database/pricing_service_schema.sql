-- pricing_service_schema.sql
-- Schema for the Pricing Service database

CREATE TABLE IF NOT EXISTS fares (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    cabin VARCHAR(10) NOT NULL,
    base_fare NUMERIC(10,2) NOT NULL,
    dynamic_fare NUMERIC(10,2),
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    audit_log JSONB
);

CREATE TABLE IF NOT EXISTS fare_overrides (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    override_fare NUMERIC(10,2) NOT NULL,
    overridden_by VARCHAR(50),
    override_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
