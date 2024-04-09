from django.shortcuts import render

from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from bestcar.models import Publishing_a_trip, Publishing_a_tripForm
from bestcar.models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
       {'title': 'На автобусе', 'url_name': 'bus'},
       {'title': 'С попутчиком', 'url_name': 'companion'},
       {'title': 'Опубликовать поездку', 'url_name': 'post'},
        ]

class HommeBestcar(ListView):
    model = Publishing_a_trip
    template_name = 'bestcar/index.html'
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'

        return context

class BusRide(ListView):
    model = Publishing_a_trip
    template_name = 'bestcar/bus_ride.html'
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class TripComp(ListView):
    model = Publishing_a_trip
    template_name = 'bestcar/trip_companion.html'
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class SearchTrip(ListView):
    template_name = 'bestcar/search.html'
    def get_queryset(self):
        departure = self.request.GET.get('d')
        arrival = self.request.GET.get('a')
        seating = self.request.GET.get('s')
        data = self.request.GET.get('t')
        object_list = Publishing_a_trip.objects.filter(Q(departure__istartswith=departure) & Q(arrival__istartswith=arrival)
                    & Q(seating__istartswith=seating) & Q(date_time__startswith=data))
        return object_list


class Post(CreateView):
    form_class = Publishing_a_tripForm
    template_name = 'bestcar/post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить поездку'
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound("<h>Упс ,что пошло не так</h>")


def about(request):
    return render(request, 'bestcar/about.html',
                  {'title': 'О сайте',"menu": menu})



