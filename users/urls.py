from django.contrib.auth.views import LogoutView, LoginView

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterView, SendPasswordView


urlpatterns = [
        path('token/', TokenObtainPairView.as_view(), name='get_token'),
        path('registration/', RegisterView.as_view(), name='new_user'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('login/', LoginView.as_view(template_name="users/login.html"),
             name='login',),
        path('send_password/', SendPasswordView.as_view(
                template_name="users/send_password.html"),
             name='send_password'),
]
