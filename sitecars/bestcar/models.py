from django.db import models

import re

from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import ModelForm


class Publishing_a_trip(models.Model):
    SEATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
    ]
    name = models.CharField(max_length=100,verbose_name="Имя")
    departure = models.CharField(max_length=100,verbose_name="Отправление")
    arrival = models.CharField(max_length=100,verbose_name="Прибытие")
    models_auto = models.CharField(max_length=100,verbose_name="Модель автомобиля")
    date_time = models.DateTimeField(verbose_name="Дата и время")
    seating = models.PositiveSmallIntegerField(verbose_name= 'Количество мест', choices=SEATING, default=1)
    cat = models.ForeignKey('Category',verbose_name="Катигория", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Выберите транспортное средство")
    def __str__(self):
        return self.name

class Publishing_a_tripForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Publishing_a_trip
        fields = ['name', 'departure', 'arrival', 'models_auto', 'date_time', 'seating','cat']
        widgets = { 'date_time': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.search(r'[^а-яА-ЯёЁ]',name):
            raise ValidationError('Поле должно содержать только русские символы')
        return name

    def clean_departure(self):
        departure = self.cleaned_data['departure']
        if re.search(r'[^а-яА-ЯёЁ]',departure):
            raise ValidationError('Поле должно содержать только русские символы')
        return departure

    def clean_arrival(self):
        arrival = self.cleaned_data['arrival']
        if re.search(r'[^а-яА-ЯёЁ]',arrival):
            raise ValidationError('Поле должно содержать только русские символы')
        return arrival

