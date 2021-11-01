"""
Module : urls.py
Modified by : Yannis Saliniere
"""
from django.urls import path

from . import views

app_name = "oc_lettings_site"


def trigger_error(request):
    division_by_zero = 1 / 0
    del division_by_zero


urlpatterns = [
    path("", views.index, name="index"),
    path("sentry-debug/", trigger_error),
]
