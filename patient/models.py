from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    title = models.CharField(max_length=20, null=True, default = 'Dr')
    name = models.CharField(max_length=200, default='Treat Me')
    phone_number = models.IntegerField(null=True, default=0)
    specialty = models.CharField(max_length=200, default='Physician')
    hospital = models.CharField(max_length=200, default='kikuyu Hospital')
    profile_photo = models.ImageField(upload_to='doc_profiles/', default='doc_profiles/no-image.jpg')
    user = models.ForeignKey(User, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
