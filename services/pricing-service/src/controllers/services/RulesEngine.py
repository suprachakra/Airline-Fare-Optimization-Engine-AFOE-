"""
RulesEngine.py
Applies business rules to the dynamically calculated fare.
Rules include:
- Minimum and maximum fare constraints
- Competitive matching
- Yield management (e.g., if flights are nearly full, increase fare)
This is implemented in pseudo-code for demonstration.
"""

import logging

logger = logging.getLogger(__name__)

def apply_rules(fare, flight_data):
    """
    Applies business rules on the given fare.
    """
    try:
        # Set default rule parameters (could be loaded from config)
        min_fare = flight_data.get("min_fare", 80.0)
        max_fare = flight_data.get("max_fare", 500.0)
        
        # Competitive adjustment (simulate a rule: if competitor fare is higher, our fare should not be lower than 95% of competitor)
        competitor_fare = flight_data.get("competitor_fare", fare)
        if fare < competitor_fare * 0.95:
            fare = competitor_fare * 0.95
        
        # Ensure fare does not fall below or above defined limits
        if fare < min_fare:
            fare = min_fare
        elif fare > max_fare:
            fare = max_fare
        
        logger.info(f"Final fare after rules applied: {fare}")
        return fare
    except Exception as e:
        logger.error("Error in RulesEngine: " + str(e))
        raise e
