from django.shortcuts import render
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
]