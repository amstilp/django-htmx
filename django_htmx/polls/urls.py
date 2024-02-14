from django.urls import include, path

from . import views

app_name = "polls"


urlpatterns = [
    path("<int:pk>/", views.QuestionDetail.as_view(), name="detail"),
]
