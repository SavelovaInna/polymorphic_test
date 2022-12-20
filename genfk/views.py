from genfk.models import EmployeeAccess


def get_all_emp_accesses(emp):
    return emp.accesess.all()


def get_emps_for_object(obj):
    return EmployeeAccess.objects.filter(content_object=obj)
