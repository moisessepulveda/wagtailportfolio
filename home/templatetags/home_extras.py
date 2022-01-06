
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
def split(value, arg):
    return value.split(arg)