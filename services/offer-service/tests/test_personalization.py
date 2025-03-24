"""
test_personalization.py
Unit tests for the PersonalizationEngine module.
Tests that personalization rules are correctly applied based on customer profiles.
"""

import unittest
from src.PersonalizationEngine import personalize_offer

class TestPersonalizationEngine(unittest.TestCase):
    def test_personalize_offer_gold_member(self):
        base_offer = {"final_offer": 240, "personalization_notes": ""}
        customer_profile = {"loyalty_status": "gold"}
        personalized = personalize_offer(base_offer, customer_profile)
        # Expect a 5% discount applied for gold members: 240 * 0.95 = 228
        self.assertAlmostEqual(personalized["final_offer"], 228.0, places=2)
        self.assertIn("Gold member", personalized["personalization_notes"])

    def test_personalize_offer_standard(self):
        base_offer = {"final_offer": 240, "personalization_notes": ""}
        customer_profile = {"loyalty_status": "silver"}
        personalized = personalize_offer(base_offer, customer_profile)
        self.assertEqual(personalized["final_offer"], 240)
        self.assertEqual(personalized["personalization_notes"], "Standard offer.")

if __name__ == '__main__':
    unittest.main()
