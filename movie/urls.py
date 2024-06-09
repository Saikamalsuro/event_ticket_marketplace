from django.urls import path
from . import views

urlpatterns = [
    path('show_movies/', views.show_movies, name='show_movies'),
    path('add_movie/', views.add_movie, name='add_movie'),
]


