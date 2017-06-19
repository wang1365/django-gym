from __future__ import unicode_literals

from django.db import models


# Create your models here.

# If you want implement model changes to db, use: python manage.py migrate app
# If you want to store model's change, use: python manage.py makemigrations app
# If you want to view detail of one stored migration, use: python manage.py sqlmigrate app 000x
# If you want to implement one stored migration, use: python manage.py migrate app 000x

class Country(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)


class User(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, null=True)

