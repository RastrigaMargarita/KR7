from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    telephone = models.CharField(max_length=15, verbose_name="телефон",
                                 blank=True, null=True)
    username = models.CharField(max_length=15, verbose_name="имя",
                                blank=True, null=True)
    is_active = models.BooleanField(default=True)
    telegram_id = models.CharField(
        max_length=15,
        verbose_name="телеграм",
        blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
