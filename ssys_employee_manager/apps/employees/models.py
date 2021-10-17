from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=156, blank=False, null=False)
    email = models.CharField(max_length=156, blank=False, null=False)
    department = models.CharField(max_length=156, blank=False, null=False)
    salary = models.DecimalField("Valor", max_digits=13, decimal_places=2)
    birth_date = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name