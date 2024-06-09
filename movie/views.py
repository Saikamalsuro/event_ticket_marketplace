from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from .models import Movie, Theater, Showtime, Ticket, Booking
from .forms import MovieForm, TheaterForm, ShowtimeForm, TicketForm, BookingForm

def show_movies(request):
    movies = Movie.objects.all()
    return render(request, 'show_movies.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        theater_form = TheaterForm(request.POST)
        showtime_form = ShowtimeForm(request.POST)
        ticket_form = TicketForm(request.POST)
        booking_form = BookingForm(request.POST)

        if (movie_form.is_valid() and theater_form.is_valid() and
                showtime_form.is_valid() and ticket_form.is_valid() and booking_form.is_valid()):
            with transaction.atomic():
                movie = movie_form.save()
                theater = theater_form.save()
                showtime = showtime_form.save(commit=False)
                showtime.movie = movie
                showtime.theater = theater
                showtime.save()
                ticket = ticket_form.save(commit=False)
                ticket.showtime = showtime
                ticket.save()
                booking = booking_form.save(commit=False)
                booking.showtime = showtime
                # Set the user properly, you might want to get this from the logged-in user or the form
                booking.user = booking_form.cleaned_data['user']
                booking.save()
                booking.tickets.add(ticket)

            return redirect('show_movies')
    else:
        movie_form = MovieForm()
        theater_form = TheaterForm()
        showtime_form = ShowtimeForm()
        ticket_form = TicketForm()
        booking_form = BookingForm()

    context = {
        'movie_form': movie_form,
        'theater_form': theater_form,
        'showtime_form': showtime_form,
        'ticket_form': ticket_form,
        'booking_form': booking_form
    }
    return render(request, 'add_movie.html', context)
