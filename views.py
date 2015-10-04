from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView, CreateView
from ask_app.models import *

# class for template
class AskAppTemplateView(TemplateView):
    template_name = 'base.html'

# classes for working with Question models

# show all questions
class QuestionListView(ListView):
    model = Question


# create one question
class QuestionCreateView(CreateView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question
    success_url = reverse_lazy('home-page')


class QuestionUpdateView(UpdateView):
    model = Question
    template_name_suffix = '_update_form'


class QuestionDeleteView(DeleteView):
    model = Question

# classes for working with Answers models

# display all elements
class AnswerListView(ListView):
    model = Answer


# create new answer
class AnswerCreateView(CreateView):
    model = Answer

# see one answer
class AnswerDetailView(DetailView):
    model = Answer

# change one answer
class AnswerUpdateView(UpdateView):
    model = Answer
    template_name_suffix = '_update_form'

# delete one answer
class AnswerDeleteView(DeleteView):
    model = Answer
    success_url = reverse_lazy('home-page')

