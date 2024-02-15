from django.views.generic import DetailView, View
from django.views.generic.detail import SingleObjectMixin
from django_tables2 import SingleTableView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

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


class VoteCreate(LoginRequiredMixin, SingleObjectMixin, View):

    model = models.Choice

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            vote = models.Vote.objects.get(
                user=self.request.user,
                choice__question=self.object.question,
            )
            vote.choice = self.object
        except models.Vote.DoesNotExist:
            vote = models.Vote(
                user=self.request.user,
                choice=self.object,
            )
        vote.save()
        return redirect(self.object.question.get_absolute_url())
