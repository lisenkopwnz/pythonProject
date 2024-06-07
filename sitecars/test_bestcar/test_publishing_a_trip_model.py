import datetime

import pytest
import pytz
from django.core.exceptions import ValidationError

from bestcar.models import Publishing_a_trip, Category
from users.models import User
from contextlib import nullcontext as does_not_raise


class Test_models_Publishing_a_trip:
    @pytest.fixture
    def create_object(self, db):
        dete_time = datetime.datetime.strptime('2022-06-05 18:02:00', '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.UTC)
        self.category = Category.objects.create(name='На машине')
        self.user = User.objects.create(username='Денис', first_name='Иванов', last_name='Иванович', email='dii@.com',
                                        password='123')
        self.trip = Publishing_a_trip.objects.create(departure='Москва', arrival='Пушкин', models_auto='BMW',
                                                     date_time=dete_time, seating=1, cat=self.category,
                                                     price=100, author=self.user)

    def test_user_create(self, create_object):
        trip = Publishing_a_trip.objects.filter(departure='Москва').exists()
        assert trip == True

    def test_verbose_name(self, create_object):
        field_label_departure = Publishing_a_trip._meta.get_field('departure').verbose_name
        field_label_arrival = Publishing_a_trip._meta.get_field('arrival').verbose_name
        field_label_models_auto = Publishing_a_trip._meta.get_field('models_auto').verbose_name
        field_label_date_time = Publishing_a_trip._meta.get_field('date_time').verbose_name
        field_label_seating = Publishing_a_trip._meta.get_field('seating').verbose_name
        field_label_cat = Publishing_a_trip._meta.get_field('cat').verbose_name
        field_label_price = Publishing_a_trip._meta.get_field('price').verbose_name
        field_label_author = Publishing_a_trip._meta.get_field('author').verbose_name
        assert field_label_departure == "Отправление"
        assert field_label_arrival == "Прибытие"
        assert field_label_models_auto == "Модель автомобиля"
        assert field_label_date_time == "Дата и время"
        assert field_label_seating == "Количество мест"
        assert field_label_cat == "Категория"
        assert field_label_price == "Цена"
        assert field_label_author == "author"

    def test_clean(self,create_object):
        with pytest.raises(ValidationError):
            assert self.trip.clean() == True

    def test_str(self,create_object):
        assert str(self.trip) == 'Денис'
