from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('search_skills/', views.SearchSkillsPageView.as_view(), name='search_skills'),
    path('search_result/', views.SearchResultPageView.as_view(), name='search_result'),
    path('temp_profile/', views.TempProfilePageView.as_view(), name='temp_profile'),

]