from django.shortcuts import render
from django.views import generic

from .models import TimeSlot, Reser

# Create your views here.

class Index(generic.ListView):
    model = TimeSlot
    template_name = 'Culinary/index.html'
    context_object_name  = 'Culinary_timeslot_list'

class TimeSlotDetail(generic.ListView):
    model = TimeSlot
    template_name = 'Culinary/timeslotdetail.html'
    context_object_name = 'timeslot_Reser_list'

class ReserDetail(generic.DetailView):
    model = Reser
    template_name = 'Culinary/reser.html'
    
