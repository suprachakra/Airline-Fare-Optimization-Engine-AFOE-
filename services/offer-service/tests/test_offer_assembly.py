"""
test_offer_assembly.py
Unit tests for the OfferAssembler module.
Tests various combinations of pricing data and ancillary bundles to ensure a complete offer is assembled correctly.
"""

import unittest
from src.OfferAssembler import assemble_offer
from src.models.Offer import Offer

class TestOfferAssembly(unittest.TestCase):
    def test_assemble_offer(self):
        pricing_data = {"fare": 200}
        bundle_offer = {"discounted_price": 40}
        offer_obj = assemble_offer(pricing_data, bundle_offer)
        offer_dict = offer_obj.to_dict()
        self.assertEqual(offer_dict["base_fare"], 200)
        self.assertEqual(offer_dict["final_offer"], 240)
    
if __name__ == '__main__':
    unittest.main()
