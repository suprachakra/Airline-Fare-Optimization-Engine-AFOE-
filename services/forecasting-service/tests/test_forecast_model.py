"""
test_forecast_model.py
Unit tests for the ForecastModel module.
Tests include:
- Verifying that the forecast output is within expected ranges given simulated input.
"""

import unittest
from src.ForecastModel import predict_demand

class TestForecastModel(unittest.TestCase):
    def test_predict_demand(self):
        flight_data = {"capacity": 200, "flight_number": "CD456"}
        # Use a weekday date for predictability (e.g., Monday)
        predicted = predict_demand(flight_data, "2023-06-05")
        # Since our pseudo model assumes 60% base, expect roughly 120 +/- variability.
        self.assertTrue(100 <= predicted <= 140)

if __name__ == '__main__':
    unittest.main()
