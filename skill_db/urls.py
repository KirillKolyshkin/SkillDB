from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from skill_db import views
#from skill_db.views import student_list
from skill_db.filters import StudentFilter
import django_filters
from skill_db.models import Student, Staff, StudentSkills, Skill


urlpatterns = [
    path('', TemplateView.as_view(template_name='skill_db/main_page.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='skill_db/about.html'), name='about'),
    path('search_skills/', TemplateView.as_view(template_name='skill_db/search_skills.html'), name='search_skills'),
    path('search_result/', TemplateView.as_view(template_name='skill_db/search_result.html'), name='search_result'),
    path('temp_profile/', TemplateView.as_view(template_name='skill_db/temp_profile.html'), name='temp_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('search/', views.student_list, name='searcher')
    #url(r'^search/$', FilterView.as_view(filterset_class=StudentFilter, template_name='skill_db/filter_result.html'), name='searcher'),
]