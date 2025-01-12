from db2rest import DB2RESTClient
import unittest
from unittest.mock import MagicMock

class TestRDBMSApiFindAll(unittest.TestCase):

    def setUp(self):
        self.client = DB2RESTClient()
        self.client.find_all = MagicMock()

    def test_find_all_success(self):
        # Mock the response of findall
        self.client.find_all.return_value = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'}
        ]
        
        result = self.client.find_all()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'Alice')
        self.assertEqual(result[1]['name'], 'Bob')

    def test_find_all_empty(self):
        # Mock the response of findall
        self.client.find_all.return_value = []
        
        result = self.client.find_all()
        self.assertEqual(len(result), 0)

    def test_find_all_exception(self):
        # Mock the response of findall to raise an exception
        self.client.find_all.side_effect = Exception("Database error")
        
        with self.assertRaises(Exception) as context:
            self.client.find_all()
        
        self.assertTrue('Database error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

