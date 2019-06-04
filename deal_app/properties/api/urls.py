from django.urls import path
from deal_app.properties.api.views import PropertyListCreateAPIView, PropertyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path(
        'api/property/',
        view=PropertyListCreateAPIView.as_view(),
        name='property-create-api'
    ),
    path(
        'api/<int:uuid>-property',
        view=PropertyRetrieveUpdateDestroyAPIView.as_view(),
        name='property-rud-api'
    )
    path(
        '/',
        view=PropertyListCreateAPIView.as_view(),
        name='property-create-api'
    ),
    path(
        'api/<int:uuid>-property',
        view=PropertyRetrieveUpdateDestroyAPIView.as_view(),
        name='property-rud-api'
    ) path(
        '/',
        view=PropertyListCreateAPIView.as_view(),
        name='property-create-api'
    ),
    path(
        'api/<int:uuid>-property',
        view=PropertyRetrieveUpdateDestroyAPIView.as_view(),
        name='property-rud-api'
    )
]
