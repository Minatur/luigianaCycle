from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.template import loader

from .models import ride


def index(request):
    rides_list = ride.objects.all()
    template = loader.get_template('index.html')
    context = {
        'rides_list': rides_list,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello world! You are at the website for Luigiana.")



# Create your views here.
class BaseView(TemplateView):
    template_name = "website_base.html"



class RideItemView(DetailView):
    model = ride
    template_name = 'ride.html'
    context_object_name = 'ride_item'
