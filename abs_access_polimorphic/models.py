from django.db import models
from polymorphic.models import PolymorphicModel


class Employee(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def get_all_accesses(self, obj):
        self.accesses.filter(score=obj)


class Project(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name


class EmployeeAccess(PolymorphicModel):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accesses')


class EmployeeAccessProject(EmployeeAccess):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='employee_accesses')


class EmployeeAccessDepartment(EmployeeAccess):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employee_accesses')


def get_emp_accesses(emp):
    return EmployeeAccess.objects.filter(emp=emp)


"""
    Плюсы:
     - Не затрагивает модели проекта и подразделения
     - интуитивная объектная модель и полиформизм
     - создается всегда только 1 модель
     - меньше вероятность, что пригодится еще одно наследование

    Минусы:
     - при выборке из базы EmployeeAccessProject и EmployeeAccessDepartment всегда делается join на таблицу EmployeeAccess
     - можно выбрать все EmployeeAccess
     - сторонняя библиотека, могут возникнуть проблемы с поддержкой. Последняя поддерживаемая версия django=4.0

"""
