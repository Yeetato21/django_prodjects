from django.contrib import admin
from .models import Player, CoinType, Coin, Collection

# Register your models here.
admin.site.register(Player)
admin.site.register(CoinType)
admin.site.register(Coin)
admin.site.register(Collection)
