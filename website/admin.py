from django.contrib import admin
from pyexpat.errors import messages

# Register your models here.
from website.models import contact
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    search_fields = ['name','message']
    list_filter = ('email',)
    list_display = ('name', 'email', )

admin.site.register(contact, ContactAdmin)

