# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_anime/', views.add_anime, name='add_anime'),
    path('show_anime/', views.show_anime, name='show_anime'),
]
