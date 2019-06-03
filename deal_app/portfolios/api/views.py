from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from deal_app.portfolios.models import Portfolio
from deal_app.portfolios.api.serializers import PortfolioSerializer


class PortfolioListCreateAPIView(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PortfolioSerializer
    lookup_field = 'uuid'


class PortfolioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PortfolioSerializer
    lookup_field = 'uuid'
