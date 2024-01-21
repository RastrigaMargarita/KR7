from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def test_create_User(self):
        data = {
            'email': 'user@test.com',
            'first_name': 'test',
            'last_name': 'test',
            'is_superuser': True,
            'is_staff': True,
            'is_active': True,
            'telegram_id': "111111111",
            'password': "123"
        }

        # CREATE
        response = self.client.post('/users/registration/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("CREATE user")
        self.assertTrue(User.objects.all().exists())

        # password
        email = {
            "email": "user@test.com"
        }
        response = self.client.post('/users/send_password/', data=email)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
