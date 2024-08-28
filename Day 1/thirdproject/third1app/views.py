from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    h = '<h1>This is home page</h1>'
    return HttpResponse(h)

def about(request):
    a = '<h1>This is about page</h1>'
    return HttpResponse(a)

def contact(request):
    c = '<h1>This is contact page</h1>'
    return HttpResponse(c)