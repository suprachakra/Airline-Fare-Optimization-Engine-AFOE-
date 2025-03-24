"""
PROSClient.py
Client library for interfacing with the PROS O&D system.
Provides methods to:
- Fetch demand and route analytics data.
- Handle API calls with retries and error handling.
"""

import requests
import logging
from . import config
from .errorHandler import handle_error

logger = logging.getLogger(__name__)

class PROSClient:
    def __init__(self):
        self.base_url = config.API_ENDPOINT
        self.api_key = config.API_KEY
        self.timeout = config.TIMEOUT

    def get_demand_data(self, route, date):
        """
        Fetches demand data for a given route and date from PROS.
        
        :param route: Flight route identifier.
        :param date: Date for demand forecast.
        :return: JSON data with demand details.
        """
        try:
            url = f"{self.base_url}/demand"
            params = {"route": route, "date": date}
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(url, headers=headers, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            handle_error(e, "get_demand_data")
            raise e
