"""
ForecastModel.py
Implements the forecasting logic to predict passenger demand.
This is a simplified pseudo-code model using historical data trends.
"""

import logging
import random  # For simulation purposes

logger = logging.getLogger(__name__)

def predict_demand(flight_data, travel_date):
    """
    Predicts demand based on flight data and travel date.
    In production, this function would use statistical models or machine learning.
    
    Parameters:
    - flight_data: dict containing historical booking data, capacity, etc.
    - travel_date: string in ISO format (YYYY-MM-DD)
    
    Returns:
    - predicted_demand: A number representing the forecasted number of bookings.
    """
    try:
        # Simulate prediction: base on a percentage of capacity with randomness.
        capacity = flight_data.get("capacity", 150)
        base_demand = capacity * 0.6  # Assume 60% average booking rate
        # Add variability based on travel_date (e.g., weekends higher demand)
        # For demonstration, we add a random factor
        variability = random.uniform(-0.1, 0.2)  # +/-10% to +20%
        predicted_demand = base_demand * (1 + variability)
        logger.info(f"Predicted demand: {predicted_demand} for flight {flight_data.get('flight_number')} on {travel_date}")
        return round(predicted_demand)
    except Exception as e:
        logger.error("Error in ForecastModel: " + str(e))
        raise e
