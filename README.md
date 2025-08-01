# PrometeyLabs - Веб-розробка та курси програмування

Сучасний Django проєкт з мінімалістичним дизайном та iOS Safari оптимізацією.

## 🎯 Особливості проєкту

- **6 сторінок**: Головна, Портфоліо, Калькулятор, Розробник, Блог, Контакти
- **Фонові відео**: Desktop та mobile версії для hero секцій
- **Card Stack ефект**: Інтерактивне портфоліо з z-index анімаціями
- **iOS Safari адаптація**: Повна оптимізація для iPhone
- **SEO оптимізація**: Структуровані дані та ключові слова
- **Модальні вікна**: Форми з валідацією та відправкою

## 🛠 Технології

- **Backend**: Django 4.2+, Python 3.9+
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Стилі**: Мінімалістичний дизайн згідно STYLE.MDC
- **Анімації**: CSS transitions + JavaScript
- **Відео**: MP4 з autoplay та fallback

## 📱 Адаптивність

- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px  
- **Mobile**: 320px - 767px
- **iOS Safari**: Спеціальні фікси для iPhone

## 🚀 Швидкий старт

### Встановлення

```bash
# Клонування репозиторію
git clone git@github.com:BonisOleg/prometeyRenova.git
cd prometeyRenova

# Створення віртуального середовища
python3 -m venv prometey_env
source prometey_env/bin/activate  # macOS/Linux
# prometey_env\Scripts\activate  # Windows

# Встановлення залежностей
pip install -r requirements.txt

# Міграції бази даних
python manage.py makemigrations
python manage.py migrate

# Створення суперкористувача
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

### Структура проєкту

```
PrometeyRenova/
├── apps/                    # Django додатки
│   ├── core/               # Основна логіка
│   ├── blog/               # Блог система
│   ├── forms/              # Форми та тест
│   └── portfolio/          # Портфоліо проєкти
├── static/                 # Статичні файли
│   ├── css/               # Стилі
│   ├── js/                # JavaScript
│   ├── videos/            # Відео файли
│   └── images/            # Зображення
├── templates/              # HTML шаблони
│   ├── components/        # Компоненти
│   └── pages/            # Сторінки
├── prometey_project/      # Налаштування Django
└── requirements.txt       # Залежності Python
```

## 🎨 Дизайн система

### Кольори
- **Червоний акцент**: #DC143C
- **Чорний текст**: #000000  
- **Білий фон**: #FFFFFF
- **Бежевий фон**: #F5F1ED

### Типографіка
- **Мега-заголовки**: 120-160px
- **Великі заголовки**: 80-100px
- **Середні заголовки**: 24-32px
- **Основний текст**: 14-16px

## 📄 Сторінки

### 1. Головна (/)
- Hero з фоновим відео
- 3 CTA кнопки з модальними вікнами
- SEO блок послуг (100% ширини)

### 2. Портфоліо (/portfolio/)
- Card Stack ефект з 6 проектами
- Фонові відео для кожного проекту
- Технології та опис робіт

### 3. Калькулятор (/calculator/)
- Тест з 5 питань
- Розрахунок вартості проєкту
- Форма з результатом

### 4. Розробник (/developer/)
- Темна сторінка 50/50 розподіл
- Опис курсів програмування
- Форма запису на курси

### 5. Блог (/blog/)
- Статті для SEO просування
- Пагінація та категорії
- Ключові слова для Google

### 6. Контакти (/contacts/)
- Соцмережі та контакти
- Форма зворотного зв'язку
- Карта та адреса

## 🔧 Функціонал

### Модальні вікна
- "Стати розробником" - форма запису на курси
- "Заявка на сайт" - форма розрахунку вартості
- "Результат тесту" - показ розрахунку
- "Дякуємо" - підтвердження відправки

### Тест калькулятора
1. Тип проєкту (сайт/бот/реклама/магазин/додаток)
2. Куди заявки (форма/telegram/whatsapp/email/телефон)
3. Терміни (3-7 днів/10-14/2-4 тижні/гнучко)
4. Оплата (ні/картка/термінал/крипто/розрахунок)
5. Готовність (думки/макети/ТЗ/логотип/контент)

## 📱 iOS Safari оптимізація

- `-webkit-fill-available` для viewport height
- `env(safe-area-inset-*)` для safe areas
- `-webkit-overflow-scrolling: touch` для скролу
- `-webkit-backdrop-filter` для blur ефектів
- Оптимізація відео для мобільних пристроїв

## 🚀 Деплой

### Локальний розвиток
```bash
python manage.py runserver
```

### Продакшн
```bash
python manage.py collectstatic
python manage.py migrate
gunicorn prometey_project.wsgi:application
```

## 📊 SEO

- Мета теги для кожної сторінки
- Структуровані дані Schema.org
- Оптимізовані зображення та відео
- Sitemap та robots.txt
- Google Analytics інтеграція

## 🤝 Розвиток

### Гілки
- `main` - стабільна версія
- `develop` - розробка нових функцій
- `feature/*` - окремі функції

### Коміти
- `feat:` - нові функції
- `fix:` - виправлення помилок
- `style:` - зміни стилів
- `docs:` - документація

## 📞 Контакти

- **Telegram**: [@prometeylabs](https://t.me/prometeylabs)
- **Email**: info@prometeylabs.com
- **GitHub**: [BonisOleg/prometeyRenova](https://github.com/BonisOleg/prometeyRenova)

## 📄 Ліцензія

MIT License - дивіться файл LICENSE для деталей.

---

**PrometeyLabs** - Сучасні веб-рішення та курси програмування 🚀 