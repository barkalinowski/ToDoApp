from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
	task_name = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Add your task here'}))
	class Meta:
		model = Task
		fields = "__all__"