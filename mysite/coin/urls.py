from django.urls import path

from . import views

app_name = "coin"
urlpatterns = [
    path("home", views.Home.as_view(), name = "home"),

    path("", views.Index.as_view(), name = "index"),
    path("CoinType/<int:pk>/", views.CoinTypeDetail.as_view(), name = "coin_type_detail"),
    path("Coin/<int:pk>/", views.CoinDetail.as_view(), name = "coin_detail"),

    path('addcointype/',views.CreateCoinType.as_view(), name = 'add_coin_type'),
    path('cointypedeleteview/',views.CoinTypeDeleteView.as_view(), name = 'coin_type_delete_view'),
    path('deletecointype/<int:pk>',views.DeleteCoinType.as_view(), name = 'delete_coin_type'),

    # path('addcoin/',views.CreateCoin.as_view(), name = 'add_coin'),
    path('coindeleteview/<int:pk>',views.CoinDeleteView.as_view(), name = 'coin_delete_view'),
    path('deletecoin/<int:pk>',views.DeleteCoin.as_view(), name = 'delete_coin'),

    path('playerlist/', views.PlayerList.as_view(), name = 'player_list'),
    path('player/<int:pk>/', views.PlayerDetail.as_view(), name = 'player_detail'), 
]
