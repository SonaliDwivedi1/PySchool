from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('procedure/', views.procedure, name='procedure'),
    path('about/', views.about, name='about'),
    path('founder-message/', views.founder_message, name='founder_message'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply, name='apply'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('announcements/', views.announcements, name='announcements'),
]






