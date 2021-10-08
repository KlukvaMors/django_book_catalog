from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr)

@register.filter
def to_model_name(value):
    return value.__class__.__name__.lower()
