# Generated by Django 5.0.4 on 2024-06-24 18:15

import bestcar.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestcar', '0004_alter_publishing_a_trip_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing_a_trip',
            name='arrival',
            field=models.CharField(max_length=100, validators=[bestcar.validators.Validators_language_model()], verbose_name='Прибытие'),
        ),
        migrations.AlterField(
            model_name='publishing_a_trip',
            name='arrival_time',
            field=models.DateTimeField(default=None, validators=[bestcar.validators.Validators_date_model()], verbose_name='Время прибытия'),
        ),
        migrations.AlterField(
            model_name='publishing_a_trip',
            name='cat',
            field=models.ForeignKey(choices=[(1, 'На машине'), (2, 'На автобусе')], on_delete=django.db.models.deletion.PROTECT, to='bestcar.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='publishing_a_trip',
            name='departure',
            field=models.CharField(max_length=100, validators=[bestcar.validators.Validators_language_model()], verbose_name='Отправление'),
        ),
        migrations.AlterField(
            model_name='publishing_a_trip',
            name='departure_time',
            field=models.DateTimeField(validators=[bestcar.validators.Validators_date_model()], verbose_name='Время отправления'),
        ),
    ]
