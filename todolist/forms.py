from django.forms import DateInput, ModelForm
from todolist.models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']