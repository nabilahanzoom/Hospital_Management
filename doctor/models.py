from django.db import models
from django.contrib.auth.models import User
from patient.models import PatientModel
# Create your models here.

class SpecializationModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
 
class DesignationModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class AvailableTimeModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class DoctorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/', blank = True,null = True)
    designation = models.ManyToManyField(DesignationModel)
    specialization = models.ManyToManyField(SpecializationModel)
    available_time = models.ManyToManyField(AvailableTimeModel)
    fee = models.IntegerField()
    
    qualification = models.CharField(max_length=100, default='')
    meet_link = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

STAR_CHOICE = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class ReviewModel(models.Model):
    reviewer = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    ratting = models.CharField(max_length=100, choices = STAR_CHOICE)


    def __str__(self):
        return f"{self.reviewer.user.first_name} to {self.doctor.user.first_name}"
    