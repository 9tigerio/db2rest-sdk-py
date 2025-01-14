import unittest
from db2rest import DB2RESTClient
from unittest.mock import MagicMock
from requests import Response

class TestDB2RESTClient(unittest.TestCase):

    def setUp(self):
        self.client = DB2RESTClient(base_url="http://localhost:5000/api/v1/rdbms", api_key="12345ABCDE", timeout="60")
        self.client._request = MagicMock()

    def test_request(self):
        # Mock the response of _request
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test_data"}
        self.client._request.return_value = mock_response

        response = self.client._request("GET", "/cases")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"data": "test_data"})

    def test_request_exception(self):
        # Mock the response of _request to raise an exception
        mock_response = MagicMock(spec=Response)
        mock_response.raise_for_status.side_effect = Exception("Server error")
        self.client._request.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.client._request("GET", "/cases")

        self.assertIn('Server error', str(context.exception))

if __name__ == '__main__':
    unittest.main()
