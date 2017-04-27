from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
