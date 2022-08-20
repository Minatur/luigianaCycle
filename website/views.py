from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from django.template import loader

from .models import activity



# Create your views here.
class BaseView(TemplateView):
    template_name = "website_base.html"



class ActivityItemView(DetailView):
    model = activity
    template_name = 'activity.html'
    context_object_name = 'activity_item'

class ActivityListView(ListView):
    model = activity
    template_name = 'index.html'
    context_object_name = 'activity_list'
