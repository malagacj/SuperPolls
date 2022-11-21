from django.urls import include, path
from django.views.generic.base import RedirectView, TemplateView
from . import views

app_name = 'survey'

urlpatterns= [
    path('', RedirectView.as_view(url='question/create/'), name='index'),

    # Question
    path(
        'question/',
        views.QuestionListView.as_view(),
        name='question_list'
    ),
    path(
        'question/create/',
        views.QuestionCreateView.as_view(),
        name='question_create'
    )
 ]
