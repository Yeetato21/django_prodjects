from django.shortcuts import render
from django.views import generic

from .models import TimeSlot, Reser

# Create your views here.

class Index(generic.ListView):
    model = TimeSlot
    template_name = "Culinary/index.html"

class TimeSlotDetail(generic.DetailView):
    model = TimeSlot
    template_name = "Culinary/TimeSlotDetail.html"

class ReserDetail(generic.DetailView):
    model = Reser
    template_name = "Culinary/ReserDetail.html"
    
