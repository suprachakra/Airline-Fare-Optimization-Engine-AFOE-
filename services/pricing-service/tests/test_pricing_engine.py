"""
test_pricing_engine.py
Unit tests for the DynamicPricingEngine functionality.
"""

import unittest
from services.DynamicPricingEngine import calculate_dynamic_fare

class TestDynamicPricingEngine(unittest.TestCase):
    def test_calculate_dynamic_fare_weekday(self):
        # Simulated flight data for a weekday
        flight_data = {
            "base_fare": 200,
            "capacity": 150,
            "bookings": 75
        }
        # Use a weekday date (e.g., Monday)
        fare = calculate_dynamic_fare(flight_data, "2023-06-05")
        # Expect a fare adjustment based on a 0.95 demand factor and load factor of 0.5 (no adjustment)
        self.assertAlmostEqual(fare, 200 * 0.95 * 1.0, places=2)

    def test_calculate_dynamic_fare_weekend(self):
        # Simulated flight data for a weekend
        flight_data = {
            "base_fare": 200,
            "capacity": 150,
            "bookings": 90
        }
        # Use a weekend date (e.g., Saturday)
        fare = calculate_dynamic_fare(flight_data, "2023-06-10")
        # Expect a higher fare due to weekend demand; exact value depends on load factor calculation.
        self.assertTrue(fare > 200)

if __name__ == '__main__':
    unittest.main()
