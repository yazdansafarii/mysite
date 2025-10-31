from django import template

register = template.Library()
from blog.models import post


@register.inclusion_tag('blog/popular-posts-blog.html')

def popular_posts():
    posts = post.objects.order_by('counted_view')
    return {'posts':posts}