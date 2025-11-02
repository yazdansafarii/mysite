from django.shortcuts import render , get_object_or_404
from blog.models import post
# Create your views here.


def blog_view(request):
    posts = post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
    


def blog_single(request,pid):
    posts = post.objects.filter(status=1)
    posts = get_object_or_404(post,pk=pid)
    context = {'posts':posts}
    return render(request,'blog/blog-single.html',context)


def blog_cat(request,cat_name):
    posts = post.objects.filter(status=1)
    posts = post.objects.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
