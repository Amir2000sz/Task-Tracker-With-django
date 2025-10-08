from django import forms
from .models import Task

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','isDone']
        widgets = {
            'isDone': forms.CheckboxInput(attrs={
                'style': 'margin-right:6px; vertical-align:middle;',
            }),
            }
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
    