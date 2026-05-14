import unittest
import sys
sys.path.insert(0, '.')
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_contains_hello(self):
        response = self.client.get('/')
        self.assertIn(b'Hello', response.data)

    def test_deliberate_failure(self):
        """This test deliberately fails to demonstrate UNSTABLE marking"""
        response = self.client.get('/')
        self.assertIn(b'THIS WILL NOT BE FOUND', response.data)

if __name__ == '__main__':
    unittest.main()
