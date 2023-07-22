from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('start/', views.start, name="start"),
    path('check/', views.check, name='generate'),
]
