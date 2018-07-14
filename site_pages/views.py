from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'main_page1.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RegisterPageView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class SearchSkillsPageView(TemplateView):
    template_name = 'search_skills.html'

class SearchResultPageView(TemplateView):
    template_name = 'search_result.html'

class TempProfilePageView(TemplateView):
    template_name = 'temp_profile.html'