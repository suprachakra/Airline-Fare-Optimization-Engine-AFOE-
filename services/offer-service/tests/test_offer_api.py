"""
test_offer_api.py
Integration tests for the OfferController API endpoints.
Simulates API requests for offer retrieval.
"""

import unittest
from src.controllers.OfferController import get_offer

class TestOfferAPI(unittest.TestCase):
    def test_get_offer_valid(self):
        request = {
            "pricing_data": {"fare": 200},
            "bundle_offer": {"discounted_price": 40},
            "customer_profile": {"loyalty_status": "gold"}
        }
        response = get_offer(request)
        import json
        data = json.loads(response)
        self.assertIn("offer", data)
        self.assertIn("final_offer", data["offer"])
    
    def test_get_offer_invalid(self):
        request = {"pricing_data": {"fare": 200}}
        response = get_offer(request)
        import json
        data = json.loads(response)
        self.assertIn("error", data)

if __name__ == '__main__':
    unittest.main()
