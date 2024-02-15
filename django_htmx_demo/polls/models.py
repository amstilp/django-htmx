from django.conf import settings
from django.db import models
from django.urls import reverse


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("polls:detail", args=[self.pk])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.question.text}: {self.text}"


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} voted for {self.choice}'
