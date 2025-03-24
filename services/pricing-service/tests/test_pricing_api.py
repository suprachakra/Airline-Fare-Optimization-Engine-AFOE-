"""
test_pricing_api.py
Integration tests for the PricingController API endpoints.
This uses a simulated HTTP request (e.g., via Flask test client or similar framework).
"""

import unittest
from controllers.PricingController import get_fare_quote

class TestPricingAPI(unittest.TestCase):
    def test_get_fare_quote_valid(self):
        # Construct a sample request with valid parameters
        request = {
            "flight_data": {
                "base_fare": 250,
                "capacity": 150,
                "bookings": 90,
                "min_fare": 200,
                "max_fare": 500,
                "competitor_fare": 300
            },
            "travel_date": "2023-06-10"
        }
        response = get_fare_quote(request)
        self.assertIn("fare", response)
        self.assertIsInstance(response["fare"], (int, float))
    
    def test_get_fare_quote_invalid(self):
        # Test missing parameters (should return error)
        request = {"flight_data": {"base_fare": 250}}
        response = get_fare_quote(request)
        self.assertIn("error", response)

if __name__ == '__main__':
    unittest.main()
