from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def about(request):
    template=loader.get_template('about.html')
    res=template.render()
    return HttpResponse(res)

def home(request):
    template=loader.get_template('home.html')
    res=template.render()
    return HttpResponse(res)