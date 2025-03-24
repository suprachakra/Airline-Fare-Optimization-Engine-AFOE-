"""
test_promotion_engine.py
Unit tests for the PromotionEngine module.
Tests include various discount scenarios and flash sale overrides.
"""

import unittest
from src.PromotionEngine import apply_promotion

class TestPromotionEngine(unittest.TestCase):
    def test_apply_standard_discount(self):
        base_fare = 200.0
        campaign = {"discount": 0.10}  # 10% discount, no override
        final_price = apply_promotion(base_fare, campaign)
        self.assertAlmostEqual(final_price, 180.0, places=2)

    def test_apply_override_price(self):
        base_fare = 200.0
        campaign = {"override_price": 150.0}  # Override should be used
        final_price = apply_promotion(base_fare, campaign)
        self.assertEqual(final_price, 150.0)

if __name__ == '__main__':
    unittest.main()
