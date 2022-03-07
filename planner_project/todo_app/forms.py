from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
	class Meta:
		model = TodoModel
		widgets = {
				'task': forms.Textarea(attrs={'rows':2, 'cols':24}),
				'note': forms.Textarea(attrs={'rows':1, 'cols':24}),
			}
		exclude = ['timestamp','user']