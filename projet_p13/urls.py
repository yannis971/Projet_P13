"""
Module : urls.py
Modified by : Yannis Saliniere
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("oc_lettings_site.urls", namespace="oc_lettings_site")),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]
