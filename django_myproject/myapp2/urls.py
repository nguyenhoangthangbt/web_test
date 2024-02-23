from django.http import HttpRequest
from django.shortcuts import render
from django.urls import path
from . import views,models

urlpatterns = [
    path('',views.home_myapp2)
]
