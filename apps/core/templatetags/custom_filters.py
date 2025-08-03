from django import template

register = template.Library()


@register.filter
def split(value, arg):
    """
    Розділяє рядок на список за роздільником
    Використання: {{ value|split:"," }}
    """
    if value:
        return [item.strip() for item in value.split(arg)]
    return [] 