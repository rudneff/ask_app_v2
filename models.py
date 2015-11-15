import datetime
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from managers import *


class User(AbstractUser):
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, null=True)

    object = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.username


class Tags(models.Model):
    text = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.text


class Question(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    date = models.DateField(default=datetime.date.today)
    tags = models.ManyToManyField(Tags)
    rating = models.IntegerField(default=0)

    my = QuestionManager()

    def __unicode__(self):
        return self.header


class Answer(models.Model):
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    which_question = models.ForeignKey(Question)
    date = models.DateField(default=datetime.date.today)
    flag = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.body
