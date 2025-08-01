from django.db import models

# Create your models here.
class DesignationModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    designation = models.ManyToManyField(DesignationModel)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

