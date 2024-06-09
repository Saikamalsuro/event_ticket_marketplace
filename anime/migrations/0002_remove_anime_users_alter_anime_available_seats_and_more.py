# Generated by Django 5.0.6 on 2024-06-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='users',
        ),
        migrations.AlterField(
            model_name='anime',
            name='available_seats',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='booked_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seats_booked',
            field=models.IntegerField(),
        ),
    ]
