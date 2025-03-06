from django.urls import path

from . import views

app_name = "coin"
urlpatterns = [
    path("", views.Index.as_view(), name = "index"),
    path("CoinType/<int:pk>/", views.CoinTypeDetail.as_view(), name = "coin_type_detail"),
    path("Coin/<int:pk>/", views.CoinDetail.as_view(), name = "coin_detail"),
    path('addcointype/',views.CreateCoinType.as_view(), name = 'add_coin_type'),
    path('deletecointype/<int:pk>',views.DeleteCoinType.as_view(), name = 'delete_coin_type'),
    path('addcoin/',views.CreateCoin.as_view(), name = 'add_coin'),
    path('deletecoin/',views.DeleteCoin.as_view(), name = 'delete_coin'),
]
