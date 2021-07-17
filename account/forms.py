from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailInput,ModelForm



class CreateUserForm(UserCreationForm):
   
    class Meta:
        model=User
        
        fields = ['username','email', 'first_name','last_name','password1','password2']
        widgets= {
            'email':EmailInput(attrs={
                'class':'email_control',
                'autocomplete':'off'
            })
        }

class GetUser(ModelForm):
    model = Task
    fields = ['username']
