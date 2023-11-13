from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('home/',views.home , name='home'),
]
