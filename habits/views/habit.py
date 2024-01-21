from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers.habit import HabitsSerializer
from habits.paginations import PagePagination


class PublicHabitsListView(generics.ListAPIView):

    serializer_class = HabitsSerializer
    pagination_class = PagePagination

    def get(self, request, **kwargs):
        self.queryset = Habit.objects.filter(is_public=True)
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = HabitsSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitsListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PagePagination
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        self.queryset = Habit.objects.filter(user=self.request.user)
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = HabitsSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitsCreateView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]


class HabitsUpdateView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsOwner]


class HabitsDeleteView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitsDetailView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
