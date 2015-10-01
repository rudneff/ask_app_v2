from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView

class AskAppTemplateView(TemplateView):
    template_name = 'base.html'
