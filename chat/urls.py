from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),   
    path('register/', views.register , name = 'register'),
    path('user_login/', views.user_login , name = 'user_login'),


    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]