from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from ask_app.models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']


class ChangeUserForm(UserCreationForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        exclude = ['rating']


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['header', 'body', 'tags']


class CreateAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['rating']
