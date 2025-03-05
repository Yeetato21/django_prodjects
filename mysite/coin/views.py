from django.shortcuts import render
from django.views import generic

from .models import CoinType, Coin

# Create your views here.

class Index(generic.ListView):
    model = CoinType
    template_name = "coin/index.html"

class CoinTypeDetail(generic.DetailView):
    model = CoinType
    template_name = "coin/CoinTypeDetail.html"

class CoinDetail(generic.DetailView):
    model = Coin
    template_name = "coin/CoinDetail.html"
