from rest_framework.test import APITestCase
from .models import CustomUser

class UserAuthTests(APITestCase):
    def test_register_user(self):
        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password": "password123",
            "phone_number": "9876543210",
            "date_of_birth": "2000-01-01"
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        user = CustomUser.objects.create_user(username="testuser", password="password123")
        data = {"username": "testuser", "password": "password123"}
        response = self.client.post('/api/login/', data)
        self.assertEqual(response.status_code, 200)

    def test_get_profile(self):
        user = CustomUser.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/profile/')
        self.assertEqual(response.status_code, 200)
