from django.contrib import admin

from .models import Employee, Project, Department, EmployeeAccess, EmployeeAccessProject, EmployeeAccessDepartment

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(EmployeeAccess)
admin.site.register(EmployeeAccessProject)
admin.site.register(EmployeeAccessDepartment)
