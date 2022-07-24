from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import ride


def index(request):
    return HttpResponse("Hello world! You are at the website for Luigiana.")
# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"
