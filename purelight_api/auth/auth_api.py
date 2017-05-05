from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from purelight.models import Admin, Customer, Healer
from .auth_serializer import Admin_Serializer, Healer_serializer, Customer_serializer


class Admin_viewsets(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = Admin_Serializer

    @detail_route(methods=['post'])
    def create_admin_user(self, request, pk):
        user = self.get_object()



class Customer_viewsets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customer_serializer

class Healer_viewsets(viewsets.ModelViewSet):
    queryset = Healer.objects.all()
    serializer_class = Healer_serializer