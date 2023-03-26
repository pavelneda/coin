from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
