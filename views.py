from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView
from ask_app.models import *


class AskAppTemplateView(TemplateView):
    template_name = 'base.html'


class QuestionListView(ListView):
    model = Question


class QuestionDetailView(DetailView):
    model = Question