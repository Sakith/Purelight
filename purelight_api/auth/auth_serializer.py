from rest_framework import serializers
from purelight import models

class Customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class Healer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Healer
        fields = '__all__'

class Admin_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields ="__all__"