from rest_framework.serializers import ModelSerializer
from .models import room,topic,message,reply,favs
from .forms import roomform

class roomserializer(ModelSerializer):
    class Meta:
        model=room
        # fields=['id','name','topic','host','ceated','updated']
        fields='__all__'

class topicserializer(ModelSerializer):
    class Meta:
        model=topic
        fields='__all__'

class roomformserializer(ModelSerializer):
    class Meta:
        model=roomform
        fields='__all__'

class messageserializer(ModelSerializer):
    class Meta:
        model=message
        fields='__all__'

class replyserializer(ModelSerializer):
    class Meta:
        model=reply
        fields='__all__'

class favsserializer(ModelSerializer):
    class Meta:
        model=favs
        fields='__all__'

