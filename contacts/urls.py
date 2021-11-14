from django.urls import path
from . import views

urlpatterns = [
    path('contact', view=views.contact, name='contact'),
]