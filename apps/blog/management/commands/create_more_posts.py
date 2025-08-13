from django.core.management.base import BaseCommand
from apps.blog.models import BlogPost


class Command(BaseCommand):
    help = 'Створює додаткові статті для блогу'

    def handle(self, *args, **options):
        articles_data = [
            {
                'title': 'React vs Vue: Який фреймворк обрати в 2024?',
                'excerpt': 'Детальне порівняння React та Vue.js. Переваги та недоліки кожного фреймворку для веб-розробки.',
                'content': '<h2>Вступ</h2><p>React та Vue - два найпопулярніші JavaScript фреймворки. Який обрати для вашого проекту?</p><h2>React</h2><p>Створений Facebook, має велику спільноту та багато бібліотек.</p><h2>Vue</h2><p>Простий у вивченні, гнучкий та швидкий.</p>',
                'seo_title': 'React vs Vue 2024 - Порівняння фреймворків',
                'seo_description': 'Порівняння React та Vue.js 2024. Який фреймворк обрати для веб-розробки?',
                'keywords': 'react vs vue, react, vue.js, javascript фреймворки, веб-розробка',
                'category': 'web-development',
                'reading_time': 6
            },
            {
                'title': 'Django REST Framework: Створення API за 30 хвилин',
                'excerpt': 'Швидкий старт з Django REST Framework. Створюйте потужні API для ваших веб-додатків.',
                'content': '<h2>Що таке DRF?</h2><p>Django REST Framework - це потужний інструмент для створення API.</p><h2>Швидкий старт</h2><p>Встановлення та налаштування за 5 хвилин.</p>',
                'seo_title': 'Django REST Framework API за 30 хвилин',
                'seo_description': 'Створення API з Django REST Framework. Швидкий старт та практичні приклади.',
                'keywords': 'django rest framework, api, python, django',
                'category': 'courses',
                'reading_time': 5
            },
            {
                'title': 'Git для початківців: Основи системи контролю версій',
                'excerpt': 'Вивчіть основи Git з нуля. Команди, гілки, merge та робота з GitHub.',
                'content': '<h2>Що таке Git?</h2><p>Git - це система контролю версій для розробників.</p><h2>Основні команди</h2><p>git init, git add, git commit, git push.</p>',
                'seo_title': 'Git для початківців - Основи контролю версій',
                'seo_description': 'Вивчення Git з нуля. Команди, гілки та робота з GitHub для початківців.',
                'keywords': 'git, github, контролю версій, початківці',
                'category': 'courses',
                'reading_time': 7
            },
            {
                'title': 'CSS Grid vs Flexbox: Коли що використовувати?',
                'excerpt': 'Порівняння CSS Grid та Flexbox. Практичні приклади та рекомендації по вибору.',
                'content': '<h2>CSS Grid</h2><p>Двовимірна система для складних макетів.</p><h2>Flexbox</h2><p>Одновимірна система для гнучких компонентів.</p>',
                'seo_title': 'CSS Grid vs Flexbox - Коли що використовувати',
                'seo_description': 'Порівняння CSS Grid та Flexbox. Практичні приклади та рекомендації.',
                'keywords': 'css grid, flexbox, css, макети, веб-дизайн',
                'category': 'web-development',
                'reading_time': 8
            },
            {
                'title': 'Python для аналізу даних: Pandas та NumPy',
                'excerpt': 'Основи аналізу даних з Python. Робота з Pandas, NumPy та створення графіків.',
                'content': '<h2>Pandas</h2><p>Бібліотека для аналізу та обробки даних.</p><h2>NumPy</h2><p>Числові обчислення та масиви.</p>',
                'seo_title': 'Python аналіз даних - Pandas та NumPy',
                'seo_description': 'Аналіз даних з Python. Pandas, NumPy та створення графіків.',
                'keywords': 'python, pandas, numpy, аналіз даних',
                'category': 'courses',
                'reading_time': 9
            },
            {
                'title': 'Веб-безпека: Захист від XSS та SQL ін\'єкцій',
                'excerpt': 'Основні загрози веб-безпеки та способи захисту. XSS, SQL ін\'єкції та CSRF атаки.',
                'content': '<h2>XSS атаки</h2><p>Cross-site scripting та способи захисту.</p><h2>SQL ін\'єкції</h2><p>Захист баз даних від зловмисних запитів.</p>',
                'seo_title': 'Веб-безпека - Захист від XSS та SQL ін\'єкцій',
                'seo_description': 'Захист веб-додатків від XSS, SQL ін\'єкцій та CSRF атак.',
                'keywords': 'веб-безпека, xss, sql ін\'єкції, csrf, захист',
                'category': 'web-development',
                'reading_time': 10
            },
            {
                'title': 'Docker для розробників: Контейнеризація додатків',
                'excerpt': 'Вивчіть Docker з нуля. Створення контейнерів, Dockerfile та Docker Compose.',
                'content': '<h2>Що таке Docker?</h2><p>Платформа для контейнеризації додатків.</p><h2>Dockerfile</h2><p>Створення власних образів.</p>',
                'seo_title': 'Docker для розробників - Контейнеризація',
                'seo_description': 'Вивчення Docker. Контейнери, Dockerfile та Docker Compose.',
                'keywords': 'docker, контейнери, devops, розробка',
                'category': 'technology',
                'reading_time': 8
            },
            {
                'title': 'JavaScript ES6+: Сучасні можливості мови',
                'excerpt': 'Нові можливості JavaScript ES6+. Arrow functions, destructuring, modules та async/await.',
                'content': '<h2>Arrow Functions</h2><p>Скорочений синтаксис для функцій.</p><h2>Destructuring</h2><p>Розпакування об\'єктів та масивів.</p>',
                'seo_title': 'JavaScript ES6+ - Сучасні можливості',
                'seo_description': 'Нові можливості JavaScript ES6+. Arrow functions, destructuring, modules.',
                'keywords': 'javascript, es6, es7, es8, сучасний js',
                'category': 'courses',
                'reading_time': 7
            },
            {
                'title': 'Node.js сервер: Створення REST API',
                'excerpt': 'Створення серверу на Node.js. Express.js, MongoDB та JWT аутентифікація.',
                'content': '<h2>Express.js</h2><p>Веб-фреймворк для Node.js.</p><h2>MongoDB</h2><p>NoSQL база даних для Node.js.</p>',
                'seo_title': 'Node.js сервер - REST API з Express',
                'seo_description': 'Створення серверу на Node.js. Express.js, MongoDB та JWT.',
                'keywords': 'node.js, express, mongodb, rest api',
                'category': 'web-development',
                'reading_time': 9
            },
            {
                'title': 'TypeScript: Типізований JavaScript',
                'excerpt': 'Введення в TypeScript. Типи, інтерфейси та переваги типізації.',
                'content': '<h2>Що таке TypeScript?</h2><p>Надмножина JavaScript з типізацією.</p><h2>Типи</h2><p>Базові типи та інтерфейси.</p>',
                'seo_title': 'TypeScript - Типізований JavaScript',
                'seo_description': 'Введення в TypeScript. Типи, інтерфейси та переваги.',
                'keywords': 'typescript, javascript, типи, інтерфейси',
                'category': 'courses',
                'reading_time': 6
            },
            {
                'title': 'GraphQL vs REST: Нова ера API',
                'excerpt': 'Порівняння GraphQL та REST API. Переваги та недоліки кожного підходу.',
                'content': '<h2>REST API</h2><p>Традиційний підхід до створення API.</p><h2>GraphQL</h2><p>Сучасний підхід з гнучкими запитами.</p>',
                'seo_title': 'GraphQL vs REST - Нова ера API',
                'seo_description': 'Порівняння GraphQL та REST API. Переваги та недоліки.',
                'keywords': 'graphql, rest api, api, веб-розробка',
                'category': 'web-development',
                'reading_time': 8
            },
            {
                'title': 'Python веб-скрапінг: Beautiful Soup та Scrapy',
                'excerpt': 'Автоматизація збору даних з веб-сайтів. Beautiful Soup, Scrapy та етика скрапінгу.',
                'content': '<h2>Beautiful Soup</h2><p>Бібліотека для парсингу HTML.</p><h2>Scrapy</h2><p>Потужний фреймворк для скрапінгу.</p>',
                'seo_title': 'Python веб-скрапінг - Beautiful Soup та Scrapy',
                'seo_description': 'Веб-скрапінг з Python. Beautiful Soup, Scrapy та етика.',
                'keywords': 'python, веб-скрапінг, beautiful soup, scrapy',
                'category': 'technology',
                'reading_time': 7
            },
            {
                'title': 'React Hooks: Сучасний React без класів',
                'excerpt': 'Вивчення React Hooks. useState, useEffect, useContext та створення власних хуків.',
                'content': '<h2>useState</h2><p>Хук для управління станом компонента.</p><h2>useEffect</h2><p>Хук для побічних ефектів.</p>',
                'seo_title': 'React Hooks - Сучасний React без класів',
                'seo_description': 'React Hooks. useState, useEffect, useContext та власні хуки.',
                'keywords': 'react hooks, react, функціональні компоненти',
                'category': 'web-development',
                'reading_time': 8
            },
            {
                'title': 'Django ORM: Робота з базами даних',
                'excerpt': 'Потужний ORM Django. Моделі, запити, міграції та оптимізація.',
                'content': '<h2>Моделі Django</h2><p>Створення та налаштування моделей.</p><h2>Запити</h2><p>ORM запити та фільтрація.</p>',
                'seo_title': 'Django ORM - Робота з базами даних',
                'seo_description': 'Django ORM. Моделі, запити, міграції та оптимізація.',
                'keywords': 'django orm, django, бази даних, моделі',
                'category': 'courses',
                'reading_time': 9
            },
            {
                'title': 'CSS анімації: Анімація без JavaScript',
                'excerpt': 'Створення анімацій тільки CSS. Transitions, animations та keyframes.',
                'content': '<h2>CSS Transitions</h2><p>Плавні переходи між станами.</p><h2>CSS Animations</h2><p>Складні анімації з keyframes.</p>',
                'seo_title': 'CSS анімації - Анімація без JavaScript',
                'seo_description': 'CSS анімації. Transitions, animations та keyframes.',
                'keywords': 'css анімації, transitions, animations, keyframes',
                'category': 'web-development',
                'reading_time': 6
            },
            {
                'title': 'Python тестування: Unit тести з pytest',
                'excerpt': 'Написання тестів для Python коду. pytest, fixtures та покриття коду.',
                'content': '<h2>pytest</h2><p>Сучасний фреймворк для тестування.</p><h2>Fixtures</h2><p>Перевикористання тестових даних.</p>',
                'seo_title': 'Python тестування - Unit тести з pytest',
                'seo_description': 'Тестування Python коду. pytest, fixtures та покриття.',
                'keywords': 'python, тестування, pytest, unit тести',
                'category': 'courses',
                'reading_time': 7
            },
            {
                'title': 'Веб-швидкість: Оптимізація завантаження',
                'excerpt': 'Техніки оптимізації швидкості веб-сайтів. Lazy loading, кешування та компресія.',
                'content': '<h2>Lazy Loading</h2><p>Відкладення завантаження зображень.</p><h2>Кешування</h2><p>Зберігання ресурсів локально.</p>',
                'seo_title': 'Веб-швидкість - Оптимізація завантаження',
                'seo_description': 'Оптимізація швидкості сайтів. Lazy loading, кешування.',
                'keywords': 'веб-швидкість, оптимізація, lazy loading, кешування',
                'category': 'web-development',
                'reading_time': 8
            },
            {
                'title': 'Git Workflow: Ефективна робота в команді',
                'excerpt': 'Gitflow, GitHub Flow та найкращі практики роботи з Git в команді.',
                'content': '<h2>Gitflow</h2><p>Модель роботи з гілками для команд.</p><h2>GitHub Flow</h2><p>Спрощена модель для швидкої розробки.</p>',
                'seo_title': 'Git Workflow - Ефективна робота в команді',
                'seo_description': 'Git workflow. Gitflow, GitHub Flow та практики.',
                'keywords': 'git workflow, gitflow, github flow, командна робота',
                'category': 'technology',
                'reading_time': 9
            },
            {
                'title': 'Python Flask: Мікрофреймворк для веб-додатків',
                'excerpt': 'Створення веб-додатків з Flask. Роути, шаблони та розширення.',
                'content': '<h2>Flask</h2><p>Легкий Python веб-фреймворк.</p><h2>Роути</h2><p>Налаштування URL та обробники.</p>',
                'seo_title': 'Python Flask - Мікрофреймворк для веб-додатків',
                'seo_description': 'Flask веб-додатки. Роути, шаблони та розширення.',
                'keywords': 'python flask, flask, веб-фреймворк, python',
                'category': 'web-development',
                'reading_time': 7
            }
        ]

        created_count = 0
        for article_data in articles_data:
            # Перевіряємо чи існує стаття з таким slug
            slug = article_data['title'].lower().replace(' ', '-').replace(':', '').replace(',', '').replace('(', '').replace(')', '').replace('\'', '').replace('+', '')
            if not BlogPost.objects.filter(slug=slug).exists():
                post = BlogPost.objects.create(
                    title=article_data['title'],
                    slug=slug,
                    excerpt=article_data['excerpt'],
                    content=article_data['content'],
                    seo_title=article_data['seo_title'],
                    seo_description=article_data['seo_description'],
                    keywords=article_data['keywords'],
                    category=article_data['category'],
                    reading_time=article_data['reading_time'],
                    is_published=True
                )
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Створено статтю: {post.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Стаття вже існує: {article_data["title"]}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Успішно створено {created_count} нових статей')
        )
