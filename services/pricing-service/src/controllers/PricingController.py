"""
PricingController.py
Handles incoming pricing requests and returns fare quotes.
This controller validates inputs, calls the Dynamic Pricing Engine, and applies the Rules Engine.
"""

from services.DynamicPricingEngine import calculate_dynamic_fare
from services.RulesEngine import apply_rules
from utils import DateUtils
import logging

logger = logging.getLogger(__name__)

def get_fare_quote(request):
    """
    Main API endpoint for retrieving a fare quote.
    Expects a JSON request with flight details, travel date, and booking context.
    """
    try:
        # Input validation (date, flight segment details)
        flight_data = request.get("flight_data")
        travel_date = request.get("travel_date")
        if not flight_data or not travel_date:
            raise ValueError("Missing required parameters: 'flight_data' and 'travel_date'")

        # Optionally convert travel_date to a standardized format
        standardized_date = DateUtils.standardize_date(travel_date)

        # Calculate the base dynamic fare
        base_fare = calculate_dynamic_fare(flight_data, standardized_date)
        
        # Apply business rules (e.g., price floors, caps, competitive adjustments)
        final_fare = apply_rules(base_fare, flight_data)
        
        return {
            "fare": final_fare,
            "currency": "USD",  # This could be dynamic based on flight_data
            "details": "Dynamic fare calculated using demand forecasts and business rules."
        }
    except Exception as e:
        logger.error("Error in PricingController: " + str(e))
        # Return error in standardized format
        return {"error": str(e)}
