from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    if kwargs.get('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name')!=None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
        

    posts=Paginator(posts,2)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage :
        posts=posts.get_page(1)

    
    # return render(request, 'blog/post_detail.html', {'post': post})
    # posts=Post.objects.filter(status=0)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    previous_post = Post.objects.filter(id__lt=pid,status=1,published_date__lte=timezone.now()).order_by('-id').first()
    # if previous_post:
    #     return True
    # if next_post:6
    #     return True
    next_post = Post.objects.filter(id__gt=pid,status=1,published_date__lte=timezone.now()).order_by('id').first()
    context={'post':post,
             'previous_post': previous_post,
             'next_post': next_post}
    return render(request,'blog/blog-single.html',context)
def test(request):
    # post=Post.objects.get(id=pid)
    # posts=Post.objects.all()
    # posts=Post.objects.filter(status=0)
    # post = get_object_or_404(Post,pk=pid)
    # context={'post':post}
    return render(request,'test.html')


def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())

    # print(request.__dict__)
    if request.method=='GET':
        # print(request.GET.get('s'))
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    #     print('get request')
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)