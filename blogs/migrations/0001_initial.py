# Generated by Django 4.1.7 on 2023-05-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('text', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['data', 'title'],
            },
        ),
    ]
