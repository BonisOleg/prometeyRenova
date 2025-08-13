from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import json
import logging

# Налаштування логування
logger = logging.getLogger(__name__)

# ===== БАЗОВІ СТОРІНКИ =====

class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'PrometeyLabs - Розробка сайтів під ключ | Telegram боти | Реклама',
            'meta_description': 'PrometeyLabs - професійна розробка сайтів під ключ, створення Telegram ботів, налаштування реклами Google Ads, навчання веб-розробки. Сучасні технології, конкурентні ціни.',
            'og_title': 'PrometeyLabs - Розробка сайтів під ключ',
            'current_year': 2024,
        })
        return context

class PortfolioView(TemplateView):
    template_name = 'pages/portfolio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Портфоліо | Створені нами сайти під ключ - PrometeyLabs',
            'meta_description': 'Портфоліо PrometeyLabs - приклади створених сайтів під ключ, Telegram ботів, налаштованої реклами. Подивіться на наші роботи та оцініть якість.',
            'current_year': 2024,
        })
        return context

class CalculatorView(TemplateView):
    template_name = 'pages/calculator.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Розрахувати вартість сайту | Калькулятор ціни - PrometeyLabs',
            'meta_description': 'Розрахуйте вартість створення сайту онлайн. Сучасні технології знижують ціну розробки. Тест для точного розрахунку вартості проекту.',
            'current_year': 2024,
        })
        return context

class DeveloperView(TemplateView):
    template_name = 'pages/developer.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Курси програмування | Стати веб-розробником - PrometeyLabs',
            'meta_description': 'Курси програмування у PrometeyLabs. Навчання веб-розробки з нуля. Індивідуальні та групові заняття. Практичний досвід, сучасні технології.',
            'current_year': 2024,
        })
        return context

class ContactsView(TemplateView):
    template_name = 'pages/contacts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Контакти | PrometeyLabs - Зв\'яжіться з нами',
            'meta_description': 'Зв\'яжіться з командою PrometeyLabs для розробки сайтів, Telegram ботів, реклами чи навчання. Київ, Україна.',
            'current_year': 2024,
        })
        return context


# ===== AJAX ОБРОБКА ФОРМ =====

def handle_form_submission(request):
    """Обробка AJAX форм"""
    if request.method == 'POST':
        try:
            # Отримуємо тип форми з data-form-type або окремого поля
            form_type = request.POST.get('form_type') or get_form_type_from_path(request)
            name = request.POST.get('name', '').strip()
            phone = request.POST.get('phone', '').strip()
            
            # Валідація базових полів
            if not name or not phone:
                return JsonResponse({
                    'success': False,
                    'message': 'Заповніть обов\'язкові поля: ім\'я та телефон'
                }, status=400)
            
            # Валідація телефону (базова)
            if not validate_phone(phone):
                return JsonResponse({
                    'success': False,
                    'message': 'Введіть коректний номер телефону'
                }, status=400)
            
            # Обробка різних типів форм
            handlers = {
                'site-request': handle_site_request,
                'developer': handle_developer_request,
                'consultation': handle_consultation_request,
                'contact': handle_contact_request
            }
            
            handler = handlers.get(form_type)
            if handler:
                return handler(request, name, phone)
            else:
                return JsonResponse({
                    'success': False,
                    'message': f'Невідомий тип форми: {form_type}'
                }, status=400)
                
        except Exception as e:
            print(f"Form submission error: {e}")  # Для debug
            return JsonResponse({
                'success': False,
                'message': 'Сталася помилка при обробці заявки. Спробуйте ще раз.'
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Метод не дозволений'
    }, status=405)

def get_form_type_from_path(request):
    """Визначає тип форми на основі URL або інших параметрів"""
    # Можна визначити тип форми на основі Referer або інших заголовків
    referer = request.META.get('HTTP_REFERER', '')
    if 'calculator' in referer:
        return 'site-request'
    elif 'developer' in referer:
        return 'developer'

    return 'consultation'  # default

def validate_phone(phone):
    """Базова валідація номера телефону"""
    import re
    # Прибираємо всі символи крім цифр та +
    clean_phone = re.sub(r'[^\d+]', '', phone)
    # Перевіряємо що номер має правильну довжину
    return len(clean_phone) >= 10 and len(clean_phone) <= 15

def handle_site_request(request, name, phone):
    """Обробка заявки на сайт"""
    details = request.POST.get('details', '')
    email = request.POST.get('email', '')
    
    # Створюємо дані для email
    form_data = {
        'type': 'Заявка на розробку сайту',
        'name': name,
        'phone': phone,
        'details': details,
        'email': email,
        'timestamp': timezone.now().strftime('%d.%m.%Y %H:%M')
    }
    
    # Відправляємо email
    send_form_email(form_data)
    
    # Зберігаємо в БД (буде реалізовано пізніше)
    save_form_submission('site-request', form_data)
    
    return JsonResponse({
        'success': True,
        'message': 'Дякуємо! Ваша заявка отримана. Ми зв\'яжемося з вами найближчим часом.',
        'redirect': None
    })

def handle_developer_request(request, name, phone):
    """Обробка заявки на курси"""
    course_type = request.POST.get('course_type', '')
    experience = request.POST.get('experience', '')
    email = request.POST.get('email', '')
    
    # Створюємо дані для email
    form_data = {
        'type': 'Заявка на курси програмування',
        'name': name,
        'phone': phone,
        'course_type': course_type,
        'experience': experience,
        'email': email,
        'timestamp': timezone.now().strftime('%d.%m.%Y %H:%M')
    }
    
    # Відправляємо email
    send_form_email(form_data)
    
    # Зберігаємо в БД
    save_form_submission('developer', form_data)
    
    return JsonResponse({
        'success': True,
        'message': 'Дякуємо! Ваша заявка на курси отримана. Ми надішлемо детальну інформацію.',
        'redirect': None
    })

def handle_consultation_request(request, name, phone):
    """Обробка заявки на консультацію"""
    topic = request.POST.get('topic', '')
    email = request.POST.get('email', '')
    
    # Створюємо дані для email
    form_data = {
        'type': 'Заявка на консультацію',
        'name': name,
        'phone': phone,
        'topic': topic,
        'email': email,
        'timestamp': timezone.now().strftime('%d.%m.%Y %H:%M')
    }
    
    # Відправляємо email
    send_form_email(form_data)
    
    # Зберігаємо в БД
    save_form_submission('consultation', form_data)
    
    return JsonResponse({
        'success': True,
        'message': 'Дякуємо! Наш спеціаліст зв\'яжеться з вами протягом 15 хвилин.',
        'redirect': None
    })

def handle_contact_request(request, name, phone):
    """Обробка заявки зі сторінки контактів"""
    message = request.POST.get('message', '')
    email = request.POST.get('email', '')
    
    # Створюємо дані для email
    form_data = {
        'type': 'Заявка зі сторінки контактів',
        'name': name,
        'phone': phone,
        'message': message,
        'email': email,
        'timestamp': timezone.now().strftime('%d.%m.%Y %H:%M'),
        'ip': request.META.get('REMOTE_ADDR', ''),
        'user_agent': request.META.get('HTTP_USER_AGENT', '')
    }
    
    # Відправляємо email
    send_form_email(form_data)
    
    # Зберігаємо в БД
    save_form_submission('contact', form_data)
    
    return JsonResponse({
        'success': True,
        'message': 'Дякуємо за ваше повідомлення! Ми зв\'яжемося з вами найближчим часом.',
        'redirect': None
    })



def handle_test_submission(request):
    """Обробка тесту для калькулятора"""
    if request.method == 'POST':
        try:
            # Отримуємо відповіді на тест
            answers = {}
            for i in range(1, 6):  # 5 питань
                answer = request.POST.get(f'question_{i}')
                if answer:
                    answers[f'question_{i}'] = answer
            
            name = request.POST.get('name', '')
            phone = request.POST.get('phone', '')
            
            if not name or not phone:
                return JsonResponse({
                    'success': False,
                    'message': 'Заповніть ім\'я та телефон'
                }, status=400)
            
            # Розрахунок базової ціни на основі відповідей
            base_price = calculate_project_price(answers)
            
            # Підготовка даних для email
            test_data = {
                'name': name,
                'phone': phone,
                'email': request.POST.get('email', ''),
                'answers': answers,
                'ip': request.META.get('REMOTE_ADDR', ''),
                'user_agent': request.META.get('HTTP_USER_AGENT', '')
            }
            
            # Відправка email з результатом
            send_test_result_email(test_data, base_price)
            
            # Збереження результату в БД
            save_form_submission('test_result', {
                'type': 'Результат тесту калькулятора',
                'name': name,
                'phone': phone,
                'estimated_price': base_price,
                'answers': answers,
                'timestamp': timezone.now().strftime('%d.%m.%Y %H:%M')
            })
            
            return JsonResponse({
                'success': True,
                'message': f'Дякуємо! Орієнтовна вартість проекту: {base_price} грн. Детальний розрахунок надіслано на email.',
                'estimated_price': base_price,
                'answers': answers
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Помилка при обробці тесту'
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Метод не дозволений'
    }, status=405)

def calculate_project_price(answers):
    """Розрахунок орієнтовної ціни проекту"""
    base_prices = {
        'A': 15000,  # Веб-сайт
        'B': 8000,   # Telegram бот
        'C': 5000,   # Реклама
        'D': 25000,  # Інтернет-магазин
        'E': 35000   # Мобільний додаток
    }
    
    # Базова ціна на основі першого питання
    project_type = answers.get('question_1', 'A')
    base_price = base_prices.get(project_type, 15000)
    
    # Коригування на основі інших відповідей
    urgency = answers.get('question_3', 'B')
    if urgency == 'A':  # Терміново
        base_price *= 1.5
    elif urgency == 'C':  # Не поспішаємо
        base_price *= 0.9
    
    payment = answers.get('question_4', 'A')
    if payment in ['B', 'C', 'D', 'E']:  # Потрібна оплата
        base_price += 5000
    
    return int(base_price)

# ===== EMAIL ТА ЗБЕРЕЖЕННЯ ДАНИХ =====

def send_form_email(form_data):
    """Відправка email з даними форми"""
    try:
        # Формуємо тему email
        subject = f"[PrometeyLabs] {form_data['type']}"
        
        # Формуємо тіло email
        message_body = f"""
Нова заявка з сайту PrometeyLabs

Тип заявки: {form_data['type']}
Дата: {form_data['timestamp']}

=== КОНТАКТНІ ДАНІ ===
Ім'я: {form_data['name']}
Телефон: {form_data['phone']}
Email: {form_data.get('email', 'Не вказано')}

=== ДЕТАЛІ ЗАЯВКИ ===
"""
        
        # Додаємо специфічні поля в залежності від типу форми
        if 'details' in form_data and form_data['details']:
            message_body += f"Опис проекту: {form_data['details']}\n"
        
        if 'message' in form_data and form_data['message']:
            message_body += f"Повідомлення: {form_data['message']}\n"
        
        if 'course_type' in form_data and form_data['course_type']:
            message_body += f"Тип курсу: {form_data['course_type']}\n"
        
        if 'experience' in form_data and form_data['experience']:
            message_body += f"Досвід: {form_data['experience']}\n"
        
        if 'topic' in form_data and form_data['topic']:
            message_body += f"Тема консультації: {form_data['topic']}\n"
        
        message_body += f"\n=== ДОДАТКОВА ІНФОРМАЦІЯ ===\nIP: {form_data.get('ip', 'Невідомо')}\nUser Agent: {form_data.get('user_agent', 'Невідомо')}"
        
        # Відправляємо email
        send_mail(
            subject=subject,
            message=message_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        logger.info(f"Email sent successfully for form type: {form_data['type']}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        return False

def save_form_submission(form_type, form_data):
    """Збереження даних форми в БД (placeholder)"""
    try:
        # TODO: Реалізувати збереження в БД коли будуть створені моделі
        logger.info(f"Form data saved: {form_type} - {form_data['name']}")
        return True
    except Exception as e:
        logger.error(f"Failed to save form data: {e}")
        return False

def send_test_result_email(test_data, estimated_price):
    """Відправка email з результатом тесту"""
    try:
        name = test_data['name']
        phone = test_data['phone']
        answers = test_data['answers']
        
        # Email для клієнта
        client_subject = "Результат розрахунку вартості проекту - PrometeyLabs"
        client_message = f"""
Дякуємо за проходження тесту!

Вітаємо, {name}!

На основі ваших відповідей, орієнтовна вартість проекту становить: {estimated_price} грн

=== ВАШІ ВІДПОВІДІ ===
1. Тип проекту: {get_answer_text('question_1', answers.get('question_1', ''))}
2. Канал зв'язку: {get_answer_text('question_2', answers.get('question_2', ''))}
3. Терміни: {get_answer_text('question_3', answers.get('question_3', ''))}
4. Оплата: {get_answer_text('question_4', answers.get('question_4', ''))}
5. Готовність: {get_answer_text('question_5', answers.get('question_5', ''))}

=== НАСТУПНІ КРОКИ ===
1. Ми зв'яжемося з вами протягом 2 годин для уточнення деталей
2. Проведемо детальну консультацію
3. Підготуємо точне технічне завдання та фінальну ціну
4. Почнемо роботу над вашим проектом

З повагою,
Команда PrometeyLabs
Телефон: +380 XX XXX XX XX
Email: info@prometeylabs.com
"""
        
        # Відправляємо клієнту (якщо є email)
        if 'email' in test_data and test_data['email']:
            send_mail(
                subject=client_subject,
                message=client_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[test_data['email']],
                fail_silently=True,
            )
        
        # Email для команди
        admin_subject = f"[PrometeyLabs] Новий розрахунок проекту - {estimated_price} грн"
        admin_message = f"""
Новий розрахунок проекту

=== КОНТАКТ ===
Ім'я: {name}
Телефон: {phone}
Email: {test_data.get('email', 'Не вказано')}

=== РЕЗУЛЬТАТ ===
Розрахована вартість: {estimated_price} грн

=== ВІДПОВІДІ ===
{chr(10).join([f"{i+1}. {get_answer_text(f'question_{i+1}', answers.get(f'question_{i+1}', ''))}" for i in range(5)])}

Дата: {timezone.now().strftime('%d.%m.%Y %H:%M')}
"""
        
        send_mail(
            subject=admin_subject,
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        logger.info(f"Test result emails sent for {name}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send test result email: {e}")
        return False

def get_answer_text(question, answer):
    """Повертає текст відповіді на основі коду"""
    answers_map = {
        'question_1': {
            'A': 'Веб-сайт (лендінг, корпоративний сайт)',
            'B': 'Telegram бот',
            'C': 'Реклама (Google Ads, Facebook Ads)',
            'D': 'Інтернет-магазин',
            'E': 'Мобільний додаток'
        },
        'question_2': {
            'A': 'Форма на сайті',
            'B': 'Telegram бот',
            'C': 'WhatsApp/Вайбер',
            'D': 'Email',
            'E': 'Телефон'
        },
        'question_3': {
            'A': 'Терміново (3-7 днів)',
            'B': 'Стандартно (10-14 днів)',
            'C': 'Не поспішаємо (2-4 тижні)',
            'D': 'Гнучкий графік'
        },
        'question_4': {
            'A': 'Ні, тільки форма заявки',
            'B': 'Так, онлайн оплата картою',
            'C': 'Так, через термінал/касу',
            'D': 'Так, через криптовалюту',
            'E': 'Так, через розрахунковий рахунок'
        },
        'question_5': {
            'A': 'Тільки думки, потрібна консультація',
            'B': 'Є макети/дизайн',
            'C': 'Є технічне завдання',
            'D': 'Є логотип та брендинг',
            'E': 'Є соціальні мережі та контент'
        }
    }
    
    return answers_map.get(question, {}).get(answer, f'Невідома відповідь ({answer})')
