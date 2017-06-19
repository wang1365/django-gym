from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Country(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)


class User(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=512)

