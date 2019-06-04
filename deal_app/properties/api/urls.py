# flavors/urls.py
from django.urls import path

from deal_app.properties.api.views import Pro

urlpatterns = [
    path(
        '/',
        view=views.PropertyFlavorListCreateAPIView.as_view(),
        name='property_rest_api'
    ),
    url(
        regex=r'^api/(?P<uuid>[-\w]+)/$',
        view=views.PropertyRetrieveUpdateDestroyAPIView.as_view(),
        name='property-rud-api'
    )
]
