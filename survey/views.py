from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy

from .models import Question, Option
from .forms import OptionFormSet

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    paginate_by = 2

def question_list(request):
    object_list = Question.objects.all()
    paginator = Paginator(object_list, 3)
    # No Pagina, siempre devuelve pagina 1. Habría que pasarle la página mediante la URL
    page_obj = paginator.page(1)
    context = {
        'object_list': object_list,
        'page_obj': page_obj
    }
    return render(request, 'survey/question_list.html', context=context)

class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['text']
    success_url = reverse_lazy('survey:question_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
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
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['text']
    success_url = reverse_lazy('survey:question_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = OptionFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = OptionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            form.instance.updated_by = self.request.user
            self.object = form.save()

            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('survey:question_list')








#class QuestionCreateView(LoginRequiredMixin, CreateView):
'''
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
'''
