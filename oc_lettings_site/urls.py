"""
Module : urls.py
Modified by : Yannis Saliniere
"""
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'oc_lettings_site'

urlpatterns = [
    path('', views.index, name='index'),
]
