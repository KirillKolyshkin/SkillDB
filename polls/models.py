from django.db import models

class Skills(models.Model):
    skill_id = models.IntegerField
    skill_name = models.CharField(max_length=40)
    skill_lvl = models.CharField(max_length=30, default="low")

class Students(models.Model):
    user_id = models.IntegerField
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=20)
    user_group = models.IntegerField
    user_skills = models.ManyToManyField(Skills)

class Teachers(models.Model):
    teacher_id = models.IntegerField
    teacher_name = models.CharField(max_length=20)
    teacher_email = models.EmailField(max_length=254)
    teacher_password = models.CharField(max_length=20)


# Create your models here.
