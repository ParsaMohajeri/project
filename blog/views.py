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
def blog_single(request,pid,post_id):
    post = get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    # if piod>=pid:
    current_post = Post.objects.get(id=post_id)
    previous_post = Post.objects.filter(id__lt=post_id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post_id).order_by('id').first()
    context={'post':post,'current_post': current_post,'next_post': next_post,'previous_post': previous_post}
    return render(request,'blog/blog-single.html',context)
def test(request,pid):
    # post=Post.objects.get(id=pid)
    # posts=Post.objects.all()
    # posts=Post.objects.filter(status=0)
    post = get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)