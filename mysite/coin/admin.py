from django.contrib import admin
from .models import CoinType, Coin

# Register your models here.
admin.site.register(CoinType)
admin.site.register(Coin)
