"""DjangoAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('EmployeeApp.urls'))
]
