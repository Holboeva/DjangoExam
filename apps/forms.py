from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, Form
from django.forms.fields import CharField

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = 'first_name', 'email', 'username', 'password'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password = make_password(password)
        return password


class LoginForm(Form):
    username = CharField(max_length=255)
    password = CharField(max_length=255)


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = 'email', 'phone_number',
