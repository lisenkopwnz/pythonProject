from django.contrib import admin
from .models import Publishing_a_trip,Category


@admin.register(Publishing_a_trip)
class Publishing_a_trip_admin(admin.ModelAdmin):
    list_display_links = ('id', 'name')
    list_display = ('id', 'name', 'departure', 'arrival','models_auto',
                    'date_time','seating','cat','price')
    ordering = ['departure', 'arrival', 'date_time']

@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display_links = ('id', 'name')
    list_display = ('id', 'name')
    ordering = ['name']




