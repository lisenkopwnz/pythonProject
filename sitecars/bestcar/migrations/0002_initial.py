# Generated by Django 5.0.4 on 2024-06-14 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bestcar', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='publishing_a_trip',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publishing_a_trip',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bestcar.category', verbose_name='Категория'),
        ),
    ]
