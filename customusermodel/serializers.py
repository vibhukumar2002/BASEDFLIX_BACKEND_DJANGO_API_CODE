from rest_framework.serializers import ModelSerializer
from . import models

class customuserserializer(ModelSerializer):
    class Meta:
        model=models.customuser
        fields=['id','firstname']

class userbyidserializer(ModelSerializer):
    class Meta:
        model=models.customuser
        fields='__all__'