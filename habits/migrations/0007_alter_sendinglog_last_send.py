# Generated by Django 5.0.1 on 2024-01-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_sendinglog_habit_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendinglog',
            name='last_send',
            field=models.DateTimeField(verbose_name='дата последней отправки'),
        ),
    ]
