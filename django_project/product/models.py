from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

# PRODUCT MODELS (Seller Side)
class Product(models.Model):
      
      # Link product to a specific user who acts as the seller 
      seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
      
      name = models.CharField(max_length=200)
      description = models.TextField(max_length=500)
      category = models.TextField(max_length=100)
      sub_category = models.TextField(max_length=100)
      actual_price = models.DecimalField(max_digits=10, decimal_places=2)
      marked_price = models.DecimalField(max_digits=10, decimal_places=2)
      stocks = models.PositiveIntegerField(default=100)
      created_at = models.DateTimeField(auto_now_add=True)
      image = models.ImageField(upload_to='product_images', blank=True, null=True)
      
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
