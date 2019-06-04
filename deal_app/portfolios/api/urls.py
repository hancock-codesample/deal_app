from django.urls import path
from deal_app.portfolios.api.views import PortfolioListCreateAPIView, PortfolioRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/<int:uuid>/',
         view=PortfolioRetrieveUpdateDestroyAPIView.as_view(),
         name='portfolio-rud-api'
         ),
    path(
        '/api/',
        view=PortfolioListCreateAPIView.as_view(),
        name='portfolio-create-api'
    )


]
