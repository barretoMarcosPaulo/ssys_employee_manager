from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EmployeeViewSet

app_name = "employees"

router = DefaultRouter()
router.register("", EmployeeViewSet, basename="employees")

urlpatterns = router.urls
