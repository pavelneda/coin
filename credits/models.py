from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Credit(models.Model):
    purpose = models.CharField(max_length=300)
    total = models.FloatField()
    term = models.IntegerField(default=3, validators=[MinValueValidator(3), MaxValueValidator(24)])
    percent = models.IntegerField(default=15, validators=[MinValueValidator(10), MaxValueValidator(30)])
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purpose

    class Meta:
        ordering = ['data', 'purpose']

