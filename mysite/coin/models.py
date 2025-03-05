from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length = 16)

    def __str__(self):
        return str(self.name)

class CoinType(models.Model):
    name = models.CharField(max_length = 32)
    value = models.IntegerField(default = 1)
    desc = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

class Coin(models.Model):
    value = models.IntegerField(default = 1)
    color = model.CharField(max_length = 16)
    holo = model.CharField(max_lenth = 32)

    def __str__(self):
        return self.name
