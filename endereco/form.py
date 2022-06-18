from django.forms import ModelForm
from django import forms 
from .models import CEP

class UploadForm(ModelForm):
	cep = forms.TextInput()
	endereco = forms.ImageField()
	class Meta:
		model = CEP
		fields= ['cep','endereco']
