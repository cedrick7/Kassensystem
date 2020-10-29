from django import template

register = template.Library()

@register.filter
def mult(value, list):
    num = len(list)
    return float(value)*float(num)
    