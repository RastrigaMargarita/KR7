import random
import string

from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    """Контроллер для регистрации пользователя"""
    model = User
    serializer_class = UserSerializer
    success_url = reverse_lazy('user:code')

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()


class SendPasswordView(TemplateView):
    template_name = "users/send_password.html"
    success_url = reverse_lazy("login")

    def post(self, request):
        email_to_send = request.POST.get('email')

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(8))

        send_mail(
            'Новый пароль на вход на портал хороших привычек',
            f'Ваш новый пароль: {password}',
            'RME1C@mail.ru',
            [email_to_send],
            fail_silently=False,
        )
        print("письмо отправлено на {email_to_send} c кодом {code}")

        user_details = User.objects.get(email=email_to_send)
        user_details.set_password(password)
        user_details.save()

        return render(request, self.template_name)
