from django.forms import inlineformset_factory
from .models import Question, Option

OptionFormSet = inlineformset_factory(Question, Option, fields=('text',))
