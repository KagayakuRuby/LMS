from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User   # مدل خود را ایمپورت کنید

class UserRegistionFrom(UserCreationForm):
    phone = forms.CharField(max_length=11, label='شماره تلفن')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'password1', 'password2']

class UserLoginForms(AuthenticationForm):
    username = forms.CharField(max_length=11)
    password = forms.CharField(max_length=11)