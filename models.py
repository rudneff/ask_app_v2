from django.db import models
from django.contrib.auth.models import User


class User(User):
    # made this field not required
    avatar = models.ImageField(blank=True, null=True)


class Tags(models.Model):
    text = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.text


class Question(models.Model):
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    date = models.DateField()
    tags = models.ManyToManyField(Tags)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.header


class Answer(models.Model):
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    which_question = models.ForeignKey(Question)
    date = models.DateField()
    flag = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.body
