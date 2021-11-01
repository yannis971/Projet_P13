"""
Module : urls.py
Modified by : Yannis Saliniere
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("oc_lettings_site.urls", namespace="oc_lettings_site")),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]
"""
handler403 = "oc_lettings_site.views.my_custom_permission_denied_view"
handler404 = 'oc_lettings_site.views.handler404'
handler500 = "oc_lettings_site.views.my_custom_error_view"
"""

if (
    settings.DEBUG or settings.DJANGO_SERVER_TYPE == "local"
) and not settings.AMAZON_STORAGE:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
