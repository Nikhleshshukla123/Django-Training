from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que1 = "Who developed python"
    a1 = "Dennis Ritchie"
    b1 = "Nikhlesh Shukla"
    c1 = "Mustafa Quasimali"
    d1 = "Pankaj Kushwah"

    que2 = "Who developed python"
    a2 = "Dennis Ritchie"
    b2 = "Nikhlesh Shukla"
    c2 = "Mustafa Quasimali"
    d2 = "Pankaj Kushwah"

    que3 = "Who developed python"
    a3 = "Dennis Ritchie"
    b3 = "Nikhlesh Shukla"
    c3 = "Mustafa Quasimali"
    d3 = "Pankaj Kushwah"

    que4 = "Who developed python"
    a4 = "Dennis Ritchie"
    b4 = "Nikhlesh Shukla"
    c4 = "Mustafa Quasimali"
    d4 = "Pankaj Kushwah"

    que5 = "Who developed python"
    a5 = "Dennis Ritchie"
    b5 = "Nikhlesh Shukla"
    c5 = "Mustafa Quasimali"
    d5 = "Pankaj Kushwah"

    context = {
        'que1' : que1,
        'a1' : a1,
        'b1' : b1,
        'c1' : c1,
        'd1' : d1,

        'que2' : que2,
        'a2' : a2,
        'b2' : b2,
        'c2' : c2,
        'd2' : d2,

        'que3' : que3,
        'a3' : a3,
        'b3' : b3,
        'c3' : c3,
        'd3' : d3,

        'que4' : que4,
        'a4' : a4,
        'b4' : b4,
        'c4' : c4,
        'd4' : d4,

        'que5' : que5,
        'a5' : a5,
        'b5' : b5,
        'c5' : c5,
        'd5' : d5
    }

    teplate = loader.get_template("testpaper.html")
    res = teplate.render(context,request)
    return HttpResponse(res)