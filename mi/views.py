from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def rohit(request):
    return render(request,'mi.html')

def sachin(request):
    return render(request,'mi.html')