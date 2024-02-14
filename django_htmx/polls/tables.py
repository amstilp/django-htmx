import django_tables2 as tables

from . import models


class QuestionTable(tables.Table):

    pk = tables.Column(linkify=True, verbose_name="ID")
    class Meta:
        model = models.Question
        fields = ("pk", "text",)
