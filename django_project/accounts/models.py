from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
      GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
      ]

      age = models.PositiveIntegerField(null=True, blank=True)
      mobile_no = models.CharField(max_length=15, null=True, blank=True)
      email = models.EmailField(unique=True, null=False, blank=False)
      gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
      
      # Address Category Fields
      city_village = models.CharField(max_length=100, null=True, blank=True)
      state = models.CharField(max_length=100, null=True, blank=True)
      country = models.CharField(max_length=100, default="India")
      pincode = models.CharField(max_length=10, null=True, blank=True)

      def __str__(self):
            return self.username