# forms.py
from django import forms
from .models import *
class PatientForm(forms.ModelForm):

	class Meta:
		model = Pat
		fields = ['Description', 'prescription','OtherAtachment']
