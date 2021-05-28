from django import forms
from .models import Action


class DateInput(forms.DateInput):
    input_type = 'date'


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('main', 'full', 'date')
        widgets = {
            'date': DateInput()
        }
