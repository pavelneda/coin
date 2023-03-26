# Generated by Django 4.1.7 on 2023-03-26 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=300)),
                ('total', models.FloatField()),
                ('term', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(24)])),
                ('percent', models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(30)])),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
