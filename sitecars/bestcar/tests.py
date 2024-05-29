from sitecars.wsgi import *

from django.test import TestCase
from bestcar.models import Publishing_a_trip

from django.contrib.auth import get_user_model

class Publishing_a_tripTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.object = Publishing_a_trip.objects.create(name="Толик", departure="Москва", arrival='Новгород',
                                                      date_time='2012-09-04 06:00:00.000000', seating='5',
                                                      cat_id='1', price='1000')

    def test_verbose_label(self):
        trip = Publishing_a_trip.objects.get(id=1)
        field_label_name = trip._meta.get_field('name').verbose_name
        field_label_departure = trip._meta.get_field('departure').verbose_name
        field_label_arrival = trip._meta.get_field('arrival').verbose_name
        field_label_models_auto = trip._meta.get_field('models_auto').verbose_name
        field_label_date_time = trip._meta.get_field('date_time').verbose_name
        field_label_seating = trip._meta.get_field('seating').verbose_name
        field_label_cat_id = trip._meta.get_field('cat_id').verbose_name
        field_label_price = trip._meta.get_field('price').verbose_name
        self.assertEqual(field_label_name, 'Имя')
        self.assertEqual(field_label_departure, 'Отправление')
        self.assertEqual(field_label_arrival, 'Прибытие')
        self.assertEqual(field_label_models_auto, 'Модель автомобиля')
        self.assertEqual(field_label_date_time, 'Дата и время')
        self.assertEqual(field_label_seating, 'Количество мест')
        self.assertEqual(field_label_cat_id, 'Категория')
        self.assertEqual(field_label_price, 'Цена')

    def test_max_length(self):
        trip = Publishing_a_trip.objects.get(id=1)
        max_length_name = trip._meta.get_field('name').max_length
        max_length_departure = trip._meta.get_field('departure').max_length
        max_length_arrival = trip._meta.get_field('arrival').max_length
        max_length_models_auto = trip._meta.get_field('models_auto').max_length
        self.assertEqual(max_length_name,100)
        self.assertEqual(max_length_departure, 100)
        self.assertEqual(max_length_arrival, 100)
        self.assertEqual(max_length_models_auto, 100)











