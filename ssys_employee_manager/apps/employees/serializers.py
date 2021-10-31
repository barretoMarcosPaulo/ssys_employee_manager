from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeesSearchSerializer(serializers.Serializer):
    search = serializers.CharField(required=True, max_length=156)
