from django.db import models

# Create your models here.
class Department(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    build_number = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")



    class Meta:
        ordering = ['number']


