"""
test_forecast_api.py
Integration tests for the ForecastController endpoints.
Tests retrieval of forecast data and model update triggers.
"""

import unittest
from src.controllers.ForecastController import get_forecast, update_model

class TestForecastAPI(unittest.TestCase):
    def test_get_forecast_valid(self):
        request = {
            "flight_data": {"capacity": 200, "flight_number": "CD456"},
            "travel_date": "2023-06-05"
        }
        response = get_forecast(request)
        self.assertIn("predicted_demand", response)
        self.assertIsInstance(response["predicted_demand"], int)

    def test_update_model_valid(self):
        request = {"historical_data": [{"flight_number": "CD456", "booking_count": 100, "capacity": 200, "date": "2023-05-01"}]}
        response = update_model(request)
        self.assertIn("model_parameters", response)

if __name__ == '__main__':
    unittest.main()
