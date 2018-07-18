from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=40)
    def __str__ (self):
    	return self.name


class StudentSkills(models.Model):
    user_id = models.ForeignKey('Students', on_delete='RESTRICT')
    skill_id = models.ForeignKey('Skills', on_delete='RESTRICT')
    lvl = models.SmallIntegerField(max_length=1, default="3")


class Students(models.Model):
    user = models.ForeignKey(User, on_delete='RESTRICT', default=0)
    group = models.CharField(max_length=12)
    skills = models.ManyToManyField(Skills, through=StudentSkills)
    def __str__ (self):
   		return self.user

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete='RESTRICT', default=0)
    def __str__ (self):
    	return self.user
