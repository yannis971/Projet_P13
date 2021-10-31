"""
Module : urls.py
Modified by : Yannis Saliniere
"""
from django.urls import path

from . import views

app_name = "oc_lettings_site"

urlpatterns = [
    path("", views.index, name="index"),
]
