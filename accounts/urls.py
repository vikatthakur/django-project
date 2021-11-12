from django.urls import path
from . import views

urlpatterns = [
    path('login', view=views.login, name='login'),
    path('logout', view=views.logout, name='logout'),
    path('register', view=views.register, name='register'),
    path('dashboard', view=views.dashboard, name='dashboard') 
]