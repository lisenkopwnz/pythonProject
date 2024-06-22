from django.utils import timezone

from django.core.exceptions import ValidationError


class Validators_date_model:
    def __init__(self, message='Ведите коректную дату.'):
        self.message = message

    def __call__(self, value):
        now = timezone.now()
        if value < now:
            raise ValidationError(self.message)


class Validators_language_model:
    def __init__(self, message='Поле должно содержать только русские символы'):
        self.message = message

    def __call__(self, value):
        if re.search(r'[^а-яА-ЯёЁ]', data):
            raise ValidationError(self.message)
