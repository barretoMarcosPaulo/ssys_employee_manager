from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from .models import Employee
from .serializers import EmployeeSerializer, EmployeesSearchSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesSearchViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeesSearchSerializer

    def post(self, *args):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        search = serializer.data["search"]

        employees = Employee.objects.filter(
            Q(
                Q(name__icontains=search)|
                Q(email__icontains=search)|
                Q(department__icontains=search)
            )
        ).distinct()
        
        return Response(
            EmployeeSerializer(employees, many=True).data,
            status=status.HTTP_200_OK,
        )