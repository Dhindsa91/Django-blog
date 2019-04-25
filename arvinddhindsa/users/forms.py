from django import forms
from django.contrib.auth.forms import UserCreationForm #Django Forms
from django.contrib.auth.models import User #Django Users

class UserRegistrationForms(UserCreationForm):
    email = forms.EmailField()