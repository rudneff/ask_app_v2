from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView
from ask_app.models import *

# class for template
class AskAppTemplateView(TemplateView):
    template_name = 'base.html'

# classes for working with Question models
class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question


class QuestionUpdateView(UpdateView):
    model = Question
    template_name_suffix = '_update_form'


class QuestionDeleteView(DeleteView):
    model = Question

# classes for working with Answers models
class AnswerListView(ListView):
    model = Answer


class AnswerDetailView(DetailView):
    model = Answer


class AnswerUpdateView(UpdateView):
    model = Answer
    template_name_suffix = '_update_form'


class AnswerDeleteView(DeleteView):
    model = Answer

