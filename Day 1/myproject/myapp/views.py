from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def greeting(request):
    s = "Hello and welcome to my firstproject"
    return HttpResponse(s)

def myclass(request):
    c = "This is my AIDS class"
    return HttpResponse(c)

def myname(request):
    n = "Nikhlesh Shukla"
    return HttpResponse(n)
