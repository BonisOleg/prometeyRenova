from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost


def blog_list(request):
    """Список статей блогу з пагінацією"""
    posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(posts, 6)  # 6 статей на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'page_title': 'Блог про веб-розробку | PrometeyLabs',
        'meta_description': 'Корисні статті про розробку сайтів, Telegram ботів, Python, Django, React. Поради від досвідчених розробників PrometeyLabs.',
        'og_title': 'Блог PrometeyLabs - Все про веб-розробку',
        'keywords': 'блог веб розробка, курси програмування, сайти під ключ, telegram боти, Python Django, React розробка',
    }
    return render(request, 'pages/blog.html', context)


def blog_detail(request, slug):
    """Детальна сторінка статті"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    context = {
        'post': post,
        'page_title': post.seo_title or post.title,
        'meta_description': post.seo_description,
        'og_title': post.title,
        'keywords': post.keywords,
    }
    return render(request, 'pages/blog_detail.html', context)
