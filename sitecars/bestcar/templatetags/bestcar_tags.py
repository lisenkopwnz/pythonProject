from django import template

from bestcar.constants import *

register = template.Library()

@register.simple_tag()
def aaa():
    return MENU