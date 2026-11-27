import unittest
import sys
import os

# Yeh line Python ko batati hai ke root folder ko dhoonde
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run import app

class TestLMSApp(unittest.TestCase):
    def test_login_page(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
    