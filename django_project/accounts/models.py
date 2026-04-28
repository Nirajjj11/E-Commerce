from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
      GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
      ]
      CATEGORY_CHOICES = [
            ("ELECTRONICS", "Electronics"),
            ("CLOTHING", "Clothing"),
            ("HOME_KITCHEN", "Home & Kitchen"),
            ("BEAUTY", "Beauty"),
            ("SPORTS", "Sports"),
            ("BOOKS", "Books"),
            ("TOYS", "Toys"),
            ("AUTOMOTIVE", "Automotive"),
            ("GROCERY", "Grocery"),
            ("ACCESSORIES", "Accessories"),
      ]
      SUB_CATEGORY_CHOICES = [
            # Electronics
            ("MOBILE", "Mobile Phones"), ("LAPTOP", "Laptops"),
            # Clothing
            ("MENS_WEAR", "Men's Wear"), ("WOMENS_WEAR", "Women's Wear"),
            # Home
            ("FURNITURE", "Furniture"), ("DECOR", "Home Decor"),
            # Beauty
            ("SKINCARE", "Skincare"), ("FRAGRANCE", "Fragrance"),
            # Others
            ("EQUIPMENT", "Sports Equipment"), ("FICTION", "Fiction Books"),
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
      
      is_approved_seller = models.BooleanField(default=False)
      category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
      sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES)
      
      
      def __str__(self):
            return self.username