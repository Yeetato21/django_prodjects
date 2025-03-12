from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length = 16)
    coins = models.ManyToManyField('Coin', through = 'Collection') 

    def __str__(self):
        return str(self.name)

class CoinType(models.Model):
    name = models.CharField(max_length = 32)
    value = models.IntegerField(default = 1)
    desc = models.CharField(max_length = 256, default = "")

    def __str__(self):
        return self.name

class Coin(models.Model):
    name = models.ForeignKey(CoinType, on_delete = models.CASCADE) 
    value = models.IntegerField(default = 1)
    color = models.CharField(max_length = 16, default = "Grey")
    holo = models.CharField(max_length = 32, default = "None")
    num = models.IntegerField(default = 0)
    owners = models.ManyToManyField('Player', through = 'Collection')

    def __str__(self):
        return str(self.name)

class Collection(models.Model):
    coin = models.ForeignKey(Coin, on_delete = models.CASCADE)
    player = models.ForeignKey(Player, on_delete = models.CASCADE) 
