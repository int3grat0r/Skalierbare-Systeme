from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ('name', 'deadline', 'progress',)
		name = forms.CharField(max_length=80)
		deadline = forms.DateField()
		progress = forms.IntegerField()
