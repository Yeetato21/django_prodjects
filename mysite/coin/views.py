from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

import random

from .models import CoinType, Coin, Player, Collection

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "coin/home.html")



class Index(generic.ListView):
    model = CoinType
    template_name = "coin/index.html"

### Player Views ###

class PlayerList(generic.ListView): # list of players
    model = Player
    template_name = "coin/PlayerList.html"

class PlayerDetail(generic.DetailView): # list of player's coins
    model = django.auth.user
    template_name = "coin/PlayerDetail.html"

### Coin Type Views ###

class CoinTypeDetail(generic.DetailView):
    model = CoinType
    template_name = "coin/CoinTypeDetail.html"

class CreateCoinType(generic.edit.CreateView):
    model = CoinType
    fields = '__all__'
    success_url = reverse_lazy('coin:index')

class CoinTypeDeleteView(LoginRequiredMixin, generic.ListView):
    model = CoinType
    template_name = "coin/CoinTypeDeleteView.html"

class DeleteCoinType(generic.edit.DeleteView):
    model = CoinType
    success_url = reverse_lazy('coin:index')

### Coin Views ###

class CoinDetail(generic.DetailView):
    model = Coin
    template_name = "coin/CoinDetail.html"


def CreateCoin(self, request, pk):
# get coin type name and value
    p = get_object_or_404(Player, id = pk)
    cointypes = list(CoinType.objects.get())
    for i in cointypes:
        print(i)
    # pick color and increase value

    # pick holo and increase value

    # return by adding new coin to table and redirect to index
    

class CoinDeleteView(generic.DetailView): # list of coins with added delete button
    model = CoinType
    template_name = "coin/CoinDeleteView.html"

class DeleteCoin(generic.edit.DeleteView): # detletes the coin
    model = Coin
    success_url = reverse_lazy('coin:index')
