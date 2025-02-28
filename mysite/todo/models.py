from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.CharField(max_length = 200)

    dueDate = models.CharField(max_length = 32)

    def __str__(self):
        return self.text
