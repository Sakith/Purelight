from purelight import models
from rest_framework import serializers
from rest_framework.generics import ListAPIView


class Media_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Media
        fields = '__all__'

class Track_srializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = '__all__'

class Offers_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offers
        fields = '__all__'
