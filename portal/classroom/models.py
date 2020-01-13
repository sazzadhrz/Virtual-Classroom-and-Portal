from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    department = models.CharField()
    mobile = models.IntegerField()


class Teacher(Person):
    initial = models.CharField(max_length=4)


class Student(Person):
    s_id = models.IntegerField(max_length=10)
