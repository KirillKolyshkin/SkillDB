from django.shortcuts import render, redirect
from .models import Students, Skills, StudentSkills
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request,'skill_db/signup.html',{'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the useh
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'skill_db/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required(login_url="login")
def student_detail_view(request, user):
    student = Students.objects.get(user=user)
    render(request, 'skill_db/student_detail.html', {'student': student})


@login_required(login_url="login")
def search_result_view(request):
    students = Students.objects.all()
    skills = Skills.objects.all()
    for student in students:
        for skill in skills:
            m = StudentSkills.objects.create(user_id=student, skill_id=skill,
            lvl=5)
            m.save()
    return render(request, 'skill_db/search_result.html', {'students': students})


# @login_required(login_url="login")
def search_skills_view(request):
    return render(request, 'skill_db/search_skills.html')

@login_required(login_url="login")
def student_profile_view(request):
    return render(request, 'skill_db/student_profile.html')
