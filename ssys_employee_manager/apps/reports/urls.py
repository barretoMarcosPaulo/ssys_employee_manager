from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AgeReportViewSet, SalaryReportViewSet

app_name = "reports"

urlpatterns = [
    path("employees/age/", AgeReportViewSet.as_view({'get':'get'}) ,),
    path("employees/salary/", SalaryReportViewSet.as_view({'get':'get'}) ,),
]



