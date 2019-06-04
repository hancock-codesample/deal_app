from django.urls import path
from deal_app.properties.api.views import PropertyListCreateAPIView, PropertyRetrieveUpdateDestroyAPIView, \
    PropertyIncomeCreateAPIView, PropertyIncomeRetrieveUpdateDestroyAPIView, PropertyPurchaseCreateAPIView, \
    PropertyPurchaseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        'api/property/',
        view=PropertyListCreateAPIView.as_view(),
        name='property-create-api'
    ),
    path(
        'api/<int:uuid>/property/',
        view=PropertyRetrieveUpdateDestroyAPIView.as_view(),
        name='property-rud-api'
    ),
    path(
        'api/property-income/',
        view=PropertyIncomeCreateAPIView.as_view(),
        name='property-income-create-api'
    ),
    path(
        'api/<int:uuid>/property-income/',
        view=PropertyIncomeRetrieveUpdateDestroyAPIView.as_view(),
        name='property-income-rud-api'
    ),
    path(
        'api/property-purchase/',
        view=PropertyPurchaseCreateAPIView.as_view(),
        name='property-purchase-create-api'
    ),
    path(
        'api/<int:uuid>/property-purchase/',
        view=PropertyPurchaseRetrieveUpdateDestroyAPIView.as_view(),
        name='property-purchase-rud-api'
    )
]
