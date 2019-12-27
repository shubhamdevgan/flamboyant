from django import forms

from .models import projects

class project_form(forms.ModelForm):
    class Meta:
        model=projects
        exclude=(

        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['by_username'].widget = forms.HiddenInput()