from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("jobs/", views.jobs, name='jobs'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),

    path("register/", views.registerPage, name='register'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logout, name='logout'),
    
    path("forms/", views.forms, name='forms'),
     
]
