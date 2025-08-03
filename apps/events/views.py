from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from .models import Event, EventCategory, EventRegistration


def events_list(request):
    """Список подій з фільтрацією"""
    events = Event.objects.filter(is_published=True).select_related('category')
    
    # Фільтри
    category_slug = request.GET.get('category')
    event_type = request.GET.get('type')
    status = request.GET.get('status')
    
    if category_slug:
        events = events.filter(category__slug=category_slug)
    
    if event_type:
        events = events.filter(event_type=event_type)
    
    if status:
        events = events.filter(status=status)
    
    # Сортування
    sort_by = request.GET.get('sort', '-start_date')
    events = events.order_by(sort_by)
    
    # Пагінація
    paginator = Paginator(events, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Категорії для фільтрів
    categories = EventCategory.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category_slug,
        'current_type': event_type,
        'current_status': status,
        'current_sort': sort_by,
        'page_title': 'Події та акції | PrometeyLabs',
        'meta_description': 'Актуальні вебінари, курси, знижки та події від PrometeyLabs. Реєструйтесь на безкоштовні вебінари та отримуйте знижки на курси програмування.',
        'og_title': 'Події PrometeyLabs - Вебінари, курси, знижки',
        'keywords': 'події вебінари, курси програмування, знижки, акції, веб розробка, Python Django',
    }
    return render(request, 'pages/events.html', context)


def event_detail(request, slug):
    """Детальна сторінка події"""
    event = get_object_or_404(Event, slug=slug, is_published=True)
    
    # Перевіряємо чи користувач вже реєструвався
    user_registered = False
    if request.user.is_authenticated:
        user_registered = EventRegistration.objects.filter(
            event=event, 
            email=request.user.email
        ).exists()
    
    # Схожі події
    similar_events = Event.objects.filter(
        is_published=True,
        category=event.category
    ).exclude(id=event.id)[:3]
    
    context = {
        'event': event,
        'similar_events': similar_events,
        'user_registered': user_registered,
        'page_title': event.seo_title or event.title,
        'meta_description': event.seo_description,
        'og_title': event.title,
        'keywords': event.keywords,
    }
    return render(request, 'pages/event_detail.html', context)


def event_registration(request, event_id):
    """Реєстрація на подію"""
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id, is_published=True)
        
        # Перевіряємо чи можна реєструватися
        if not event.is_registration_open:
            messages.error(request, 'Реєстрація на цю подію закрита.')
            return redirect('event_detail', slug=event.slug)
        
        if event.is_full:
            messages.error(request, 'На жаль, всі місця на цю подію вже зайняті.')
            return redirect('event_detail', slug=event.slug)
        
        # Перевіряємо чи користувач вже реєструвався
        if EventRegistration.objects.filter(event=event, email=request.POST.get('email')).exists():
            messages.warning(request, 'Ви вже зареєстровані на цю подію.')
            return redirect('event_detail', slug=event.slug)
        
        # Створюємо реєстрацію
        try:
            registration = EventRegistration.objects.create(
                event=event,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                company=request.POST.get('company', ''),
                message=request.POST.get('message', '')
            )
            
            messages.success(request, f'Ви успішно зареєструвалися на подію "{event.title}"!')
            return redirect('event_detail', slug=event.slug)
            
        except Exception as e:
            messages.error(request, 'Помилка при реєстрації. Спробуйте ще раз.')
            return redirect('event_detail', slug=event.slug)
    
    return redirect('events_list')


def events_ajax_filter(request):
    """AJAX фільтрація подій"""
    if request.is_ajax():
        events = Event.objects.filter(is_published=True).select_related('category')
        
        # Застосовуємо фільтри
        category_slug = request.GET.get('category')
        event_type = request.GET.get('type')
        status = request.GET.get('status')
        
        if category_slug:
            events = events.filter(category__slug=category_slug)
        
        if event_type:
            events = events.filter(event_type=event_type)
        
        if status:
            events = events.filter(status=status)
        
        # Сортування
        sort_by = request.GET.get('sort', '-start_date')
        events = events.order_by(sort_by)
        
        # Пагінація
        paginator = Paginator(events, 6)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        # Формуємо HTML для подій
        events_html = []
        for event in page_obj:
            events_html.append({
                'id': event.id,
                'title': event.title,
                'excerpt': event.excerpt,
                'start_date': event.start_date.strftime('%d.%m.%Y %H:%M'),
                'category_name': event.category.name,
                'category_color': event.category.color,
                'event_type': event.get_event_type_display(),
                'price': str(event.price) if event.price else 'Безкоштовно',
                'is_online': event.is_online,
                'url': event.get_absolute_url(),
                'image_url': event.image.url if event.image else '',
                'is_featured': event.is_featured,
                'is_registration_open': event.is_registration_open,
                'available_spots': event.available_spots,
            })
        
        return JsonResponse({
            'events': events_html,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages,
        })
    
    return JsonResponse({'error': 'Invalid request'}) 