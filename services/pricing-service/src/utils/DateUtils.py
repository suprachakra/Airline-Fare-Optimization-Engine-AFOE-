"""
DateUtils.py
Utility functions for handling date and time operations.
Useful for ensuring consistent fare validity periods and handling time zones.
"""

from datetime import datetime

def standardize_date(date_str):
    """
    Converts a date string into a standardized ISO format.
    Expected input format: YYYY-MM-DD or similar.
    """
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.isoformat()
    except Exception as e:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.") from e

def get_current_utc():
    """
    Returns the current UTC datetime in ISO format.
    """
    return datetime.utcnow().isoformat()

# Example usage:
# iso_date = standardize_date("2023-01-01")
