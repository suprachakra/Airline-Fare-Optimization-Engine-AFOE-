"""
BookingClass.py
Shared Model for Booking Class/Fare Class Information

This model represents fare class details, including the booking class code, description,
and any associated fare rules. It is used across services for inventory control and integration.
"""

class BookingClass:
    def __init__(self, code, description, fare_rules):
        self.code = code  # e.g., "Y" for Economy, "J" for Business
        self.description = description  # e.g., "Economy Class"
        self.fare_rules = fare_rules  # Dictionary or structured rules (e.g., refundable, change fees)

    def to_dict(self):
        return {
            "code": self.code,
            "description": self.description,
            "fare_rules": self.fare_rules
        }

# Example usage:
# booking_class = BookingClass("Y", "Economy Class", {"refundable": False, "changes_allowed": True})
# print(booking_class.to_dict())
