from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version="v1",
        description="API documentation for the EMS",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# 👇 ADD THIS
schema_view.security_definitions = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": 'JWT auth, format: **Bearer &lt;token&gt;**',
    }
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/employees/", include("employees.urls")),
    path("api/attendance/", include("attendance.urls")),
    path("api/performance/", include("performance.urls")),
    path("api/token/",        TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/",TokenRefreshView.as_view(),  name="token_refresh"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("api-auth/", include("rest_framework.urls")),
]
