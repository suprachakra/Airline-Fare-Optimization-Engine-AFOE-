"""
FareModel.py
Defines the data model for fare information.
This model represents the fare details including cabin type, fare basis, conditions, etc.
"""

class FareModel:
    def __init__(self, base_fare, cabin, conditions, currency="USD"):
        self.base_fare = base_fare      # Base fare value
        self.cabin = cabin              # Cabin class (e.g., Economy, Business)
        self.conditions = conditions    # Fare conditions (refundable, change fees, etc.)
        self.currency = currency

    def to_dict(self):
        return {
            "base_fare": self.base_fare,
            "cabin": self.cabin,
            "conditions": self.conditions,
            "currency": self.currency
        }

# Example usage:
# fare = FareModel(200, "Economy", {"refundable": False})
