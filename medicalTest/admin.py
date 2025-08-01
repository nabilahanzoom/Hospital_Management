from django.contrib import admin
from .models import CategoryModel, MedicalTestModel, PatientTestModel
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(MedicalTestModel)
admin.site.register(PatientTestModel)