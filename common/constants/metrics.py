"""
metrics.py
Definitions of common metric names for monitoring.
Ensures that all services report metrics using consistent identifiers.
"""

METRICS = {
    "pricing_fare_calculation_time": "pricing.fare.calc.time",
    "forecast_accuracy": "forecast.accuracy",
    "ancillary_conversion_rate": "ancillary.conversion.rate",
    "offer_assembly_time": "offer.assembly.time",
    "api_response_time": "api.response.time"
}

# Example usage:
# record_metric(METRICS["pricing_fare_calculation_time"], value)
