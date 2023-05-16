from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from credits.models import Credit
from deposits.models import Deposit


class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    card = models.ForeignKey('Card', on_delete=models.SET_NULL, null=True)
    deposit = models.ForeignKey(Deposit, on_delete=models.SET_NULL, null=True, blank=True)
    credit = models.ForeignKey(Credit, on_delete=models.SET_NULL, null=True, blank=True)

    # def __str__(self):
    #     return self.name
    #
    # class Meta:
    #     ordering = ['name']


class Card(models.Model):
    number = models.PositiveBigIntegerField()
    cvv = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    balance = models.FloatField(default=0)

    def __str__(self):
        return f'{self.number}'
