"""
test_pros_client.py
Unit tests for the PROSClient module.
Tests include:
- Successful data retrieval from PROS.
- Handling of errors such as network failures or invalid responses.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.PROSClient import PROSClient

class TestPROSClient(unittest.TestCase):
    @patch("src.PROSClient.requests.get")
    def test_get_demand_data_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"predictedBookings": 120, "routeCode": "NYC-LON"}
        mock_get.return_value = mock_response
        
        client = PROSClient()
        data = client.get_demand_data("NYC-LON", "2023-06-05")
        self.assertEqual(data["routeCode"], "NYC-LON")
        self.assertEqual(data["predictedBookings"], 120)
    
    @patch("src.PROSClient.requests.get")
    def test_get_demand_data_error(self, mock_get):
        mock_get.side_effect = Exception("Network Error")
        client = PROSClient()
        with self.assertRaises(Exception):
            client.get_demand_data("NYC-LON", "2023-06-05")

if __name__ == '__main__':
    unittest.main()
