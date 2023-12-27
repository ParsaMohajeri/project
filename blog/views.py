from django.shortcuts import render,get_object_or_404
from blog.models import Post
import datetime
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1)
    posts = Post.objects.filter(published_date__lte=timezone.now())
    # posts=Post.objects.filter(status=0)
    # posts=Post.objects.filter(published_date=datetime.date(2023,12,24))
    # start_date = datetime.date(2005, 1, 1)
    # end_date = datetime.date(2022, 12, 27)
    # pub_d=Post.objects.filter(published_date=(start_date,end_date))
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request):
    return render(request,'blog/blog-single.html')
def test(request,pid):
    # post=Post.objects.get(id=pid)
    # posts=Post.objects.all()
    # posts=Post.objects.filter(status=0)
    post = get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)