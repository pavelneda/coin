# Generated by Django 4.1.7 on 2023-03-27 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["data", "title"]},
        ),
    ]
