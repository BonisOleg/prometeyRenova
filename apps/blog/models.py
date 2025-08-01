from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    excerpt = models.TextField(max_length=300, verbose_name="Короткий опис")
    content = models.TextField(verbose_name="Контент")
    seo_title = models.CharField(max_length=70, verbose_name="SEO заголовок")
    seo_description = models.CharField(max_length=160, verbose_name="SEO опис")
    keywords = models.CharField(max_length=255, verbose_name="Ключові слова")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Стаття блогу"
        verbose_name_plural = "Статті блогу"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
