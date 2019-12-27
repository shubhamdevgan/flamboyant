from django import forms
from .models import *

class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        exclude=()