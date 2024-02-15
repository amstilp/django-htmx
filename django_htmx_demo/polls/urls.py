from django.urls import include, path

from . import views

app_name = "polls"


urlpatterns = [
    path("<int:pk>/", views.QuestionDetail.as_view(), name="detail"),
    path("", views.QuestionList.as_view(), name="list"),
    path("vote/<int:pk>/", views.VoteCreate.as_view(), name="vote"),
]
