from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicParentModelAdmin

from .models import Employee, Project, Department, EmployeeAccess, EmployeeAccessProject, EmployeeAccessDepartment

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Department)


class ModelAChildAdmin:
    pass


@admin.register(EmployeeAccessProject)
class EmployeeAccessProjectAdmin(PolymorphicChildModelAdmin):
    base_model = EmployeeAccessProject


@admin.register(EmployeeAccessDepartment)
class EmployeeAccessDepartmentAdmin(PolymorphicChildModelAdmin):
    base_model = EmployeeAccessDepartment


@admin.register(EmployeeAccess)
class EmployeeAccessAdmin(PolymorphicParentModelAdmin):
    base_model = EmployeeAccess
    child_models = (EmployeeAccessProject, EmployeeAccessDepartment)
