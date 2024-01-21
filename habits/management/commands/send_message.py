import os
import requests
from rest_framework import status
from rest_framework.response import Response
from requests.exceptions import RequestException
from django.core.management import BaseCommand
from datetime import datetime, timedelta
from django.utils import timezone

from habits.models import Habit, SendingLog
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Начинаю отправку")
        habits_to_send = Habit.objects.all()
        current_date = datetime.now(tz=timezone.timezone.utc)

        for habit in habits_to_send:
            user = User.objects.get(id=habit.user.pk)

            try:
                # Отправка в итерации
                log_record = SendingLog.objects.get(habit_sent=habit)

                if log_record.last_send < \
                        (current_date - timedelta(days=habit.periodity)):
                    self.send_habit(habit.action, user.telegram_id)
                    print("Отправляю второй раз")
                    log_record.last_send = current_date
                    log_record.save()

            except Exception as e:
                print(e)
                try:
                    # Отправка в первый раз
                    self.send_habit(habit.action, user.telegram_id)
                    SendingLog.objects.create(habit_sent_id=habit.pk,
                                              last_send=current_date)
                except Exception as e:
                    print(e)

        print("все отправил")

    def send_habit(self, habit_action, chat_id):

        try:
            telegram_token = os.getenv('TELEGRAM_TOKEN')
            url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'

            params = {
                'chat_id': chat_id,
                'text': habit_action
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

        except RequestException as e:
            print(Response({'error': str(e)},
                           status=status.HTTP_500_INTERNAL_SERVER_ERROR))
