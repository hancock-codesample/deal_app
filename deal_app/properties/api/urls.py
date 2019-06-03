# flavors/urls.py
from django.conf.urls import url
from django.urls import path

from .api import views

urlpatterns = [
    path(
        '/',
        view=views.PropertyFlavorListCreateAPIView.as_view(),
        name='property_rest_api'
    ),
    url(
        regex=r'^api/(?P<uuid>[-\w]+)/$',
        view=views.PropertyRetrieveUpdateDestroyAPIView.as_view(),
        name='flavor_rest_api'
    )
]
