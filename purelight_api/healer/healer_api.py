from healer_serializer import *
from rest_framework import viewsets
from purelight.models import *
import django_filters.rest_framework
from rest_framework import generics


class Media_viewsets(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = Media_serializer


class Track_viewsets(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = Track_srializer


class Offers_viewsets(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = Offers_serializer