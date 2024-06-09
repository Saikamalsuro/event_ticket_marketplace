# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_webseries/', views.add_webseries, name='add_webseries'),
    path('show_webseries/', views.show_webseries, name='show_webseries'),
]

