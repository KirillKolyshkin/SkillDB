from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=40)
    lvl = models.CharField(max_length=30, default="low")

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    group = models.IntegerField
    user_skills = models.ManyToManyField(Skill)

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
