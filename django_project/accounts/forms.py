from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
            model = CustomUser
            # We explicitly list the fields to ensure they are captured from the POST request
            fields = UserCreationForm.Meta.fields + (
                  'email', 'age', 'gender', 'mobile_no', 
                  'city_village', 'state', 'country', 'pincode',
            )

class CustomUserChangeForm(UserChangeForm): 
      class Meta: 
            model = CustomUser 
            fields = ('username', 'email', 'age', 'gender', 'mobile_no', 'city_village', 'state', 'country', 'pincode')