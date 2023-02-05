from django.urls import include, path
from django.views.generic.base import RedirectView, TemplateView
from . import views

app_name = 'survey'

urlpatterns= [
    path('', RedirectView.as_view(url='question/'), name='index'),

    # Question
    path(
        'question/',
        views.QuestionListView.as_view(),
        name='question_list'
    ),
        path(
        'question_f/',
        views.question_list,
        name='question_f_list'
    ),
    path(
        'question/<int:pk>/',
        views.QuestionDetailView.as_view(),
        name='question_detail'
    ),
    path(
        'question/create/',
        views.QuestionCreateView.as_view(),
        name='question_create'
    ),
    path(
        'question/<int:pk>/update/',
        views.QuestionUpdateView.as_view(),
        name='question_update'
    ),
    path(
        'question/<int:pk>/delete/',
        views.QuestionDeleteView.as_view(),
        name='question_delete'
    ),
 ]
