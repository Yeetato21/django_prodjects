from django.urls import path

from . import views

app_name = "coin"
urlpatterns = [
    path("", views.Index.as_view(), name = "index"),
    path("CoinType/<int:pk>/", views.CoinTypeDetail.as_view(), name = "coin_type_detail"),
    path("Coin/<ink:pk>/", views.CoinDetail.as_view(), name = "coin_detail"),
]
