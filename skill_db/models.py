from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=40)

    def __init__(self, name):
        self.name = name

class StudentSkills(models.Model):
    user_id = models.ForeignKey('Student', on_delete='RESTRICT')
    skill_id = models.ForeignKey('Skill', on_delete='RESTRICT')
    lvl = models.PositiveSmallIntegerField(default=1)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=12, default='null')
    skills = models.ManyToManyField(Skill, through=StudentSkills)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

