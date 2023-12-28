from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.db.models import F

from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now())

    # for posts in Post.objects.all():
    #     Post.counted_views  =+1
    # return render(request, 'blog/post_detail.html', {'post': post})
    # posts=Post.objects.filter(status=0)
    # posts=Post.objects.filter(published_date=datetime.date(2023,12,24))
    # start_date = datetime.date(2005, 1, 1)
    # end_date = datetime.date(2022, 12, 27)
    # pub_d=Post.objects.filter(published_date=(start_date,end_date))
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    posts=Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now())
    post = get_object_or_404(posts,pk=pid)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)
def test(request,pid):
    # post=Post.objects.get(id=pid)
    # posts=Post.objects.all()
    # posts=Post.objects.filter(status=0)
    post = get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)