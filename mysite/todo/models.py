from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.CharField(max_length = 200)
    startDate = models.DateTimeField('start date')
    dueDate = models.DateTimeField('due date')

    def __str__(self):
        return self.itemText
