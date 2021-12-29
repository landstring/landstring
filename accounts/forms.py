from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import Textarea

from .models import Comments

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.Form):
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows' : '5', 'cols' : '133'} ))

class CreateIdeaForm(forms.Form):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows' : '20', 'cols' : '120'} ))

class CreateStageForm(forms.Form):
	name = forms.CharField(max_length=80)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows' : '20', 'cols' : '120'} ))

class CreateTaskForm(forms.Form):
	name = forms.CharField(max_length=80)

class CreateProjectForm(forms.Form):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows' : '20', 'cols' : '120'} ))

class CreateApplication(forms.Form):
	options = (
		(1, "Ведущий программист"),
		(2, "Креативный директор"),
		(3, "Главный менеджер"),
		(4, "Программист"),
		(5, "Менеджер"),
	)
	team = forms.CharField(max_length=100)
	role = forms.TypedChoiceField(widget=forms.RadioSelect,
										 choices=options)