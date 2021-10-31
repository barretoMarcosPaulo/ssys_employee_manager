from rest_framework import status, viewsets
from rest_framework.response import Response
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated

from ssys_employee_manager.apps.employees.models import Employee
from ssys_employee_manager.apps.employees.serializers import EmployeeSerializer


class AgeReportViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        <strong>Response samples:</strong><br>
        <pre>
        <code>
            {
                "youngerer": {
                    "id": 7,
                    "name": "Piter Parker",
                    "email": "omi_aranha@ssys.com.br",
                    "department": "Full Stack",
                    "salary": "400.00",
                    "birth_date": "2000-01-01"
                },
                "older": {
                    "id": 1,
                    "name": "Anakin Skywalker",
                    "email": "skywalker@ssys.com.br",
                    "department": "Architecture",
                    "salary": "4000.00",
                    "birth_date": "1913-01-01"
                },
                "average": 64
            }
        </code>
        </pre>
        """
        all_employees = Employee.objects.all()

        if all_employees:
            current_year = timezone.now().year
            younger_employee = Employee.objects.latest("birth_date")
            older_employee = Employee.objects.earliest("birth_date")

            age_younger_employee = current_year - younger_employee.birth_date.year
            age_older_employee = current_year - older_employee.birth_date.year

            datas = {
                "youngerer": EmployeeSerializer(younger_employee).data,
                "older": EmployeeSerializer(older_employee).data,
                "average": (age_younger_employee + age_older_employee) // 2,
            }

            return Response(
                datas,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                [],
                status=status.HTTP_200_OK,
            )


class SalaryReportViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        """
        <strong>Response samples:</strong><br>
        <pre>
        <code>
            {
                "lowest": {
                    "id": 7,
                    "name": "Piter Parker",
                    "email": "omi_aranha@ssys.com.br",
                    "department": "Full Stack",
                    "salary": "400.00",
                    "birth_date": "2000-01-01"
                },
                "highest": {
                    "id": 6,
                    "name": "Bruce Wayne",
                    "email": "bruce_wayne@ssys.com.br",
                    "department": "Backend",
                    "salary": "74000.00",
                    "birth_date": "1999-01-01"
                },
                "average": 37200.0
            }
        </code>
        </pre>
        """
        all_employees = Employee.objects.all()

        if all_employees:
            highest_salary_employee = Employee.objects.latest("salary")
            lowest_salary_employee = Employee.objects.earliest("salary")
            salary_sum = highest_salary_employee.salary + lowest_salary_employee.salary

            datas = {
                "lowest": EmployeeSerializer(lowest_salary_employee).data,
                "highest": EmployeeSerializer(highest_salary_employee).data,
                "average": salary_sum // 2,
            }

            return Response(
                datas,
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                [],
                status=status.HTTP_200_OK,
            )
