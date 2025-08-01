from django.contrib import admin
from .models import ContactUsModel
# Register your models here.

# we can show data, tabular format in admin panal. Use this pice of code.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']

admin.site.register(ContactUsModel, ContactUsAdmin)