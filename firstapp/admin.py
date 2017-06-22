from django.contrib import admin
from .models import Country, User

# Register your models here.

admin.site.register((Country, User))
