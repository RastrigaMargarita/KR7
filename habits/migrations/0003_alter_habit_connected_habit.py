# Generated by Django 5.0.1 on 2024-01-07 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='connected_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связана с'),
        ),
    ]
