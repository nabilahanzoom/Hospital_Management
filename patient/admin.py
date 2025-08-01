from django.contrib import admin
from .models import PatientModel
# Register your models here.

# display data in a table formate
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mobile_no', 'age', 'gender']

    # Get Relational fields data (forignkey, onetoonefield, manytomany fields)
    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name
    
    def email(self, obj):
        return obj.user.email

admin.site.register(PatientModel, PatientAdmin)