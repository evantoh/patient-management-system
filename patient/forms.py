from django import forms
from .models import Doctor,Patient

class UpdateDocForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['profile_photo', 'first_name','last_name', 'hospital', 'email','title','phone_number']

class addPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['profile_photo', 'first_name','last_name', 'date_of_birth', 'email','phone_number','phone_number']