from django.contrib import admin
from django.urls import path
from django.views.decorators.http import require_GET
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import api_health, html_health

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", require_GET(html_health), name="health-html"),
    path("api/health/", require_GET(api_health), name="health-api"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
