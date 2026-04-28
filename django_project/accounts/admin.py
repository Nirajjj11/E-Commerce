# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser 

class CustomUserAdmin(UserAdmin): 
      add_form = CustomUserCreationForm 
      form = CustomUserChangeForm 
      model = CustomUser 
      
      # Show email in the main list view
      list_display = ["username", "email", "mobile_no", "is_staff"] 
      
      # Add email to the "Personal Info" section in the edit page
      fieldsets = UserAdmin.fieldsets + (
            ("Additional Info", {"fields": ("age", "gender", "mobile_no")}),
            ("Address Details", {"fields": ("city_village", "state", "country", "pincode")}),
      )
      
      # Ensure email shows up when creating a user via Admin
      add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {"fields": ("email",)}),
            ("Personal Info", {"fields": ("age", "gender", "mobile_no")}),
            ("Address", {"fields": ("city_village", "state", "country", "pincode")}),
      )
      

admin.site.register(CustomUser, CustomUserAdmin)