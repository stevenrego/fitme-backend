from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Health
    path("api/", include("apps.common.urls")),

    # Auth + Users
    path("api/auth/", include("apps.users.urls_auth")),
    path("api/users/", include("apps.users.urls_users")),

    # Schema / Docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
