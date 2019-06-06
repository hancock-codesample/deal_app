from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from deal_app.properties.models import Property
from deal_app.properties.api.serializers import PropertySerializer


class PropertyListCreateAPIView(ListCreateAPIView):
    queryset = Property.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertySerializer
    lookup_field = 'uuid'


class PropertyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertySerializer
    lookup_field = 'uuid'
