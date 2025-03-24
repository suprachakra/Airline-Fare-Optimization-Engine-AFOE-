"""
AncillaryController.py
Exposes API endpoints to retrieve ancillary products and bundle recommendations.
Handles HTTP requests, validates inputs, and returns JSON responses.
"""

import json
import logging
from BundlingEngine import create_bundle

logger = logging.getLogger(__name__)

def get_ancillary_options(request):
    """
    API endpoint to list available ancillary options for a flight.
    
    Expects:
        request (dict): Contains 'flight_data' and optionally 'passenger_profile'.
    
    Returns:
        JSON response with ancillary items or recommended bundle.
    """
    try:
        flight_data = request.get("flight_data")
        if not flight_data:
            raise ValueError("Missing required parameter: 'flight_data'")
        
        # If passenger profile is provided, generate a bundle recommendation
        passenger_profile = request.get("passenger_profile")
        if passenger_profile:
            bundle = create_bundle(flight_data, passenger_profile)
            response = {"bundle_offer": bundle}
        else:
            # Otherwise, return raw ancillary options
            ancillary_options = flight_data.get("ancillary_items", [])
            response = {"ancillary_options": ancillary_options}
        return json.dumps(response)
    except Exception as e:
        logger.error("Error in AncillaryController: " + str(e))
        return json.dumps({"error": str(e)})
