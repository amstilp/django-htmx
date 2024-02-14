from django.views.generic import DetailView
from django_tables2 import SingleTableView

from . import models, tables


class QuestionDetail(DetailView):
    model = models.Question
    template_name = "polls/question_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["choices"] = self.object.choice_set.all()
        vote = None
        if self.request.user.is_authenticated:
            try:
                vote = models.Choice.objects.filter(
                    question=self.object,
                    vote__user=self.request.user
                ).get()
            except models.Choice.DoesNotExist:
                pass
        context["vote"] = vote
        return context


class QuestionList(SingleTableView):
    table_class = tables.QuestionTable
    model = models.Question
    template_name = "polls/question_list.html"
