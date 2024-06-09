from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from accounts.models import Profile




def event_list(request):
    return render(request, 'event_list.html')

def event_detail(request):
    return render(request,'event_detail.html')

def buy_ticket(request):
    return render(request, 'buy_ticket.html')

def cancel_ticket(request):
    return render(request, 'cancel_ticket.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def movie(request):
    return render(request, 'movie.html')

def ipl(request):
    return render(request, 'ipl.html')

def travel(request):
    return render(request, 'travel.html')

def hotel(request):
    return render(request, 'hotel.html')    

def book(request):
    return render(request, 'book.html') 
   
# def home(request):
#     return render(request, 'home.html') 
  
def contactt(request):
    return render(request, 'contactt.html')     
      

def anime(request):
    return render(request, 'anime.html')     
            

def webseries(request):
    return render(request, 'webseries.html')     
                        
@login_required
def home(request):
    return render(request, 'home.html')