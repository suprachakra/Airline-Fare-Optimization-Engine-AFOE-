"""
PromotionEngine.py
Core logic to apply promotional adjustments to fares.
This module calculates discount amounts, applies flash sale overrides,
and determines the final promotional price based on the active campaign rules.
"""

import logging

logger = logging.getLogger(__name__)

def apply_promotion(base_fare, campaign):
    """
    Applies promotional adjustments to a given base fare.
    
    Parameters:
      base_fare (float): The original fare before promotion.
      campaign (dict): Promotional campaign details containing:
         - discount (float): Discount percentage (e.g., 0.15 for 15% off)
         - override_price (float, optional): A flash sale override price, if provided.
         - conditions (dict): Conditions under which the promotion applies.
    
    Returns:
      float: The final fare after applying the promotion.
    """
    try:
        # If an override price is provided, use it directly
        if campaign.get("override_price"):
            final_price = campaign["override_price"]
            logger.info(f"Flash sale override applied: {final_price}")
        else:
            discount = campaign.get("discount", 0)
            final_price = base_fare * (1 - discount)
            logger.info(f"Applied discount of {discount*100}%: Base fare {base_fare} -> {final_price}")
        
        # Additional conditions (e.g., applicable routes or time limits) can be checked here.
        # For example, if the campaign is only valid for certain routes, add conditional logic.
        
        return round(final_price, 2)
    except Exception as e:
        logger.error("Error in PromotionEngine: " + str(e))
        raise e
