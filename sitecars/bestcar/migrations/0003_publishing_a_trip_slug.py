# Generated by Django 5.0.4 on 2024-06-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestcar', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishing_a_trip',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100),
        ),
    ]