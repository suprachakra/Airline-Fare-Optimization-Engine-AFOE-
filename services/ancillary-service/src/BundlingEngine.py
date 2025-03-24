"""
BundlingEngine.py
Core logic to create dynamic ancillary bundles.
Bundles are created based on flight data, passenger profiles, and business rules.
This module applies various bundling strategies (e.g., family bundle, business traveler bundle)
and calculates potential discounts.

Pseudo-code implementation:
- Retrieve available ancillary items.
- Determine eligibility based on passenger type and flight context.
- Combine eligible items into bundles and calculate total price and discount.
"""

import logging

logger = logging.getLogger(__name__)

def create_bundle(flight_data, passenger_profile):
    """
    Creates a bundle recommendation for a given flight and passenger profile.
    
    Parameters:
        flight_data (dict): Contains flight-specific information (e.g., flight number, class, base fare).
        passenger_profile (dict): Contains passenger details (e.g., loyalty status, travel type).
    
    Returns:
        dict: A bundle offer containing ancillary items, total price, discount applied, and bundle type.
    """
    try:
        # For demonstration: basic bundle rules
        base_bundle = []
        discount = 0.0
        
        # Retrieve ancillary options from flight data (simulated)
        available_items = flight_data.get("ancillary_items", [
            {"name": "Extra Baggage", "price": 30},
            {"name": "Preferred Seat", "price": 20},
            {"name": "In-flight Meal", "price": 25}
        ])
        
        # Determine bundle type based on passenger profile
        travel_type = passenger_profile.get("travel_type", "leisure")
        if travel_type.lower() == "family":
            # Family bundle: include extra baggage and meal
            bundle_items = [item for item in available_items if item["name"] in ["Extra Baggage", "In-flight Meal"]]
            discount = 0.15  # 15% discount for family bundles
            bundle_type = "Family Bundle"
        elif travel_type.lower() == "business":
            # Business bundle: include preferred seat and meal
            bundle_items = [item for item in available_items if item["name"] in ["Preferred Seat", "In-flight Meal"]]
            discount = 0.10  # 10% discount for business bundles
            bundle_type = "Business Bundle"
        else:
            # Standard bundle: include one ancillary item with a small discount
            bundle_items = [available_items[0]]  # Default to first item
            discount = 0.05
            bundle_type = "Standard Bundle"
        
        # Calculate total price and discounted price
        total_price = sum(item["price"] for item in bundle_items)
        discounted_price = total_price * (1 - discount)
        
        bundle_offer = {
            "bundle_type": bundle_type,
            "items": bundle_items,
            "total_price": total_price,
            "discount": discount,
            "discounted_price": round(discounted_price, 2)
        }
        logger.info(f"Bundle created: {bundle_offer}")
        return bundle_offer
    except Exception as e:
        logger.error("Error in BundlingEngine: " + str(e))
        raise e
