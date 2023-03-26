from django.db import models
from deposits.models import Deposit
from credits.models import Credit

# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    card = models.ForeignKey('Card', on_delete=models.SET_NULL, null=True)
    deposit = models.ForeignKey(Deposit, on_delete=models.SET_NULL, null=True)
    credit = models.ForeignKey(Credit, on_delete=models.SET_NULL, null=True)


class Card(models.Model):
    number = models.PositiveBigIntegerField()
    cvv = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    balance = models.FloatField(default=0)