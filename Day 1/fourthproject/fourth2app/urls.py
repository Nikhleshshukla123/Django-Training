from django.urls import path
from fourth2app import views

urlpatterns = [
    path('testpaper/', views.testpaper),
    path('result/', views.result)
]
