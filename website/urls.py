from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^$', 'website.views.home', name='home'),
]
