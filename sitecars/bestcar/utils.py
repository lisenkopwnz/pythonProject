from bestcar.constants import *

class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = MENU

    def get_mixin_context(self, context, **kwargs):
        context['menu']=MENU
        context.update(kwargs)
        return context