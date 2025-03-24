"""
PromotionCampaign.py
Defines the data model for a promotional campaign.
Represents a campaign with fields such as id, name, discount, override_price, applicable_routes, start_date, end_date, and conditions.
"""

import uuid
from datetime import datetime

class PromotionCampaign:
    def __init__(self, name, discount, applicable_routes, start_date, end_date, override_price=None, conditions=None):
        self.id = str(uuid.uuid4())  # Unique identifier for the campaign
        self.name = name
        self.discount = discount  # e.g., 0.15 for 15%
        self.override_price = override_price  # Optional flash sale override price
        self.applicable_routes = applicable_routes  # List of routes where the promotion applies
        self.start_date = start_date  # ISO date string
        self.end_date = end_date      # ISO date string
        self.conditions = conditions or {}  # Additional rules or conditions

    def is_active(self, current_date=None):
        current_date = current_date or datetime.utcnow().isoformat()
        return self.start_date <= current_date <= self.end_date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "discount": self.discount,
            "override_price": self.override_price,
            "applicable_routes": self.applicable_routes,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "conditions": self.conditions
        }

# Example usage:
# campaign = PromotionCampaign("Summer Sale", 0.15, ["NYC-LON", "NYC-PAR"], "2023-06-01T00:00:00Z", "2023-06-30T23:59:59Z")
