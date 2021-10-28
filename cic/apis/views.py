from rest_framework import viewsets
from .models import Person, Organization
from .serializers import PersonSerializer, OrganizationSerializer, CreatePersonSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='All people available in CIC'))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description='You must be logged in. Use the JSON structure and schema as shown below.'))
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonSerializer
        if self.action == 'create':
            return CreatePersonSerializer

    http_method_names = ['get', 'post', 'delete', 'put']


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='All organizations available in CIC'))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description='You must be logged in. Use the JSON structure and schema as shown below.'))
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    http_method_names = ['get', 'post', 'delete', 'put']



