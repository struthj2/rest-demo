import unittest
import requests
import unicodedata


class ApiTest(unittest.TestCase):

    def test_hello_world(self):
        response =  requests.get("http://localhost:5000/v1/helloWorld")
        self.assertIsNot(response, None)
        self.assertIn("Hello, World", str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_double_value(self):
        response =  requests.get("http://localhost:5000/v1/double?i=5")
        self.assertIn("10", str(response.content))

    def test_double_value_bad_request(self):
        response =  requests.get("http://localhost:5000/v1/double")
        self.assertEqual(response.status_code, 400)

    def test_double_value_multiple_params(self):
        response =  requests.get("http://localhost:5000/v1/double?x=6&i=7")
        self.assertIn("14", str(response.content))
        self.assertEqual(response.status_code, 200)
    
    def test_double_value_multiple_bad_params(self):
        response =  requests.get("http://localhost:5000/v1/double?x=6&y=8")
        self.assertIn("Value i not found", str(response.content))
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()