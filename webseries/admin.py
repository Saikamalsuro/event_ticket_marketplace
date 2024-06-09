from django.contrib import admin
from .models import WebSeries, Screening, Booking

class ScreeningInline(admin.TabularInline):
    model = Screening
    extra = 0

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0

class WebSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'rating')
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'release_date')
    inlines = [ScreeningInline]

class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('web_series', 'screening_time', 'available_seats')
    list_filter = ('web_series__title', 'screening_time')
    search_fields = ('web_series__title',)
    inlines = [BookingInline]

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'screening', 'seats_booked', 'booking_time')
    list_filter = ('screening__web_series__title', 'booking_time')
    search_fields = ('user__username', 'screening__web_series__title')

admin.site.register(WebSeries, WebSeriesAdmin)
admin.site.register(Screening, ScreeningAdmin)
admin.site.register(Booking, BookingAdmin)
