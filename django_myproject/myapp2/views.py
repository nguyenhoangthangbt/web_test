# Create your views here.
from django.shortcuts import render

def home_myapp2(request):
    return render(request, 'myapp2/home_myapp2.html')
