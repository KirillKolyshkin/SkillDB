from django.contrib import admin
from .models import Student
from .models import Skill
from .models import Staff

# Register your models here.

admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(Staff)