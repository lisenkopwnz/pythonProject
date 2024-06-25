from bestcar.constants import *


class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = MENU  # Предполагается, что MENU - это глобальная переменная
        context.update(kwargs)
        context.update(self.extra_context)  # Добавляем extra_context в context
        return context
