from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import requests

# Custom User Model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related_name to avoid clash
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Custom related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username

# Movie Model
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # duration in minutes
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=255)
    cast = models.TextField()

    def fetch_poster_url(self):
        response = requests.get(f"https://source.unsplash.com/random/400x600/?movie,cinema,{self.title}")
        return response.url

    def __str__(self):
        return self.title

# Theater Model
class Theater(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Showtime Model
class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.theater.name} on {self.start_time}"

# Ticket Model
class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Ticket for {self.showtime.movie.title} - Seat {self.seat_number}"

# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    tickets = models.ManyToManyField(Ticket)

    def total_amount(self):
        return sum(ticket.price for ticket in self.tickets.all())

    def __str__(self):
        return f"Booking by {self.user.username} for {self.showtime.movie.title} at {self.showtime.theater.name} - Total: ${self.total_amount()}"



