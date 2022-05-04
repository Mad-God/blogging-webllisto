from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", 'name', "author", "description")




class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput()

 