from django import forms
from .models import Mytodo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task',]
