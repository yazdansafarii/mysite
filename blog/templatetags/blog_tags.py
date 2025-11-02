from django import template

register = template.Library()
from blog.models import post
from blog.models import category


@register.inclusion_tag('blog/popular-posts-blog.html')

def popular_posts():
    posts = post.objects.order_by('counted_view')
    return {'posts':posts}


@register.inclusion_tag('blog/post-catgory-blog.html')

def Category():
    posts = post.objects.filter(status=1)
    categorys = category.objects.all()
    cat_dic = {}
    for name in categorys:
        cat_dic[name]=posts.filter(category=name).count()
    return{'categorys':cat_dic}
