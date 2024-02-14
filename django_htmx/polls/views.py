from django.views.generic import DetailView

from . import models


class QuestionDetail(DetailView):
    model = models.Question
    template_name = "polls/question_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["choices"] = self.object.choice_set.all()
        return context
