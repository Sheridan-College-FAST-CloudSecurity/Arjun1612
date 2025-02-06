import unittest
from Arjun1612.app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.data.decode(), 'Hello [YOUR NAME]')  # Match the greeting

if __name__ == "__main__":  # Corrected __name__ and __main__
    unittest.main()
