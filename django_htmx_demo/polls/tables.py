import django_tables2 as tables
from django.utils.safestring import mark_safe
from . import models


class QuestionTable(tables.Table):

    pk = tables.Column(linkify=True, verbose_name="ID")
    number_of_votes = tables.Column(empty_values=())

    class Meta:
        model = models.Question
        fields = ("pk", "text",)

    def render_number_of_votes(self, record):
        return models.Vote.objects.filter(choice__question=record).count()


class QuestionTableAuthenticated(QuestionTable):

    my_votes = tables.Column(empty_values=())

    def render_my_votes(self, record):
        value = ""
        if self.request.user.is_authenticated:

            try:
                models.Choice.objects.filter(
                    question=record,
                    vote__user=self.request.user
                ).get()
                value = """<i class="bi bi-check-circle-fill"></i>"""
            except models.Choice.DoesNotExist:
                pass
        return mark_safe(value)
