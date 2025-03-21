from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse, reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

import random

from .models import CoinType, Coin 

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "coin/home.html")



class Index(generic.ListView):
    model = CoinType
    template_name = "coin/index.html"

### Player Views ###

class PlayerList(generic.ListView): # list of players
    model = User
    template_name = "coin/PlayerList.html"

class PlayerDetail(generic.DetailView): # list of player's coins
    model = User
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


class CreateCoin(LoginRequiredMixin,View):

    def GET(self, request, pk):
        return redirect(reverse('coin:home'))

    def POST(self, request, pk):

    # get coin type name and value
        u = get_object_or_404(User, id = pk)
        #c = Coin(cointype=Bolt) 
    # pick color and increase value

    # pick holo and increase value

    # return by adding new coin to table and redirect 
        return redirect(reverse_lazy('coin:home'))


class CoinDeleteView(generic.DetailView): # list of coins with added delete button
    model = CoinType
    template_name = "coin/CoinDeleteView.html"

class DeleteCoin(generic.edit.DeleteView): # detletes the coin
    model = Coin
    success_url = reverse_lazy('coin:index')
