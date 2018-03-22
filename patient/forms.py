from django import forms
from .models import Doctor,Patient,Treatment,NextOfKin,Medicine

class UpdateDocForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['profile_photo', 'first_name','last_name', 'hospital', 'email','title','phone_number']

class addPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['profile_photo', 'first_name','last_name', 'date_of_birth', 'email','phone_number','phone_number']

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['cash_charged','symptoms','diagnosis','recommendations']

class NewNextOfKinForm(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = ['relationship','phone_number','email']
class NewMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name','date_given','doctor_prescribed']