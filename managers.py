from django.db import models


class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by('-rating')

    def newest(self):
        return self.order_by('-date')

    # TODO: add sort by tag
    # def findByTag(self):
    #     return self.filter()
