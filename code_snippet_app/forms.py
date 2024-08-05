from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Snippet 


class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['language', 'description', 'code']        