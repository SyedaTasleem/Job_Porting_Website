
from django.forms  import ModelForm
#from .models import Requirement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
  
# creating a form 

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']




