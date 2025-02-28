from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Item

# Create your views here.
class index(generic.ListView):
    model = Item
    template_name = 'todo/index.html'
    context_object_name  = 'todo_item_list'

class detail(generic.DetailView):
    model = Item
    template_name = 'todo/detail.html'

class CreateView(generic.edit.CreateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy("todo:index")

class DeleteView(generic.edit.DeleteView):
    model = Item
    success_url = reverse_lazy("todo:index")

