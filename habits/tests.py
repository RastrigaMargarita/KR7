from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='user@test.com',
            password='test',
            username='username')
        self.client.force_authenticate(user=self.user)

    def test_CRUD_habit(self):
        data = {"user": 1,
                "place": "place_1",
                "action": "action_1",
                "is_pleasant": "false",
                "connected_habit": "",
                "periodity": 7,
                "reward": "reward_1",
                "duration": 50,
                "is_public": "true",
                'time': '02:00:00'
                }

        data_update = {"user": 1,
                       "place": "place_2",
                       "action": "action_2",
                       "is_pleasant": "false",
                       "connected_habit": "",
                       "periodity": 7,
                       "reward": "reward_1",
                       "duration": 50,
                       "is_public": "true",
                       'time': '02:00:00'
                       }

        response_data = {'action': 'action_1',
                         'connected_habit': None,
                         'duration': 50,
                         'id': 1,
                         'is_pleasant': False,
                         'is_public': True,
                         'periodity': 7,
                         'place': 'place_1',
                         'reward': 'reward_1',
                         'time': '02:00:00',
                         'title': 'Я буду action_1 в place_1 в 02:00:00',
                         'user': 1}
        response_data_updated = {'id': 1, 'title':
                                 'Я буду action_1 в place_1 в 02:00:00',
                                 'place': 'place_1',
                                 'time': '02:00:00',
                                 'action': 'action_1',
                                 'is_pleasant': False,
                                 'periodity': 7,
                                 'reward': 'reward_1',
                                 'duration': 50,
                                 'is_public': True,
                                 'user': 1,
                                 'connected_habit': None}

        response_list = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': 1, 'title':
                    'Я буду action_1 в place_1 в 02:00:00',
                 'place': 'place_1',
                 'time': '02:00:00',
                 'action': 'action_1',
                 'is_pleasant': False,
                 'periodity': 7,
                 'reward': 'reward_1',
                 'duration': 50,
                 'is_public': True,
                 'user': 1,
                 'connected_habit': None}]}

        # CREATE
        response = self.client.post('/habits/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("CREATE")
        self.assertEqual(response.json(), response_data)
        self.assertTrue(Habit.objects.all().exists())

        # UPDATE
        self.client.patch('/habits/update/1', data=data_update)
        print("UPDATE")

        # GET
        response = self.client.get('/habits/1/')
        print("GET")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_data_updated)

        # GET_PUBLIC_LIST
        response = self.client.get('/habits/')
        print("PUBLIC_LIST")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_list)

        # GET_PRIVATE_LIST
        response = self.client.get('/habits/my/')
        print("PRIVATE_LIST")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_list)

        # DELETE
        response = self.client.delete('/habits/delete/1/')
        print("DELETE")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
