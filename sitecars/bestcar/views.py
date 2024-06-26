from django.shortcuts import render
from bestcar.utils import DataMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, request, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin

from bestcar.models import Publishing_a_trip, Publishing_a_tripForm
from bestcar.models import *
from sitecars import settings
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json


class HommeBestcar(DataMixin, TemplateView):
    model = Publishing_a_trip
    template_name = 'bestcar/index.html'
    title_page = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class Bus_trip(DataMixin, ListView):
    model = Publishing_a_trip
    template_name = 'bestcar/bus_trip.html'
    title_page = 'На автобусе'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class Car_trip(DataMixin, ListView):
    model = Publishing_a_trip
    template_name = 'bestcar/car_trip.html'
    title_page = 'На машине'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class SearchTrip(DataMixin, ListView):
    template_name = 'bestcar/search.html'
    title_page = 'Поиск'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, default_image=settings.DEFAULT_USER_IMAGE)

    def get_queryset(self):
        departure = self.request.GET.get('d')
        arrival = self.request.GET.get('a')
        seating = self.request.GET.get('s')
        data = self.request.GET.get('t')
        cat = self.request.GET.get('cat')

        # Словарь для сопоставления категорий с фильтрами
        filters_map = {
            'На машине ': Publishing_a_trip.car,
            'На автобусе': Publishing_a_trip.bus,
            # Добавьте другие категории здесь, если они будут использоваться
        }

        # Получение объектов на основе выбранной категории или всех объектов, если категория не найдена
        object_list = filters_map.get(cat, Publishing_a_trip.objects).filter(
            Q(departure__istartswith=departure) &
            Q(arrival__istartswith=arrival) &
            Q(seating__istartswith=seating) &
            Q(departure_time__startswith=data))
        return object_list


class Post(DataMixin, LoginRequiredMixin, CreateView):
    form_class = Publishing_a_tripForm
    template_name = 'bestcar/post.html'
    success_url = reverse_lazy('home')
    title_page = 'Опубликовать поездку'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


def to_book(request, trip_slug):
    obj = get_object_or_404(Publishing_a_trip, slug=trip_slug)

    return render(request, 'bestcar/to_book_a_trip.html', {'obj': obj, 'default_image': settings.DEFAULT_USER_IMAGE})


def booking_checkout(request, trip_slug):
    obj = get_object_or_404(Publishing_a_trip, slug=trip_slug)
    return render(request, 'bestcar/booking_checkout.html', {'obj': obj})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h>Упс ,что пошло не так</h>")


def about(request):
    previous_url = request.META.get('HTTP_REFERER')
    return render(request, 'bestcar/about.html',
                  {'previous_url': previous_url})


@csrf_exempt
def json_form_view(request):
    if request.method == 'POST':

        # Извлекаем данные из запроса
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        print(data)
        print(data_json)

        # Извлекаем ключ и значение из данных

        key = data_json.get('checkbox1')
        print(key)
        value = data_json.get('checkbox2')
        print(value)

        # Логика обработки данных


        result = {"success": True, "message": f"Received key={key}, value={value}"}
        # Возвращаем ответ в формате JSON
        return JsonResponse(result)
    else:
        # Обработка других HTTP-методов или возврат ошибки для несоответствующих запросов
        return JsonResponse({"error": "Invalid request method"}, status=405)
