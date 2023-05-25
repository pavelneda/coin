from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)



class Card(models.Model):
    number = models.PositiveBigIntegerField(unique=True)
    cvv = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    balance = models.FloatField(default=0)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'{self.number}'
