from rest_framework import serializers
from .models import Company, Client

# The CompanySerializer class is a Django REST framework serializer for the Company model that
# includes all fields.
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# The `ClientSerializer` class is a Django REST framework serializer for the `Client` model with all
# fields included.
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
