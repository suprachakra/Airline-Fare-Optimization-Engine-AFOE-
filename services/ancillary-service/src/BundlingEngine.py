"""
BundlingEngine.py

Core logic to create dynamic ancillary bundles.
This module implements the dynamic bundling strategy as defined in
docs/product/Ancillary_Services_PRD.md, including rules for family, business, and standard bundles.

Key actions:
- Retrieve available ancillary items from flight data.
- Evaluate passenger profiles (e.g., travel type, loyalty status).
- Apply bundling rules and calculate discounts.

Business impact:
- Aims to increase ancillary revenue by 10–15%.
- Enhances customer satisfaction by delivering tailored offers.
"""

import logging

logger = logging.getLogger(__name__)

def create_bundle(flight_data, passenger_profile):
    """
    Creates a bundle recommendation for a given flight and passenger profile.
    
    For detailed business logic and thresholds, refer to
    docs/product/Ancillary_Services_PRD.md (Section "Key Features").
    """
    try:
        # Retrieve ancillary options; fallback to default list if not provided.
        available_items = flight_data.get("ancillary_items", [
            {"name": "Extra Baggage", "price": 30},
            {"name": "Preferred Seat", "price": 20},
            {"name": "In-flight Meal", "price": 25}
        ])
        # Determine bundle type based on passenger travel type.
        travel_type = passenger_profile.get("travel_type", "leisure")
        if travel_type.lower() == "family":
            bundle_items = [item for item in available_items if item["name"] in ["Extra Baggage", "In-flight Meal"]]
            discount = 0.15  # 15% discount for family bundles (see Ancillary_Services_PRD.md: "Key Features")
            bundle_type = "Family Bundle"
        elif travel_type.lower() == "business":
            bundle_items = [item for item in available_items if item["name"] in ["Preferred Seat", "In-flight Meal"]]
            discount = 0.10  # 10% discount for business bundles
            bundle_type = "Business Bundle"
        else:
            bundle_items = [available_items[0]]
            discount = 0.05
            bundle_type = "Standard Bundle"
        
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
