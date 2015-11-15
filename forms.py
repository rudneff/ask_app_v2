from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.forms.widgets import ClearableFileInput
from ask_app.models import *


class CreateUserForm(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ChangeUserForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=ClearableFileInput)
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        exclude = ['rating']


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['header', 'body', 'tags']


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
