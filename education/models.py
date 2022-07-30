from django.db import models


class School(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.name} - {self.address}'


class SClass(models.Model):
    grade = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.grade} - {self.school}'

class Student(models.Model):
    name = models.CharField(max_length=64)
    sclass = models.ForeignKey(SClass, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.sclass}'
