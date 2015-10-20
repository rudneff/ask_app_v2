from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView, CreateView, FormView
from ask_app.models import *
from ask_app.forms import *


# class for template
class AskAppTemplateView(TemplateView):
    template_name = 'base.html'

    # edit this func to see popular users ans tags
    def get_context_data(self, **kwargs):
        data = super(AskAppTemplateView, self).get_context_data(**kwargs)
        #  edit here
        data['best_users'] = User.objects.all()[:5]
        data['tags'] = Tags.objects.all()[:5]
        return data


# classes for working with Question models


# show all questions
class QuestionListView(ListView):
    model = Question
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super(QuestionListView, self).get_context_data(**kwargs)
        data['best_users'] = User.objects.all()[:5]
        data['tags'] = Tags.objects.all()[:3]
        return data


# create one question
class QuestionCreateView(CreateView):
    model = Question
    form_class = CreateQuestionForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        data = super(QuestionCreateView, self).get_context_data(**kwargs)
        #  edit here
        data['best_users'] = User.objects.all()[:5]
        data['tags'] = Tags.objects.all()[:5]
        return data

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreateView, self).form_valid(form)


# see one question
class QuestionDetailView(DetailView):
    model = Question
    success_url = reverse_lazy('home-page')


# update one question
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
    form_class = CreateAnswer
    template_name_suffix = '_create_form'


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

# classes for working with Users models


# display all elements
class UserListView(ListView):
    model = User


# create new user / registration
class UserCreateView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('home-page')

    # function for auto login after creating new user
    def form_valid(self, form):
        valid = super(UserCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def get_context_data(self, **kwargs):
        data = super(UserCreateView, self).get_context_data(**kwargs)
        #  edit here
        data['best_users'] = User.objects.all()[:5]
        data['tags'] = Tags.objects.all()[:5]
        return data


# see one user
class UserDetailView(DetailView):
    model = User


# change one user
class UserUpdateView(UpdateView):
    model = User
    form_class = ChangeUserForm
    template_name_suffix = '_update_form'


# delete one user
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('home-page')
