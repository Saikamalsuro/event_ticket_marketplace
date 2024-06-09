
from django.contrib import admin 
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import  settings 
from django.contrib.auth import views as auth_views


from .views import event_detail,buy_ticket,cancel_ticket,event_list,login,about,register,index,contact,movie,ipl,travel,hotel,book,home,contactt




urlpatterns = [
    path('admin/', admin.site.urls),
    path('event_list/', event_list, name='event_list'),
    path('event_detail/', event_detail, name='event_detail'),
    path('buy_ticket/', buy_ticket, name='buy_ticket'),
    path('cancel_ticket/', cancel_ticket, name='cancel_ticket'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('index', index, name='index'),
    path('register/', register, name='register'),
    path('contact/', contact, name='contact'),
    path('movie/', movie, name='movie'),
    path('ipl/', ipl, name='ipl'),
    path('travel/', travel, name='travel'),
    path('hotel/', hotel, name='hotel'),
    path('book/', book, name='book'),
    path('contactt/', contactt, name='contactt'),
    path('', home, name='home'),
    path('', include('movie.urls')),
    path('', include('anime.urls')),
    path('', include('webseries.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('accounts.urls')),
  # Include URLs from the movies app
]


path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),