from rest_framework import serializers, viewsets, routers
from .models import User


# Serializers define the API document
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'age')