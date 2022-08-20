from django.urls import path, include
from.views import BaseView, RideListView, RideItemView

from . import views

urlpatterns = [
    path('', BaseView.as_view()),
    path('index/', RideListView.as_view()),
    path('index/rides/<int:pk>/', RideItemView.as_view(), name = 'ride_item')

]
