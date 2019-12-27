from django import forms
from .models import *

class QAForm(forms.ModelForm):
    class Meta:
        model=questionanswer

        exclude=()