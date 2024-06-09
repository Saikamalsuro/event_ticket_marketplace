from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Movie, Theater, Showtime, Ticket, Booking

User = get_user_model()

# Unregister the original User model if already registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register the custom User model
admin.site.register(User)

# Register other models
admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Showtime)
admin.site.register(Ticket)
admin.site.register(Booking)
