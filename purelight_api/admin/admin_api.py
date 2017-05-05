from rest_framework import viewsets
from purelight.models import *
from purelight_api.admin.admin_serializer import *


class Admin_viewsets(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = Admin_serializer


class User_viewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serialzer
     

class User_role_viewsets(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = User_role_serialzer
     

class Customer_viewsets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customer_serializer
     

class Healer_viewsets(viewsets.ModelViewSet):
    queryset = Healer.objects.all()
    serializer_class = Healer_serializer
     

class Media_viewsets(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = Media_serializer
     

class Track_viewsets(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = Track_srializer
     

class Offers_viewsets(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = Offers_serializer
     

class Purcahses_viewsets(viewsets.ModelViewSet):
    queryset = Purchasedetail.objects.all()
    serializer_class = Purcahses_serializer
     

class Download_viewsets(viewsets.ModelViewSet):
    queryset = Downloaddetail.objects.all()
    serializer_class = Download_serializer
     