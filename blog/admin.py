from django.contrib import admin

# Register your models here.

from blog.models import post

class postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author','published_date' , 'status', 'created_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')


admin.site.register(post,postadmin)