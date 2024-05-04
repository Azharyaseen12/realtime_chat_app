from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('register/', views.register , name = 'register'),
    path('user_login/', views.user_login , name = 'user_login'),


    path('personal_chat/<int:pk>/', views.personel_chat , name = 'personal_chat'),
    
]