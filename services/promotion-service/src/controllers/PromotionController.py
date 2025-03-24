"""
PromotionController.py
API endpoints for managing and querying promotions.
Allows creation, update, and retrieval of current active promotional campaigns.
"""

import json
import logging
from models.PromotionCampaign import PromotionCampaign
from PromotionEngine import apply_promotion

logger = logging.getLogger(__name__)

# In-memory storage for demonstration; replace with a persistent store in production.
PROMOTIONS_DB = {}

def create_promotion(request):
    """
    API endpoint to create a new promotional campaign.
    
    Expects:
      request (dict): Must include campaign details (name, discount, applicable_routes, start_date, end_date, etc.)
    
    Returns:
      JSON response with created campaign details.
    """
    try:
        campaign_data = request.get("campaign_data")
        if not campaign_data:
            raise ValueError("Missing required parameter: 'campaign_data'")
        
        # Create a new PromotionCampaign instance
        campaign = PromotionCampaign(**campaign_data)
        PROMOTIONS_DB[campaign.id] = campaign.to_dict()
        logger.info(f"Promotion created: {campaign.to_dict()}")
        return json.dumps({"status": "success", "campaign": campaign.to_dict()})
    except Exception as e:
        logger.error("Error in create_promotion: " + str(e))
        return json.dumps({"error": str(e)})

def update_promotion(request):
    """
    API endpoint to update an existing promotional campaign.
    
    Expects:
      request (dict): Must include campaign 'id' and update data.
    
    Returns:
      JSON response with updated campaign details.
    """
    try:
        campaign_id = request.get("id")
        update_data = request.get("update_data")
        if not campaign_id or not update_data:
            raise ValueError("Missing required parameters: 'id' and 'update_data'")
        
        if campaign_id not in PROMOTIONS_DB:
            raise ValueError("Campaign not found.")
        
        # Update the campaign data
        campaign = PROMOTIONS_DB[campaign_id]
        campaign.update(update_data)
        PROMOTIONS_DB[campaign_id] = campaign
        logger.info(f"Promotion updated: {campaign}")
        return json.dumps({"status": "success", "campaign": campaign})
    except Exception as e:
        logger.error("Error in update_promotion: " + str(e))
        return json.dumps({"error": str(e)})

def get_active_promotions():
    """
    API endpoint to retrieve all current active promotions.
    
    Returns:
      JSON response with a list of active promotions.
    """
    try:
        # In production, filter promotions based on current date and conditions.
        active_promos = list(PROMOTIONS_DB.values())
        return json.dumps({"active_promotions": active_promos})
    except Exception as e:
        logger.error("Error in get_active_promotions: " + str(e))
        return json.dumps({"error": str(e)})

def apply_current_promotion(base_fare, campaign_id):
    """
    Applies the promotion identified by campaign_id to the base fare.
    
    Returns:
      JSON response with the final fare.
    """
    try:
        if campaign_id not in PROMOTIONS_DB:
            raise ValueError("Promotion campaign not found.")
        campaign = PROMOTIONS_DB[campaign_id]
        final_fare = apply_promotion(base_fare, campaign)
        return json.dumps({"final_fare": final_fare})
    except Exception as e:
        logger.error("Error in apply_current_promotion: " + str(e))
        return json.dumps({"error": str(e)})

# The controller functions would be wired into a web framework (Flask, FastAPI, etc.) in production.
