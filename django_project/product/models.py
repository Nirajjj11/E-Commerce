from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

# PRODUCT MODELS (Seller Side)
class Product(models.Model):
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
      
      # Link product to a specific user who acts as the seller 
      seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
      
      name = models.CharField(max_length=200)
      description = models.TextField(max_length=1000)
      category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
      sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY_CHOICES)
      stocks = models.PositiveIntegerField(default=100)
      created_at = models.DateTimeField(auto_now_add=True)
      image = models.ImageField(upload_to='product_images', blank=True, null=True)
      
      marked_price = models.DecimalField(max_digits=10, decimal_places=2)
      discounts = models.PositiveIntegerField(default=0, help_text="Enter percentage (e.g., 10 for 10%)")
      
      actual_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
      
      def save(self, *args, **kwargs):
            # Calculate actual_price: Marked Price - (Marked Price * Discount / 100)
            discount_amount = (self.marked_price * self.discounts) / 100
            self.actual_price = self.marked_price - discount_amount
            super().save(*args, **kwargs)
            
      def __str__(self):
            return self.name
      
      def get_absolute_url(self):
            return reverse("product_detail", kwargs= {"pk": self.pk})