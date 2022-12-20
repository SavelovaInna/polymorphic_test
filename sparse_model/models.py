from django.core.exceptions import ValidationError
from django.db import models


class Employee(models.Model):
    name = models.CharField('Наименование', max_length=100)


class Project(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name


class EmployeeAccess(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accesses')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='employee_accesses')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name='employee_accesses')

    def get_access_object_name(self):
        if self.project:
            return str(self.project)
        if self.department:
            return str(self.department)

    def clean(self):
        cleaned_data = super().clean()
        project = cleaned_data.get("project")
        department = cleaned_data.get("department")
        if not project and not department:
            raise ValidationError('Не указан объект для выдачи доступа')

        if project and department:
            raise ValidationError(
                'Не возможно создать объект с обоими видами объектов.Выберите или проект или подразделение')


def get_emp_accesses(employee):
    return employee.accesses.all()


def get_project_employees(project):
    return EmployeeAccess.objects.filter(project=project)


def get_department_employees(department):
    return EmployeeAccess.objects.filter(department=department)


"""
    Плюсы:
      - Проект и подразделение могут ничего не знать о логике доступа к ним
      - Инзначально простое решение

    Минусы:
     - Сложная валидация
     - Добавление еще одного типа объектов для выдачи прав приводит к миграции и еще большему усложнению
     - Нет общих методов для получения доступов для проктов и подразделений

"""
