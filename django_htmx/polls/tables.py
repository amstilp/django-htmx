import django_tables2 as tables

from . import models


class QuestionTable(tables.Table):
    class Meta:
        model = models.Question
        fields = ("text",)
