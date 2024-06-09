# forms.py

from django import forms
from django.contrib.auth import get_user_model
from .models import Movie, Theater, Showtime, Ticket, Booking

User = get_user_model()

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class TheaterForm(forms.ModelForm):
    class Meta:
        model = Theater
        fields = '__all__'

class ShowtimeForm(forms.ModelForm):
    class Meta:
        model = Showtime
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
