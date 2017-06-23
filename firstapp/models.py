from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

# If you want implement model changes to db, use: python manage.py migrate app
# If you want to store model's change, use: python manage.py makemigrations app
# If you want to view detail of one stored migration, use: python manage.py sqlmigrate app 000x
# If you want to implement one stored migration, use: python manage.py migrate app 000x

# To enter an django shell, use: python manage.py shell

@python_2_unicode_compatible
class Country(models.Model):
    # id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class User(models.Model):
    # id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, null=True)

    def __str__(self):
        return "%d:%s" % (self.pk, self.name)
