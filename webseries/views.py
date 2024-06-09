
# views.py

from django.shortcuts import render, redirect
from .models import WebSeries
from .forms import WebSeriesForm

def add_webseries(request):
    if request.method == 'POST':
        form = WebSeriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_webseries')
    else:
        form = WebSeriesForm()
    return render(request, 'add_webseries.html', {'form': form})

def show_webseries(request):
    web_series_list = WebSeries.objects.all()
    return render(request, 'show_webseries.html', {'web_series_list': web_series_list})
