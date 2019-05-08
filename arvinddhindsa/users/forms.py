#this file was created by us to hold the form that inherts from UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm #Django Forms
from django.contrib.auth.models import User #Django Users
from .models import Profile

class UserRegistrationForm(UserCreationForm): #extends userCreationForm
    email = forms.EmailField() #default required=TRUE

    class Meta:       #the model this form is associated with, gives us nested namespace for configurations and keeps them in one place 
        model = User
        fields = ['username', 'email', 'password1', 'password2']    #fields we want and in what order 



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email'] 


class ProfileUpdateForm(forms.ModelForm):                     #User and Profile are different tables
    class Meta:
        model = Profile
        fields = ['image']

