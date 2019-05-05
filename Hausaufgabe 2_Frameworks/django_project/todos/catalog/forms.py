from django import forms
from .models import Todo
from todos import settings

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ('name', 'deadline', 'progress',)
		name = forms.CharField(max_length=80)
		deadline = forms.DateField(input_formats=settings.DATE_FORMAT)
		progress = forms.IntegerField()
