from django.db import models


class Employee(models.Model):
    name = models.CharField('Наименование', max_length=100)


class AccessScore(models.Model):
    pass


class Project(models.Model):
    name = models.CharField('Наименование', max_length=100)
    score = models.OneToOneField(AccessScore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_all_emps(self):
        return self.score.employee_accesses.all()


class Department(models.Model):
    name = models.CharField('Наименование', max_length=100)
    score = models.OneToOneField(AccessScore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_all_emps(self):
        return self.score.employee_accesses.all()


class EmployeeAccess(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accesses')
    score = models.ForeignKey(AccessScore, on_delete=models.CASCADE, related_name='employee_accesses')


"""
    Плюсы:
     - можно выбрать все AccessScore
     - нет сложной валидации

    Минусы:
     - нужно создавать AccessScore
     - в данном случае AccessScore - пустая таблица
     - нужен постоянный join на AccessScore
     - нужно отдельно создавать AccessScore

"""
