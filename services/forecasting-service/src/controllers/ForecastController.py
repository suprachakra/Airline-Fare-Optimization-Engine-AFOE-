"""
ForecastController.py
Provides HTTP API endpoints for retrieving demand forecasts and triggering model updates.
"""

from ForecastModel import predict_demand
from ModelTrainer import train_forecast_model
import logging

logger = logging.getLogger(__name__)

def get_forecast(request):
    """
    API endpoint to retrieve demand forecast for a flight.
    
    Expects:
    - request: dict with keys 'flight_data' and 'travel_date'
    
    Returns:
    - JSON response with predicted demand.
    """
    try:
        flight_data = request.get("flight_data")
        travel_date = request.get("travel_date")
        if not flight_data or not travel_date:
            raise ValueError("Missing required parameters: 'flight_data' and 'travel_date'")
        
        predicted_demand = predict_demand(flight_data, travel_date)
        return {
            "predicted_demand": predicted_demand,
            "details": "Demand forecast calculated using current model parameters."
        }
    except Exception as e:
        logger.error("Error in ForecastController: " + str(e))
        return {"error": str(e)}

def update_model(request):
    """
    API endpoint to trigger model training/update.
    
    Expects:
    - request: dict containing 'historical_data'
    
    Returns:
    - JSON response with updated model parameters.
    """
    try:
        historical_data = request.get("historical_data")
        if not historical_data:
            raise ValueError("Missing required parameter: 'historical_data'")
        
        new_params = train_forecast_model(historical_data)
        return {
            "model_parameters": new_params,
            "details": "Forecast model updated successfully."
        }
    except Exception as e:
        logger.error("Error in update_model: " + str(e))
        return {"error": str(e)}
