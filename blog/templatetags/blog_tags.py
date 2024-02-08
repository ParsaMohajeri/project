from django import template
from blog.models import Post,Comment
from blog.models import Category
from django.utils import timezone


register = template.Library()





@register.simple_tag(name='totalposts')
def function():
    posts=Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='comments_count')
def commnets_count(pid):
    return Comment.objects.filter(post=pid,approved=True).count()


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



@register.inclusion_tag('website/popular-posts.html')
def latest_posts_index():
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return {'posts': posts}