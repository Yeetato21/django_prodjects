from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

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

class CreateCoinType(generic.edit.CreateView):
    model = CoinType
    fields = '__all__'
    success_url = reverse_lazy('coin:index')

class DeleteCoinType(generic.edit.DeleteView):
    model = CoinType
    success_url = reverse_lazy('coin:index')

class CreateCoin(generic.edit.CreateView):
    model = Coin
    fields = '__all__'
    success_url = reverse_lazy('coin:index')

class DeleteCoin(generic.edit.DeleteView):
    model = Coin
    fields = '__all__'
    success_url = reverse_lazy('coin:index')
