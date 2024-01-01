from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone


# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
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