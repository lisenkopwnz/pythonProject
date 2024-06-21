from django.utils import timezone
import datetime
import pytz

from django.core.exceptions import ValidationError

def check_arrival_time(value):
    now = timezone.now()
    if value < now:
        raise ValidationError('Ведите коректную дату.')

def check_departure_time(value):
    now = timezone.now()
    if value < now:
        raise ValidationError('Ведите коректную дату.')
