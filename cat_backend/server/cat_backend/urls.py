from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("agency/", include("server.apps.cats.urls")),
]
