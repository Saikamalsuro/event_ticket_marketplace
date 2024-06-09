# Generated by Django 5.0.6 on 2024-06-09 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_remove_anime_users_alter_anime_available_seats_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
