from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    skill_list = Student.objects.order_by('-group').all
    context = {'skill_list': skill_list}
    return render(request, 'testing.html', context)

def email(email):
	return HttpResponse("You can write this student at  %s" % email)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

###
from django.contrib.auth.decorators import login_required
from .models import Student
from skill_db.filters import StudentFilter

#@login_required(login_url='accounts/login/')
def student_list(request):
    students=Student.objects.all()
    filter=StudentFilter(request.GET, queryset=students)
    context={'filter':filter}
    return render(request, 'skill_db/filter_result.html', context)

