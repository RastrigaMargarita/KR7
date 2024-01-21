from rest_framework import serializers
from habits.models import Habit


class HabitsSerializer(serializers.ModelSerializer):

    title = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = "__all__"

    def get_title(self, instance):
        return f"Я буду {instance.action} в {instance.place} в {instance.time}"
