from django.db import models


class Employee(models.Model):
    name = models.CharField('Наименование', max_length=100)


class AccessScore(models.Model):
    pass


class Project(models.Model):
    name = models.CharField('Наименование', max_length=100)
    score = models.OneToOneField(AccessScore, on_delete=models.CASCADE)

    def get_all_emps(self):
        return self.score.employee_accesses.all()


class Department(models.Model):
    name = models.CharField('Наименование', max_length=100)
    score = models.OneToOneField(AccessScore, on_delete=models.CASCADE)

    def get_all_emps(self):
        return self.score.employee_accesses.all()


class EmployeeAccess(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accesses')
    score = models.ForeignKey(AccessScore, on_delete=models.CASCADE, related_name='employee_accesses')


"""
    Плюсы:
     - можно выбрать все AccessScore
     - не нужно самостоятельно создавать AccessScore
     - хорошо выглядит в админке

    Минусы:
     - нужно создавать AccessScore
     - в данном случае AccessScore - пустая таблица
     - дубливароние кода или 2 абстрации

"""
