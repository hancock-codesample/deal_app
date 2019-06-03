from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from deal_app.properties.models import Property, PropertyIncome, PropertyPurchase
from deal_app.properties.api.serializers import PropertySerializer, PropertyIncomeSerializer, PropertyPurchaseSerializer


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


class PropertyIncomeCreateAPIView(ListCreateAPIView):
    queryset = PropertyIncome.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertyIncomeSerializer
    lookup_field = 'uuid'


class PropertyIncomeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PropertyIncome.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertyIncomeSerializer
    lookup_field = 'uuid'


class PropertyPurchaseCreateAPIView(ListCreateAPIView):
    queryset = PropertyPurchase.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertyPurchaseSerializer
    lookup_field = 'uuid'


class PropertyPurchaseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertyPurchaseSerializer
    lookup_field = 'uuid'
