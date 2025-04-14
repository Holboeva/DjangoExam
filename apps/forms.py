from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = 'first_name', 'email', 'username', 'password1', 'password2',

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = 'email', 'password'