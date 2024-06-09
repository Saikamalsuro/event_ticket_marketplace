# views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Anime
from .forms import AnimeForm

def add_anime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_anime')
    else:
        form = AnimeForm()
    return render(request, 'add_anime.html', {'form': form})

def show_anime(request):
    animes = Anime.objects.all()
    return render(request, 'show_anime.html', {'animes': animes})
