from django.urls import path, include
from.views import BaseView, ActivityListView, ActivityItemView

from . import views

urlpatterns = [
    path('', BaseView.as_view()),
    path('index/', ActivityListView.as_view()),
    path('index/activity/<int:pk>/', ActivityItemView.as_view(), name = 'activity_item')

]
