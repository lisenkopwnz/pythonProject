from django.urls import path

from . import views
from .views import HommeBestcar, SearchTrip, Post



urlpatterns = [
    path('',HommeBestcar.as_view(), name='home'),
    path('search/',SearchTrip.as_view(), name='search'),
    path('post/', Post.as_view(), name='post'),
    path('about/', views.about, name='about'),
    path('to_book/<int:trip_id>/', views.to_book, name='to_book'),


]
