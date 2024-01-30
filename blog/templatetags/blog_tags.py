from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone


register = template.Library()


@register.inclusion_tag('latest_posts.html')
def latest_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {'posts': posts}


@register.simple_tag(name='totalposts')
def function():
    posts=Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts=Post.objects.filter(status=1)
    return posts


@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts =Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.simple_tag
def post_title(posts):
    posts=Post.objects.all()
    titles=posts
    return {'titles':titles}

@register.inclusion_tag('website/index.html')
def latest_posts():
    posts = Post.objects.order_by('-published_date')[:6]
    return {'posts': posts}

@register.simple_tag
def post_title():
    posts = Post.objects.order_by('-published_date')[:6]
    return posts

@register.simple_tag
def post_category(post):
    return post.Category  

@register.simple_tag
def post_content(post):
    return post.content[:200] + "..."

@register.simple_tag
def post_img(post):
    return post.image.url 

@register.simple_tag
def hello ():
    return 'hello'

@register.inclusion_tag('website/popular-posts.html')
def latest_posts_index():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {'posts': posts}