"""
DynamicPricingEngine.py
Core algorithm to calculate dynamic fares based on:
- Demand forecasts (fed from Forecasting Service)
- Historical booking data
- Real-time inventory levels
This module uses a simplified pseudo-code model for illustration.
"""

import math
import logging

logger = logging.getLogger(__name__)

def calculate_dynamic_fare(flight_data, travel_date):
    """
    Calculate dynamic fare using:
    - Base fare from flight_data
    - Demand factor based on travel_date and historical trends
    - Load factor adjustments (if available)
    """
    try:
        # Retrieve base fare from flight data (assume it is provided)
        base_fare = flight_data.get("base_fare", 100.0)
        
        # Calculate a demand factor (a value between 0.8 and 1.2 for illustration)
        demand_factor = get_demand_factor(travel_date, flight_data)
        
        # Calculate load factor adjustment (simulate using available seats vs capacity)
        load_adjustment = get_load_adjustment(flight_data)
        
        # Combine base fare with demand and load factors
        dynamic_fare = base_fare * demand_factor * load_adjustment
        
        logger.info(f"Calculated dynamic fare: {dynamic_fare} (Base: {base_fare}, Demand Factor: {demand_factor}, Load Adjustment: {load_adjustment})")
        return round(dynamic_fare, 2)
    except Exception as e:
        logger.error("Error in DynamicPricingEngine: " + str(e))
        raise e

def get_demand_factor(travel_date, flight_data):
    """
    Pseudo-code for demand factor calculation.
    In practice, this would use historical data and real-time forecasts.
    For now, we simulate with a simple function.
    """
    # For illustration: if travel_date is a weekend, increase demand slightly.
    from datetime import datetime
    dt = datetime.strptime(travel_date, "%Y-%m-%d")
    if dt.weekday() >= 5:
        return 1.1  # 10% increase on weekends
    else:
        return 0.95  # 5% decrease on weekdays

def get_load_adjustment(flight_data):
    """
    Pseudo-code for load factor adjustment.
    Compares current bookings with capacity to determine pricing adjustment.
    """
    capacity = flight_data.get("capacity", 150)
    current_bookings = flight_data.get("bookings", 75)
    load_factor = current_bookings / capacity
    # Simple linear adjustment: higher load factor increases fare
    return 1 + (load_factor - 0.5)  # If load factor is 0.5, no adjustment; above increases, below decreases
