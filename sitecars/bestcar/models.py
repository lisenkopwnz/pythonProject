from django.db import models

import re

from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import ModelForm

from django.contrib.auth import get_user_model
import datetime
import pytz



class CarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(cat_id=1)


class BusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(cat_id=2)


class ObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


class Publishing_a_trip(models.Model):
    SEATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
    ]

    departure = models.CharField(max_length=100,verbose_name="Отправление")
    arrival = models.CharField(max_length=100,verbose_name="Прибытие")
    models_auto = models.CharField(max_length=100,verbose_name="Модель автомобиля")
    date_time = models.DateTimeField(verbose_name="Дата и время")
    seating = models.PositiveSmallIntegerField(verbose_name= 'Количество мест', choices=SEATING, default=1)
    cat = models.ForeignKey('Category',verbose_name="Категория", on_delete=models.PROTECT)
    price = models.PositiveSmallIntegerField(verbose_name="Цена")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post', null=True, default=None)
    car = CarManager()
    bus = BusManager()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Опубликованные поездки'
        verbose_name_plural = 'Опубликованные поездки'
        ordering = ('date_time',)

    def __str__(self):
        return str(self.author)

    def clean(self):
        today = datetime.datetime.now().replace(tzinfo=pytz.UTC)
        if today > self.date_time:
            raise ValidationError('Введите корректную дату')



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name="Категория")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Publishing_a_tripForm(forms.ModelForm):

    class Meta:
        model = Publishing_a_trip
        fields = [ 'departure', 'arrival', 'models_auto', 'date_time', 'seating','price','cat']
        widgets = { 'date_time': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'})
        }

    @classmethod
    def __clean(cls,data):
        if re.search(r'[^а-яА-ЯёЁ]',data):
            raise ValidationError('Поле должно содержать только русские символы')
        return data


    def clean_departure(self):
        departure = self.cleaned_data['departure']
        return self.__clean(departure)

    def clean_arrival(self):
        arrival = self.cleaned_data['arrival']
        return self.__clean(arrival)



