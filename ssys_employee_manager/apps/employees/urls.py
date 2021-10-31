from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EmployeeViewSet, EmployeesSearchViewSet

app_name = "employees"

router = DefaultRouter()
router.register("", EmployeeViewSet, basename="employees")

urlpatterns = [
    path(
        "search/",
        EmployeesSearchViewSet.as_view({"post": "post"}),
    ),
]

urlpatterns += router.urls
