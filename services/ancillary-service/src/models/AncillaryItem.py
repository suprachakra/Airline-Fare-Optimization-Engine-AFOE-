"""
AncillaryItem.py

Represents an ancillary product offered to passengers.

Attributes:
    name (str): The name of the ancillary service (e.g., Extra Baggage).
    type (str): The category of the service (e.g., baggage, seating, in-flight meal).
    base_price (float): The standard price before any dynamic adjustments.
    cost (float): The underlying cost to the airline for providing this service.

Business Note:
    The configuration for these items (e.g., discount thresholds, bundling rules) is defined in the Ancillary Services PRD.
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
