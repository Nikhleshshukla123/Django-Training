from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template("home.html")
    res = template.render()
    return HttpResponse(res)

def index(request):
    template = loader.get_template("index.html")
    res = template.render()
    return HttpResponse(res)

def about(request):
    template = loader.get_template("about.html")
    res = template.render()
    return HttpResponse(res)

def contact(request):
    template = loader.get_template("contact.html")
    res = template.render()
    return HttpResponse(res)