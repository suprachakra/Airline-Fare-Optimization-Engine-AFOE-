"""
PSSClient.py
Client library for interacting with Amadeus PSS APIs.
Provides methods for:
- Retrieving flight availability and inventory data.
- Publishing new fare recommendations.
All calls include automatic retries and standardized error handling.
"""

import requests
import logging
from . import config
from .errorHandler import handle_error

logger = logging.getLogger(__name__)

class PSSClient:
    def __init__(self):
        self.base_url = config.API_ENDPOINT
        self.api_key = config.API_KEY
        self.timeout = config.TIMEOUT

    def get_flight_availability(self, flight_id):
        """
        Fetches flight availability data from Amadeus PSS.
        
        :param flight_id: Identifier for the flight.
        :return: JSON data containing inventory details.
        """
        try:
            url = f"{self.base_url}/flights/{flight_id}/availability"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            handle_error(e, "get_flight_availability")
            raise e

    def push_fare_update(self, flight_id, fare_data):
        """
        Pushes new fare recommendations to the Amadeus PSS.
        
        :param flight_id: Identifier for the flight.
        :param fare_data: Dictionary containing fare update details.
        :return: Response from the PSS system.
        """
        try:
            url = f"{self.base_url}/flights/{flight_id}/fares"
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            response = requests.post(url, json=fare_data, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            handle_error(e, "push_fare_update")
            raise e
