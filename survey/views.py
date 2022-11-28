from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from .models import Question, Option
from .forms import OptionFormSet


class QuestionListView(ListView):
    model = Question


#class QuestionCreateView(LoginRequiredMixin, CreateView):
class QuestionCreateView(CreateView):
    model = Question
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OptionFormSet(self.request.POST)
        else:
            context['formset'] = OptionFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            form.instance.created_by = self.request.user
            form.instance.updated_by = self.request.user
            self.object = form.save()

            if formset.is_valid():
                formset.instance= self.object
                formset.save()
        return super().form_valid(form)
