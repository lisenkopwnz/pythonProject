# Generated by Django 5.0.4 on 2024-07-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestcar', '0008_alter_publishing_a_trip_author_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'зарезервированные поездки', 'verbose_name_plural': 'зарезервированные поездки'},
        ),
        migrations.AddField(
            model_name='publishing_a_trip',
            name='reserved_seats',
            field=models.PositiveIntegerField(default=0, verbose_name='количество_зарезервиронных_мест'),
        ),
    ]