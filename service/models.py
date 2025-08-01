from django.db import models

# Create your models here.

class ServiceModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # When i fill this image fields, img are save in the images folder in service app.
    image = models.ImageField(upload_to='service/images/')

    def __str__(self):
        return self.name
    