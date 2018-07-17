from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Student
from .models import Skill
from .models import TemporaryModel
from django.shortcuts import render


def student_show_skills_view(request, username):
    student = Student.objects.get(username=username)
    return render(request, 'polls/student_skills.html', {'student': student})



def addSkill(request, student, skill, lvl):
    m = TemporaryModel.objects.create(user_id=student, skill_id=skill, lvl=lvl)
    m.save()
    context = {'student': student}
    return render(request, 'polls/index.html', context)# страницу сами нужную вставите


def GetStudentsBySkill(request, needed_skill):
    students = [s for s in Student.objects.all() if s.skills.contains(needed_skill)]
    return students


def byName_key(student):
    return student.user


def SortByName(students):
    students = sorted(students, key=byName_key)
    return students


def byGroup_key(student):
    return student.group


def SortByGroup(students):
    students = sorted(students, key=byGroup_key)
    return students


def bySkills_key(student):
    return student.skills.count


def SortBySkillAmount(students):
    students = sorted(students, key=bySkills_key)
    return students


def index(request):
    students = Student.objects.all()
    skills = Skill.objects.all()
    for student in students:
        for skill in skills:
            m = TemporaryModel.objects.create(user_id=student, skill_id=skill,
            lvl=5)
            m.save()
    context = {'students': students} #,'smth':something}
    return render(request, 'polls/index.html', context)


def getSkills(request, user):
    student = Student.objects.get(user=user)
    return render(request, 'polls/student_skills.html', {'student':student})  # страницу сами нужную вставите




