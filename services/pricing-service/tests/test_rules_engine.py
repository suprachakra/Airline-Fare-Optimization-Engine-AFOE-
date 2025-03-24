"""
test_rules_engine.py
Unit tests for the RulesEngine functionality.
"""

import unittest
from services.RulesEngine import apply_rules

class TestRulesEngine(unittest.TestCase):
    def test_apply_rules_with_competitor_adjustment(self):
        base_fare = 180.0
        flight_data = {
            "min_fare": 150.0,
            "max_fare": 400.0,
            "competitor_fare": 200.0
        }
        # Expect the final fare to be adjusted to at least 95% of competitor_fare (i.e., 190)
        final_fare = apply_rules(base_fare, flight_data)
        self.assertGreaterEqual(final_fare, 190.0)
    
    def test_apply_rules_with_floor_and_cap(self):
        base_fare = 50.0  # Below min_fare
        flight_data = {
            "min_fare": 100.0,
            "max_fare": 500.0,
            "competitor_fare": 120.0
        }
        final_fare = apply_rules(base_fare, flight_data)
        self.assertEqual(final_fare, 100.0)

if __name__ == '__main__':
    unittest.main()
