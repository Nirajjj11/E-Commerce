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
      seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
      
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
      

# ORDER MODEL (Buyer Side) 
class Order(models.Model):
      # link order to the user who is buying
      buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
      created_at = models.DateTimeField(auto_now_add=True)
      is_returned = models.BooleanField(default=False)
      is_shipped = models.BooleanField(default=False, null=True)
      shipping_address = models.TextField(blank=True, null=True)
      
      # will include if we give the payment 
      # is_paid = models.BooleanField(default=False)

# ORDER ITEMS (the junction table with logistic Status)
class OrderItems(models.Model): 
      STATUS_CHOICES = [
            ("OREDER_ACCEPTED","Order Accepted"),
            ("PROCESSING", "Processing/Packing"),
            ("SHIPPED", "Shipped"),
            ("IN_TRANSIT","In Transit"),
            ("DELEVERED", "Delivered"),
            ("CANCELLED","Cancelled"),
            ("RETURNED","Returned"),
            
      ]           
      order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity = models.PositiveIntegerField(default=1)
      price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
      
      # Logistics Status
      status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
      tracking_id = models.CharField(max_length=100, blank=True, null=True)
      last_update = models.DateTimeField(auto_now=True)
      
      def __str__(self):
            return f"{self.product.name} ({self.quantity} - {self.status})"

# TRACKING LOGS (Timeline for Logistics)
class OrderItemTracking(models.Model):
      item = models.ForeignKey(OrderItems, on_delete=models.CASCADE, related_name='logs')
      status = models.CharField(max_length=20, choices=OrderItems.STATUS_CHOICES)
      timestamp = models.DateTimeField(auto_now_add=True)
      notes = models.CharField(max_length=100, blank=True, null=True)

      class Meta:
            ordering = ['-timestamp']
      
      def __str__(self):
            return f"{self.item.product.name} moved to {self.status} at {self.timestamp}"
