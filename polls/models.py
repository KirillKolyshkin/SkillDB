from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=40)


class TemporaryModel(models.Model):
    user_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    skill_id = models.ForeignKey('Skill', on_delete=models.CASCADE)
    lvl = models.CharField(max_length=12, default="low")


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    group = models.IntegerField(max_length=6, null='true')
    skills = models.ManyToManyField(Skill, through=TemporaryModel)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

# Create your models here.
