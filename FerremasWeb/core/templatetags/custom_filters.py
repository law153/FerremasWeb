from django import template

register = template.Library()

@register.filter
def divide_by(value, arg):
    return value / arg
