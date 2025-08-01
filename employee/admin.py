from django.contrib import admin
from .models import EmployeeModel, DesignationModel
# Register your models here.

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(DesignationModel, DesignationAdmin)
admin.site.register(EmployeeModel)