from django.urls import path

from . import views
from .views import HommeBestcar, SearchTrip, Post, Bus_trip, Car_trip

urlpatterns = [
    path('', HommeBestcar.as_view(), name='home'),
    path('search/', SearchTrip.as_view(), name='search'),
    path('post/', Post.as_view(), name='post'),
    path('bus_trip/', Bus_trip.as_view(), name='bus_trip'),
    path('car_trip/', Car_trip.as_view(), name='car_trip'),
    path('about/', views.about, name='about'),
    path('to_book/<slug:trip_slug>/', views.to_book, name='to_book'),
    path('booking/checkout/<slug:trip_slug>/', views.booking_checkout, name='booking'),

    path('your-server-endpoint/', views.json_form_view, name='json_form'),

]
