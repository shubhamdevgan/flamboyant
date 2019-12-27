from django import forms

from .models import *

class BidForm(forms.ModelForm):
    class Meta:
        model=Bid
        exclude=()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['by_user'].widget = forms.HiddenInput()
        self.fields['on_project'].widget = forms.HiddenInput()
