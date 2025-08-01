from django.db import models
from doctor.models import DoctorModel
from patient.models import PatientModel
# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class MedicalTestModel(models.Model):
    name = models.CharField(max_length=200)
    Type = models.ManyToManyField(CategoryModel)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
   

TEST_STATUS = [
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]
class PatientTestModel(models.Model):
    test = models.ForeignKey(MedicalTestModel, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    test_status = models.CharField(max_length=30, choices=TEST_STATUS, default='Pending')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.test.name} - {self.test_status}"

