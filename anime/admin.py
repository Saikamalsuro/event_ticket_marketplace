# anime/admin.py

from django.contrib import admin
from .models import Anime, Booking

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    readonly_fields = ('user', 'seats_booked', 'booking_time')

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'rating', 'screening_time', 'available_seats', 'booked_seats')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'release_date')
    inlines = [BookingInline]

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'anime', 'seats_booked', 'booking_time')
    search_fields = ('user__username', 'anime__title')
    list_filter = ('booking_time',)

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Booking, BookingAdmin)
