import unittest
from db2rest import DB2RESTClient

class TestDB2RESTClient(unittest.TestCase):

    def setUp(self):
        self.client = DB2RESTClient(base_url="http://localhost:5000", username="admin", password="password")

    def test_initialization(self):
        self.assertEqual(self.client.base_url, "http://localhost:5000")
        self.assertEqual(self.client.username, "admin")
        self.assertEqual(self.client.password, "password")

    def test_get_request(self):
        response = self.client.get("/test-endpoint")
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

    def test_post_request(self):
        payload = {"key": "value"}
        response = self.client.post("/test-endpoint", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_put_request(self):
        payload = {"key": "new_value"}
        response = self.client.put("/test-endpoint/1", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["key"], "new_value")

    def test_delete_request(self):
        response = self.client.delete("/test-endpoint/1")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
