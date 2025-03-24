"""
Offer.py
Defines the data model for a complete travel offer.
The offer combines the base fare, ancillary bundle details, and any personalization adjustments.
"""

class Offer:
    def __init__(self, base_fare, ancillary_bundle, final_offer, additional_info=None):
        self.base_fare = base_fare
        self.ancillary_bundle = ancillary_bundle
        self.final_offer = final_offer
        self.additional_info = additional_info or {}

    def to_dict(self):
        return {
            "base_fare": self.base_fare,
            "ancillary_bundle": self.ancillary_bundle,
            "final_offer": self.final_offer,
            "additional_info": self.additional_info
        }

# Example usage:
# offer = Offer(200, {"bundle_type": "Business Bundle", "discounted_price": 40}, 240)
