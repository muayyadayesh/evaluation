from rest_framework import viewsets
from .models import Company, Client
from .serializers import CompanySerializer, ClientSerializer
from django.http import Http404
from rest_framework.response import Response

# The CompanyViewSet class defines a viewset for handling Company objects in a Django REST framework
# API.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise Http404("No companies found")
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data, "approval": False})


# The `ClientViewSet` class is a Django REST framework viewset for handling Client objects with a
# custom list method that returns serialized data with an additional "approval" key set to False.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise Http404("No clients found")
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data, "approval": False})

