from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='skill_db/main_page.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='skill_db/about.html'), name='about'),
    path('egg/', TemplateView.as_view(template_name='skill_db/egg.html'), name='egg'),
    # path('search_skills/', TemplateView.as_view(template_name='skill_db/search_skills.html'), name='search_skills'),
    # path('student_profile/', TemplateView.as_view(template_name='skill_db/student_profile.html'), name='student_profile'),
    path('404/', TemplateView.as_view(template_name='skill_db/404.html'), name='404'),
    path('signup/',views.signup_view, name="signup"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('search_result/', views.search_result_view, name='search_result'),
    path('student_detail/<user>', views.student_detail_view, name="student_detail"),
    path('search_skills/', views.search_skills_view, name='search_skills'),
    path('student_profile/', views.student_profile_view, name='student_profile'),
]
