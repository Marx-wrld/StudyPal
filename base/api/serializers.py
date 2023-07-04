#serializers are classes that take a certain model/object that we want to serialize and turn it into json data

from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta: 
        #meta is a class that defines behaviour of certain classes and their instances and contains metadata used to change the behaviour of model fields
        model = Room
        fields = '__all__'