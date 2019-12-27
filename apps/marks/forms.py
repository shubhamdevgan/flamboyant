from django import forms
from .models import *

class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks

        exclude=()