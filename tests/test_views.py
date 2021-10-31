import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from django.urls import reverse

from ssys_employee_manager.apps.employees.models import Employee


class LoginTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse("auth_register")
        self.login_url = reverse("token_obtain_pair")

        self.user_data = {
            "username": "user_teste",
            "password": "teste@user_teste",
            "password2": "teste@user_teste",
            "email": "teste_api@gmail.com",
            "first_name": "marcos paulo",
            "last_name": "barreto",
        }

        return super().setUp()

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        response = self.client.post(self.register_url, self.user_data)

        response = self.client.post(
            self.login_url,
            {
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmployeesTestCase(APITestCase):
    def setUp(self):
        self.employee_url = "/api/employees/"

        self.employee_data = {
            "name": "Funcionario Teste",
            "email": "funcionario_teste@gmail.com",
            "department": "DevOps",
            "salary": "5000.00",
            "birth_date": "1980-01-01",
        }
        self.employee_data_update = {
            "name": "Funcionario",
            "email": "funcionario_teste@gmail.com",
            "department": "DevOps",
            "salary": "5000.00",
            "birth_date": "1980-01-01",
        }

        self.user = User.objects.create_user(username="teste", password="teste")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_employee(self):
        response = self.client.post(self.employee_url, self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employee(self):
        self.test_create_employee()

        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_details_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.get(self.employee_url + str(employee.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.put(
            self.employee_url + str(employee.id) + "/", self.employee_data_update
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.delete(self.employee_url + str(employee.id) + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
