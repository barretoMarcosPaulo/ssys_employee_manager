from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse("auth_register")
        self.login_url = reverse("token_obtain_pair")
        self.employee_url = "/api/employees/"
        
        self.user_data = {
            "username": "user_teste",
            "password": "teste@user_teste",
            "password2": "teste@user_teste",
            "email": "teste_api@gmail.com",
            "first_name": "marcos paulo",
            "last_name": "barreto"
        }

        self.employee_data = {
            "name":"Funcionario Teste",
            "email":"funcionario_teste@gmail.com",
            "department":"DevOps",
            "salary":"5000.00",
            "birth_date":"1980-01-01"
        }


        return super().setUp()
    
    def tearDowns(self):
        return super().tearDown()

