from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world! You are at the website for Luigiana.")
# Create your views here.
