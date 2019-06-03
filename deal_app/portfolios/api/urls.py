from django.conf.urls import url
from django.urls import path

from deal_app.portfolios.api import views

urlpatterns = [
    path(
        '/api/',
        view=views.PortfolioListCreateAPIView.as_view(),
        name='flavor_rest_api'
    ),
    # /flavors/api/:slug/
    url('api/<uuid>/',
        regex=r'^api/(?P<uuid>[-\w]+)/$',
        view=views.PortfoliosRetrieveUpdateDestroyAPIView.as_view(),
        name='flavor_rest_api'
        )
]
