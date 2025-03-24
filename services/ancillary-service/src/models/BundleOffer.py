"""
BundleOffer.py
Defines the data model for a bundle offer.
A bundle offer combines multiple ancillary items with a base fare, including an applied discount.
"""

class BundleOffer:
    def __init__(self, bundle_type, items, discount):
        self.bundle_type = bundle_type  # e.g., "Family Bundle", "Business Bundle"
        self.items = items  # List of ancillary items (as dicts)
        self.discount = discount  # Discount rate (e.g., 0.15 for 15%)

    def calculate_total(self):
        total = sum(item["price"] for item in self.items)
        return total

    def calculate_discounted_total(self):
        total = self.calculate_total()
        return round(total * (1 - self.discount), 2)

    def to_dict(self):
        return {
            "bundle_type": self.bundle_type,
            "items": self.items,
            "total": self.calculate_total(),
            "discount": self.discount,
            "discounted_total": self.calculate_discounted_total()
        }

# Example usage:
# bundle = BundleOffer("Family Bundle", [{"name": "Extra Baggage", "price": 30}], 0.15)
