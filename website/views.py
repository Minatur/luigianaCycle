from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from django.template import loader

from .models import ride



# Create your views here.
class BaseView(TemplateView):
    template_name = "website_base.html"



class RideItemView(DetailView):
    model = ride
    template_name = 'ride.html'
    context_object_name = 'ride_item'

class RideListView(ListView):
    model = ride
    template_name = 'index.html'
    context_object_name = 'ride_list'
