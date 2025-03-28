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
            c = 60
        elif RCN >= 61 and RCN <= 67:
            coin.color = "Violet"
            c = 7
        elif RCN == 68:
            coin.color = "Indigo"
            c=1
        elif RCN >= 69 and RCN <= 75:
            coin.color = "Blue"
            c=7
        elif RCN >= 76 and RCN <= 81:
            coin.color = "Green"
            c=6
        elif RCN >= 82 and RCN <= 88:
            coin.color = "Yellow"
            c=7
        elif RCN >= 89 and RCN <= 95:
            coin.color = "Orange"
            c=7
        elif RCN >= 96 and RCN <= 100:
            coin.color = "Red"
            c=5

        CurVal = CurVal + 60 - c

        RHN = random.randint(1,10000)
        if RHN <= 7999:
            coin.holo = ""
            h=79.99
        elif RHN >= 8000 and RHN <= 8399:
            coin.holo = "Cracked Ice"
            h=4
        elif RHN >= 8400 and RHN <= 8799:
            coin.holo = "Confetti"
            h=4
        elif RHN >= 8800 and RHN <= 9199:
            coin.holo = "Moon"
            h=4
        elif RHN >= 9200 and RHN <= 9599:
            coin.holo = "Sun"
            h=4
        elif RHN >= 9600 and RHN <= 9999:
            coin.holo = "Radial"
            h=4
        elif RHN == 10000:
            coin.holo = "Inverse"
            h=0.01
        
        CurVal = CurVal + 80 - h

        coin.value = CurVal

        coin.save()
    # pick color and increase value

    # pick holo and increase value

    # return by adding new coin to table and redirect 
        return redirect(reverse('coin:player_detail',args = [pk]))


class CoinDeleteView(generic.DetailView): # list of coins with added delete button
    model = CoinType
    template_name = "coin/CoinDeleteView.html"

class DeleteCoin(generic.edit.DeleteView): # detletes the coin
    model = Coin
    success_url = reverse_lazy('coin:index')
