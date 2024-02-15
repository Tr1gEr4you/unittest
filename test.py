import unittest
import requests

class TestPetStoreAPI(unittest.TestCase):
    def test_successful_request_number1(self):
        response = requests.get("https://petstore.swagger.io")
        self.assertEqual(response.status_code, 200)
        
    def test_correct_data_format_number2(self):
        pet_id = 1
        
        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        
        response_data = response.json()
        self.assertIn('id', response_data)
        self.assertIn('name', response_data)
        self.assertIn('category', response_data)
        self.assertIn('photoUrls', response_data)
        self.assertIn('tags', response_data)
        self.assertIn('status', response_data)

        self.assertEqual(response.status_code, 200)

    def test_invalid_request_returns_correct_number3(self):
        pet_id = "invalid_id"

        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
