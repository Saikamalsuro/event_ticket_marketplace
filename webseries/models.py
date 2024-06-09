from django.db import models
from django.contrib.auth.models import User

class WebSeries(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    poster_image = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

class Screening(models.Model):
    web_series = models.ForeignKey(WebSeries, on_delete=models.CASCADE)
    screening_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.web_series.title} - {self.screening_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='webseries_bookings')
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.screening.web_series.title}"

