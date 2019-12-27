from django import forms

from .models import feedback

class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback

        exclude=()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['by_user'].widget = forms.HiddenInput()
