"""
AncillaryItem.py
Defines the data model for an ancillary product.
Represents an item with attributes like name, type, base price, and cost.
"""

class AncillaryItem:
    def __init__(self, name, item_type, base_price, cost):
        self.name = name
        self.item_type = item_type  # e.g., "baggage", "seat", "meal"
        self.base_price = base_price
        self.cost = cost

    def to_dict(self):
        return {
            "name": self.name,
            "item_type": self.item_type,
            "base_price": self.base_price,
            "cost": self.cost
        }

# Example usage:
# item = AncillaryItem("Extra Baggage", "baggage", 30, 20)
