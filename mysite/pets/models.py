from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Pet(models.Model):
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight_in_pounds = models.IntegerField(null=True)
    Owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name

class Appointment(models.Model):
    date_of_appointment = models.DateField(default=datetime.now)
    duration_minutes = models.IntegerField(null=True)
    special_instructions = models.CharField(max_length=500)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
      return str(self.pet)