

#from typing import ContextManager
from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout as django_logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm 

#insertJobs

def index(request):

  return render(request, 'index.html')
 # return HttpResponse("this is a home page")

@login_required(login_url='login')
def jobs(request):
  return render(request, 'jobs.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

#Registration
def registerPage(request):
  if request.user.is_authenticated:
    return redirect('forms')
  if request.user.is_authenticated:
    return redirect('home')
  else:
    form = CreateUserForm()
    if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

#Login
def loginPage(request):
  if request.user.is_authenticated:
    if request.user.is_staff:
      return redirect('forms')
    else:
      return redirect('home')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        if user.is_staff:
          auth.login(request,user)
          return redirect('forms')
        else:
          auth.login(request, user)
          return redirect('home')
      else:
        messages.info(request, 'Username OR Password is incorrect')
    
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logout(request):
  django_logout(request)
  return redirect('/login')

#Staff-forms(forms.html)
@login_required(login_url='login')
def forms(request):
  displayjobs = JobDetail.objects.all()
  if request.user.is_authenticated:
    return render(request, 'forms.html', { 'JobDetail': displayjobs })
  else:
    return redirect('login')


