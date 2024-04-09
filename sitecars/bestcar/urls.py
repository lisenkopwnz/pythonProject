from django.urls import path

from . import views
from .views import HommeBestcar, SearchTrip, Post, BusRide, TripComp

urlpatterns = [
    path('',HommeBestcar.as_view(), name='home'),
    path('bus/',BusRide.as_view(),name='bus'),
    path('companion/', TripComp.as_view(),name='companion'),
    path('search/',SearchTrip.as_view(), name='search'),
    path('post/', Post.as_view(), name='post'),
    path('about/', views.about, name='about'),

]
