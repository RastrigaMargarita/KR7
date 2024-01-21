from django.contrib import admin
from habits.models import Habit, SendingLog


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'time', 'action', 'is_pleasant',
                    'connected_habit', 'periodity', 'reward', 'duration',
                    'is_public')


@admin.register(SendingLog)
class SendingLogAdmin(admin.ModelAdmin):
    list_display = ('last_send', 'habit_sent')
