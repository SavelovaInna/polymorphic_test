from django.db import models


class Employee(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def get_all_accesses(self, obj):
        self.accesses.filter(score=obj)


class AccessScore(models.Model):
    name = models.CharField('Наименование', max_length=100)

    def __str__(self):
        return self.name

    def get_all_employees(self):
        return self.employee_accesses.all().values_list('emp', flat=True)


class Project(AccessScore):
    pass


class Department(AccessScore):
    pass


class EmployeeAccess(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accesses')
    score = models.ForeignKey(AccessScore, on_delete=models.CASCADE, related_name='employee_accesses')


"""
    Плюсы:
     - можно выбрать все AccessScore
     - интуитивная объектная модель и полиформизм, получается что Department является AccessScore
     - не нужно самостоятельно создавать AccessScore
     
    Минусы:
     - при выборке из базы Project и Department всегда делается join на таблицу AccessScore
     - django не поддерживает множественное наследование моделей, поэтому применить такой подход еще раз не получится,
    если потребуется расширять логику моделей Project или Department
     
"""
