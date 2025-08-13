from django.core.management.base import BaseCommand
from apps.blog.models import BlogPost

class Command(BaseCommand):
    def handle(self, *args, **options):
        title = 'CSS-in-JS: Стилі в JavaScript компонентах'
        content = '<p>Повний цікавий текст для цієї статті...</p>'
        post = BlogPost.objects.get(title=title)
        post.content += content
        post.save()
        self.stdout.write(self.style.SUCCESS('Оновлено статтю!'))
