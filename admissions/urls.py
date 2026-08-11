from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('procedure/', views.procedure),
    path('home/', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('apply/', views.apply),
    path('scholarships/', views.scholarships),
    path('announcements/', views.announcements),
]




