from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Employees API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/employees/", include("ssys_employee_manager.apps.employees.urls")),
    path("api/reports/", include("ssys_employee_manager.apps.reports.urls")),
    path("api/auth/", include("ssys_employee_manager.apps.accounts.urls")),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
