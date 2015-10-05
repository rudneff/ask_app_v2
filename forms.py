from django import forms
from django.contrib.auth.forms import UserCreationForm
from ask_app.models import *


class CreateUserForm(UserCreationForm):
    avatar = forms.ImageField()


class CreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['header', 'body', 'tags']


class CreateAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
