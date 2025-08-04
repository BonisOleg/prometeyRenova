"""
Context processors для передачі додаткових змінних в шаблони
"""

def debug_processor(request):
    """
    Передає DEBUG змінну в шаблони
    """
    from django.conf import settings
    return {'debug': settings.DEBUG} 