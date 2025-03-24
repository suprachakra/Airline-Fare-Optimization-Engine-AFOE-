"""
OfferController.py
Provides HTTP API endpoints for retrieving and managing travel offers.
This controller interacts with the OfferAssembler and PersonalizationEngine to create tailored offers.
"""

import json
import logging
from OfferAssembler import assemble_offer
from PersonalizationEngine import personalize_offer

logger = logging.getLogger(__name__)

def get_offer(request):
    """
    API endpoint to retrieve a travel offer.
    Expects a JSON request with keys 'pricing_data', 'bundle_offer', and optionally 'customer_profile'.
    
    Returns:
      JSON response with the complete offer.
    """
    try:
        pricing_data = request.get("pricing_data")
        bundle_offer = request.get("bundle_offer")
        customer_profile = request.get("customer_profile", {})
        if not pricing_data or not bundle_offer:
            raise ValueError("Missing required parameters: 'pricing_data' and 'bundle_offer'")

        # Assemble base offer
        offer_obj = assemble_offer(pricing_data, bundle_offer)
        offer = offer_obj.to_dict()
        
        # Personalize offer if customer profile is provided
        if customer_profile:
            offer = personalize_offer(offer, customer_profile)
        
        return json.dumps({"offer": offer})
    except Exception as e:
        logger.error("Error in OfferController: " + str(e))
        return json.dumps({"error": str(e)})
