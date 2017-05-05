from purelight import models
from rest_framework import serializers

class Admin_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = "__all__"

class User_serialzer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class User_role_serialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'

class Customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class Healer_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Healer
        fields = '__all__'

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

class Purcahses_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchasedetail
        fields = '__all__'

class Download_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Downloaddetail
        fields = '__all__'