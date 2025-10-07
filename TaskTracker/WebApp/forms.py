from django import forms
from .models import Task

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','isDone']
