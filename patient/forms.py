from django import forms
from .models import Doctor

class UpdateDocForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['profile_photo', 'first_name','last_name', 'hospital', 'email','title','phone_number']