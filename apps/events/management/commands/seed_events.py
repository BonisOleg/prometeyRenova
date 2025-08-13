from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.events.models import Event, EventCategory
from datetime import timedelta

class Command(BaseCommand):
    help = 'Створює демо-категорії та події для сторінки Події'

    def handle(self, *args, **options):
        categories_spec = [
            ('вебінари', '#DC143C'),
            ('курси', '#000000'),
            ('знижки', '#F5F1ED'),
            ('майстер-класи', '#FAF7F2'),
        ]

        slug_map = {
            'вебінари': 'webinars',
            'курси': 'courses',
            'знижки': 'discounts',
            'майстер-класи': 'workshops',
        }

        categories = {}
        for name, color in categories_spec:
            cat, _ = EventCategory.objects.get_or_create(
                slug=slug_map[name],
                defaults={'name': name, 'color': color},
            )
            categories[name] = cat

        now = timezone.now()
        demo_events = [
            {
                'title': 'Вебінар: Django + React — повний стек',
                'excerpt': 'Практичний воркшоп: як швидко зʼєднати Django API та React UI.',
                'content': 'Детальна програма, посилання на матеріали, Q&A. Онлайн, запис буде.',
                'category': categories['вебінари'],
                'event_type': 'webinar',
                'status': 'upcoming',
                'start_date': now + timedelta(days=3),
                'end_date': now + timedelta(days=3, hours=2),
                'is_online': True,
                'price': None,
                'original_price': None,
                'discount_percent': 0,
                'max_participants': 200,
                'is_published': True,
                'is_featured': True,
            },
            {
                'title': 'Курс: Python для веб-розробників',
                'excerpt': '8 тижнів інтенсиву: Django, REST, деплой та best practices.',
                'content': 'Програма курсу, розклад занять, домашні завдання, менторська підтримка.',
                'category': categories['курси'],
                'event_type': 'course',
                'status': 'active',
                'start_date': now - timedelta(days=2),
                'end_date': now + timedelta(days=26),
                'is_online': True,
                'price': 6000,
                'original_price': 7500,
                'discount_percent': 20,
                'max_participants': 50,
                'is_published': True,
                'is_featured': True,
            },
            {
                'title': 'Знижка -30% на індивідуальний менторинг',
                'excerpt': 'Обмежена пропозиція до кінця місяця на персональні сесії.',
                'content': 'Деталі пакету, як записатися, теми менторства, відгуки.',
                'category': categories['знижки'],
                'event_type': 'discount',
                'status': 'active',
                'start_date': now - timedelta(days=1),
                'end_date': now + timedelta(days=5),
                'is_online': True,
                'price': 1400,
                'original_price': 2000,
                'discount_percent': 30,
                'max_participants': None,
                'is_published': True,
                'is_featured': False,
            },
            {
                'title': 'Майстер-клас: Оптимізація фронтенду під iOS Safari',
                'excerpt': 'Практика адаптації анімацій, viewport та safe-area.',
                'content': 'Живі приклади, профілювання, покрокові рекомендації.',
                'category': categories['майстер-класи'],
                'event_type': 'workshop',
                'status': 'upcoming',
                'start_date': now + timedelta(days=10),
                'end_date': now + timedelta(days=10, hours=3),
                'is_online': False,
                'location': 'Kyiv HUB',
                'price': 900,
                'original_price': 900,
                'discount_percent': 0,
                'max_participants': 30,
                'is_published': True,
                'is_featured': False,
            },
        ]

        created, updated = 0, 0
        for data in demo_events:
            obj, is_created = Event.objects.update_or_create(
                slug=None,
                defaults=data,
                title=data['title'],
            )
            if is_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(f'Категорії: {len(categories)}. Події створено: {created}, оновлено: {updated}'))
