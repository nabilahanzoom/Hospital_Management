from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]
class PatientModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12, default='')
    age = models.IntegerField()
    gender = models.CharField(max_length=30, choices=GENDER, default='Male')
    
    
    
    