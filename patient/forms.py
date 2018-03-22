from django import forms
from .models import Doctor,Patient,Treatment,NextOfKin,Medicine

class UpdateDocForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['profile_photo', 'first_name','last_name', 'hospital', 'email','title']

class addPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['profile_photo', 'first_name','last_name', 'email','gender']

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['cash_charged','symptoms','diagnosis','recommendations']

class NewNextOfKinForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = ['relationship','email']
class NewMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['doctor_prescribed']