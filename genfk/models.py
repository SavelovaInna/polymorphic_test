from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
