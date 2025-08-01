from django.contrib import admin
from .models import MedicinelistModel, BuyMedicineModel
# Register your models here.

admin.site.register(MedicinelistModel)
admin.site.register(BuyMedicineModel)