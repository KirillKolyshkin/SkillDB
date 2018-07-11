# Register your models here.

from django.contrib import admin

from .models import Student
from .models import Skill
from .models import Teacher

admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(Teacher)