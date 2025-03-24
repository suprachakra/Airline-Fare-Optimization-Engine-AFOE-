"""
test_bundling_engine.py
Unit tests for the BundlingEngine module.
Tests include:
- Creating bundles for different passenger profiles (family, business, standard).
- Verifying that the correct discount and bundle type are applied.
"""

import unittest
from src.BundlingEngine import create_bundle

class TestBundlingEngine(unittest.TestCase):
    def test_family_bundle(self):
        flight_data = {
            "base_fare": 250,
            "ancillary_items": [
                {"name": "Extra Baggage", "price": 30},
                {"name": "Preferred Seat", "price": 20},
                {"name": "In-flight Meal", "price": 25}
            ]
        }
        passenger_profile = {"travel_type": "family"}
        bundle = create_bundle(flight_data, passenger_profile)
        self.assertEqual(bundle["bundle_type"], "Family Bundle")
        self.assertAlmostEqual(bundle["discounted_price"], round((30+25)*0.85, 2))

    def test_business_bundle(self):
        flight_data = {
            "base_fare": 250,
            "ancillary_items": [
                {"name": "Extra Baggage", "price": 30},
                {"name": "Preferred Seat", "price": 20},
                {"name": "In-flight Meal", "price": 25}
            ]
        }
        passenger_profile = {"travel_type": "business"}
        bundle = create_bundle(flight_data, passenger_profile)
        self.assertEqual(bundle["bundle_type"], "Business Bundle")
        self.assertAlmostEqual(bundle["discounted_price"], round((20+25)*0.90, 2))

    def test_standard_bundle(self):
        flight_data = {
            "base_fare": 250,
            "ancillary_items": [
                {"name": "Extra Baggage", "price": 30},
                {"name": "Preferred Seat", "price": 20}
            ]
        }
        passenger_profile = {"travel_type": "leisure"}
        bundle = create_bundle(flight_data, passenger_profile)
        self.assertEqual(bundle["bundle_type"], "Standard Bundle")
        self.assertAlmostEqual(bundle["discounted_price"], round(30*0.95, 2))

if __name__ == '__main__':
    unittest.main()
