# Generated by Django 5.0.4 on 2024-06-03 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestcar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing_a_trip',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestcar.category', verbose_name='Категория'),
        ),
    ]
