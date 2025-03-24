"""
test_pss_client.py
Unit tests for the PSSClient module.
Tests include:
- Successful retrieval of flight availability data.
- Handling of network errors and invalid responses.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.PSSClient import PSSClient

class TestPSSClient(unittest.TestCase):
    @patch("src.PSSClient.requests.get")
    def test_get_flight_availability_success(self, mock_get):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"availability": "data"}
        mock_get.return_value = mock_response
        
        client = PSSClient()
        result = client.get_flight_availability("FL123")
        self.assertEqual(result, {"availability": "data"})
    
    @patch("src.PSSClient.requests.get")
    def test_get_flight_availability_error(self, mock_get):
        # Simulate an error response
        mock_get.side_effect = Exception("Network Error")
        client = PSSClient()
        with self.assertRaises(Exception):
            client.get_flight_availability("FL123")

if __name__ == '__main__':
    unittest.main()
