# forms.py

from django import forms
from .models import Anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = [
            'title', 'description', 'duration', 'genre', 
            'release_date', 'rating', 'poster_image', 
            'screening_time', 'available_seats'
        ]
