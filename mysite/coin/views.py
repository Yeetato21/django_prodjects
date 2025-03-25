from django.shortcuts import render, redirect, get_object_or_404
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

    def get(self, request, pk):
        return redirect(reverse('coin:home'))

    def post(self, request, pk):
        ctids = [] 
        for i in CoinType.objects.all():
            ctids.append(i)
        CurCT = random.choice(ctids)
        CurVal = CurCT.basevalue
        
        coin = Coin()
        coin.cointype = CurCT
        coin.save()
        coin.owners.add(self.request.user)


        RCN = random.randint(1,100)
        if RCN <= 60:
            coin.color = "Grey"
        elif RCN >= 61 and RCN <= 67:
            coin.color = "Violet"
        elif RCN == 68:
            coin.color = "Indigo"
        elif RCN >= 69 and RCN <= 75:
            coin.color = "Blue"
        elif RCN >= 76 and RCN <= 81:
            coin.color = "Green"
        elif RCN >= 82 and RCN <= 88:
            coin.color = "Yellow"
        elif RCN >= 89 and RCN <= 95:
            coin.color = "Orange"
        elif RCN >= 96 and RCN <= 100:
            coin.color = "Red"


        coin.save()
    # pick color and increase value

    # pick holo and increase value

    # return by adding new coin to table and redirect 
        return redirect(reverse_lazy('coin:index'))


class CoinDeleteView(generic.DetailView): # list of coins with added delete button
    model = CoinType
    template_name = "coin/CoinDeleteView.html"

class DeleteCoin(generic.edit.DeleteView): # detletes the coin
    model = Coin
    success_url = reverse_lazy('coin:index')
