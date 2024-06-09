# anime/models.py

from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField()
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    poster_image = models.ImageField(upload_to='posters/')
    screening_time = models.DateTimeField()
    available_seats = models.IntegerField()
    booked_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anime_bookings')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.anime.title}'

