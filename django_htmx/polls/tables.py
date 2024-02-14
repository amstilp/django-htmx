import django_tables2 as tables

from . import models


class QuestionTable(tables.Table):

    pk = tables.Column(linkify=True, verbose_name="ID")
    number_of_votes = tables.Column(empty_values=())

    class Meta:
        model = models.Question
        fields = ("pk", "text",)

    def render_number_of_votes(self, record):
        return models.Vote.objects.filter(choice__question=record).count()
