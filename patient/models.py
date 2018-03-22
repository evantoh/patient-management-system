from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    title = models.CharField(max_length=20, null=True, default = 'Dr')
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.IntegerField(null=True, default=0)
    specialty = models.CharField(max_length=200, default='Physician')
    hospital = models.CharField(max_length=200, default='kikuyu Hospital')
    profile_photo = models.ImageField(upload_to='doc_profiles/', default='doc_profiles/no-image.jpg')
    user = models.ForeignKey(User, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['first_name']


class Patient(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField(default=254)
    gender = models.CharField(max_length=6)
    id_number = models.IntegerField(default=0)
    status = models.CharField(max_length=8)
    email = models.EmailField()
    blood_group = models.CharField(max_length=5)
    doctor = models.ForeignKey(Doctor, null=True)
    profile_photo = models.ImageField(upload_to='patients_photo/', null=True)


    def __str__(self):
            return self.first_name

    class Meta:
        ordering = ['first_name']



class Treatment(models.Model):
    patient = models.ForeignKey(Patient, null=True)
    doctor = models.ForeignKey(Doctor, null=True)
    cash_charged = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    symptoms = models.CharField(max_length=500, null=True)
    diagnosis = models.CharField(max_length=1000)
    recommendations = models.CharField(max_length=1000, null=True)

    class Meta:
        ordering = ['-date']

