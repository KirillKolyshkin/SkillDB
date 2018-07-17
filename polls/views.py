from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Student
from .models import Skill
from .models import TemporaryModel
from django.shortcuts import render


def addSkill(request, student, skill, lvl):
    m = TemporaryModel.objects.create(user_id=student, skill_id=skill, lvl=lvl)
    m.save()
    context = {'student': student}
    return render(request, 'polls/index.html', context)# страницу сами нужную вставите


def getSkills(request, student):
    context = {'student': student}
    return render(request, 'polls/index.html', context)  # страницу сами нужную вставите


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
    '''stud_ent = Student.objects.all().last()
    ski_ll = Skill.objects.create(name='SoHard')
    m1 = TemporaryModel(user_id=stud_ent, skill_id=ski_ll, lvl=5)
    m1.save()'''


    students = Student.objects.all()
    skills = Skill.objects.all()
    '''skill = Skill.objects.create(name='SoHard')
    temp = TemporaryModel.objects.all()'''
    for student in students:
        for skill in skills:
            m = TemporaryModel.objects.create(user_id=student, skill_id=skill,
            lvl=5)
            m.save()
    '''something = students.skills.all()
    #skill_list = Student.objects.order_by('-group').all#[:1]'''
    context = {'students': students} #,'smth':something}
    return render(request, 'polls/index.html', context)


def detail(request, skills):
    return HttpResponse(" %s" % skills)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




