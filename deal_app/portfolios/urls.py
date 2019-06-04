from django.urls import path
from deal_app.portfolios.api.views import PortfolioRetrieveUpdateDestroyAPIView, PortfolioListCreateAPIView
from deal_app.portfolios.views import (
    portfolio_detail_view,
    portfolio_list_view,
    portfolio_create_view,
    portfolio_update_view,
    portfolio_delete_view,
)

app_name = "portfolios"
urlpatterns = [
    path(
        "create/",
        view=portfolio_create_view,
        name="create"
    ),
    path(
        "",
        view=portfolio_list_view,
        name="list"
    ),
    path(
        "new/",
        view=portfolio_create_view,
        name="new"
    ),
    path(
        "<str:username>/<int:pk>",
        view=portfolio_detail_view,
        name="detail"
    ),
    path(
        "<int:pk>/delete/",
        view=portfolio_delete_view,
        name="delete"
    ),
    path(
        "<int:pk>/update/",
        view=portfolio_update_view,
        name="update"
    ),
    path('api/<int:uuid>/',
         view=PortfolioRetrieveUpdateDestroyAPIView.as_view(),
         name='portfolio-rud-api'
         ),
    path(
        'api/portfolio/',
        view=PortfolioListCreateAPIView.as_view(),
        name='portfolio-create-api'
    )

]
