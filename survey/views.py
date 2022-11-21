from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.forms import modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question, Option


class QuestionListView(ListView):
    model = Question


#class QuestionCreateView(LoginRequiredMixin, CreateView):
class QuestionCreateView(CreateView):
    model = Question
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = modelformset_factory(Option, fields=['text'])
        return context
