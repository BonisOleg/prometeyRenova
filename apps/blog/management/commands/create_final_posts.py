from django.core.management.base import BaseCommand
from apps.blog.models import BlogPost


class Command(BaseCommand):
    help = 'Створює фінальні статті для блогу'

    def handle(self, *args, **options):
        articles_data = [
            {
                'title': 'Svelte: Новий підхід до веб-розробки',
                'excerpt': 'Svelte - революційний фреймворк, який компілюється в vanilla JavaScript. Швидкість та простота.',
                'content': '<h2>Що таке Svelte?</h2><p>Svelte - це компілятор, який створює високопродуктивний JavaScript код.</p><h2>Переваги</h2><p>Менший bundle size та краща продуктивність.</p>',
                'seo_title': 'Svelte - Новий підхід до веб-розробки',
                'seo_description': 'Svelte фреймворк. Компіляція в JavaScript та висока продуктивність.',
                'keywords': 'svelte, фреймворк, веб-розробка, javascript',
                'category': 'web-development',
                'reading_time': 6
            },
            {
                'title': 'Python FastAPI: Швидкий веб-фреймворк',
                'excerpt': 'FastAPI - сучасний Python фреймворк для створення API. Автоматична документація та валідація.',
                'content': '<h2>FastAPI</h2><p>Сучасний веб-фреймворк з автоматичною документацією.</p><h2>Переваги</h2><p>Швидкість, автоматична валідація та OpenAPI.</p>',
                'seo_title': 'Python FastAPI - Швидкий веб-фреймворк',
                'seo_description': 'FastAPI Python фреймворк. Автоматична документація та валідація.',
                'keywords': 'python fastapi, fastapi, веб-фреймворк, api',
                'category': 'web-development',
                'reading_time': 7
            },
            {
                'title': 'CSS-in-JS: Стилі в JavaScript компонентах',
                'excerpt': 'Styled-components, Emotion та інші CSS-in-JS рішення. Переваги та недоліки підходу.',
                'content': '<h2>Styled-components</h2><p>CSS-in-JS бібліотека для React компонентів.</p><h2>Переваги</h2><p>Динамічні стилі та компонентний підхід.</p>',
                'seo_title': 'CSS-in-JS - Стилі в JavaScript компонентах',
                'seo_description': 'CSS-in-JS рішення. Styled-components, Emotion та переваги.',
                'keywords': 'css-in-js, styled-components, emotion, react',
                'category': 'web-development',
                'reading_time': 6
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
