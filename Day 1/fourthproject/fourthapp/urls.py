from django.urls import path
from fourthapp import views

urlpatterns = [
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact)
]
