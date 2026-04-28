# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser 

class CustomUserAdmin(UserAdmin): 
      add_form = CustomUserCreationForm 
      form = CustomUserChangeForm 
      model = CustomUser 
      
      # 1. Added 'is_approved_seller' to list_display so you can see status at a glance
      # 2. Added 'list_editable' so you can approve sellers directly from the list page
      list_display = ["username", "email", "mobile_no", "is_approved_seller", "is_staff"] 
      list_editable = ["is_approved_seller"] 
      list_filter = UserAdmin.list_filter + ("is_approved_seller",)
      
      # Add the approval field to the Edit page
      fieldsets = UserAdmin.fieldsets + (
            ("Seller Status", {"fields": ("is_approved_seller",)}),
            ("Additional Info", {"fields": ("age", "gender", "mobile_no")}),
            ("Address Details", {"fields": ("city_village", "state", "country", "pincode")}),
      )
      
      # Ensure it's available when creating a user via Admin
      add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {"fields": ("email", "is_approved_seller")}),
            ("Personal Info", {"fields": ("age", "gender", "mobile_no")}),
            ("Address", {"fields": ("city_village", "state", "country", "pincode")}),
      )

admin.site.register(CustomUser, CustomUserAdmin)