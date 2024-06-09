# forms.py

from django import forms
from .models import WebSeries

class WebSeriesForm(forms.ModelForm):
    class Meta:
        model = WebSeries
        fields = ['title', 'description', 'genre', 'release_date', 'rating', 'poster_image']
