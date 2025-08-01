from django.db import models
from doctor.models import DoctorModel
from patient.models import PatientModel
# Create your models here.
class MedicinelistModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class BuyMedicineModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)