from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", 'name', "author", "description")
    
    
    def save(self, commit=True, **kwargs):
        m = super(CustomUserCreationForm, self).save(commit=True)
        reader_group = Group.objects.get(name="reader")
        m.groups.add(reader_group)
        m.save()
        return m



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput()

 