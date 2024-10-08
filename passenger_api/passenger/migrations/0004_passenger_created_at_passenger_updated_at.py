# Generated by Django 5.1.1 on 2024-10-06 22:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0003_alter_passenger_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
