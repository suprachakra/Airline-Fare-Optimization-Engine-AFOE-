"""
DataPreprocessor.py
Utility functions to preprocess and normalize input data for the forecasting model.
Handles data cleaning, missing value imputation, and normalization of historical bookings.
"""

import logging

logger = logging.getLogger(__name__)

def preprocess_data(raw_data):
    """
    Processes raw historical booking data and returns cleaned, normalized data.
    
    Parameters:
    - raw_data: List of raw data records (dictionaries)
    
    Returns:
    - preprocessed_data: List of cleaned data records ready for training
    """
    try:
        preprocessed_data = []
        for record in raw_data:
            # Basic cleaning: ensure required fields are present; fill missing with defaults.
            cleaned = {
                "flight_number": record.get("flight_number"),
                "booking_count": record.get("booking_count", 0),
                "capacity": record.get("capacity", 150),
                "date": record.get("date")
            }
            preprocessed_data.append(cleaned)
        logger.info("Data preprocessing completed. Processed records: " + str(len(preprocessed_data)))
        return preprocessed_data
    except Exception as e:
        logger.error("Error in DataPreprocessor: " + str(e))
        raise e
