from django.shortcuts import render
from django.views import generic

from .models import Item

# Create your views here.
class index(generic.ListView):
    model = Item
    template_name = 'todo/index.html'
    context_object_name  = 'todo_item_list'

class detail(generic.DetailView):
    model = Item
    template_name = 'todo/detail.html'
