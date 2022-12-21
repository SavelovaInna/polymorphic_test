from django.core.exceptions import ValidationError
from django.db import models


class Employee(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def get_all_access_objects(self):
        return self.accesses.all()


class Project(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name

    def get_all_employees(self):
        return EmployeeAccess.objects.filter(score__project=self)


class Department(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name

    def get_all_employees(self):
        return EmployeeAccess.objects.filter(score__department=self)


class AccessScore(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='scores')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='scores')

    def clean(self):
        cleaned_data = super().clean()
        project = cleaned_data.get("project")
        department = cleaned_data.get("department")
        if not project and not department:
            raise ValidationError('Не указан объект для выдачи доступа')


class EmployeeAccess(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accesses')
    score = models.ForeignKey(AccessScore, on_delete=models.CASCADE, related_name='employee_accesses')


def get_emp_accesses(employee):
    return employee.accesses.all()


def get_project_employees(project):
    return EmployeeAccess.objects.filter(score__project=project)


def get_department_employees(department):
    return EmployeeAccess.objects.filter(score__department=department)


"""
    Плюсы:
     - есть некоторая абстракция в которую можно инкапсулитровать логику

    Минусы:
     - Сложная валидация
     - Добавление еще одного типа объектов для выдачи прав приводит к миграции и еще большему усложнению
     - Нет общих методов для получения доступов для проектов и подразделений
     
     - нужен постоянный join на AccessScore
     - нужно отдельно создавать AccessScore
"""
