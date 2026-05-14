from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from product.models import *
# Create your models here.

# not done

# ORDER MODEL (Buyer Side) 
class Order(models.Model):
      # link order to the user who is buying
      PAYMENT_CHOICES = [
            ("COD", "Cash on Delivery"),
            ("ONLINE", "Online Payment"),
      ]
      buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
      created_at = models.DateTimeField(auto_now_add=True)
      
      is_shipped = models.BooleanField(default=False, null=True)
      is_returned = models.BooleanField(default=False)
      
      shipping_address = models.TextField(blank=True, null=True)
      
      subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
      delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
      platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
      total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
      
      payment_method = models.CharField( max_length=20, choices=PAYMENT_CHOICES, default="COD")
      
      order_status = models.CharField(max_length=20,default="PENDING")
      
      is_bazar_member = models.BooleanField(default=False)
      
      def __str__(self):
            return f"Order {self.order_id}"

# ORDER ITEMS (the junction table with logistic Status)
class OrderItems(models.Model): 
      STATUS_CHOICES = [
            ("PENDING", "Pending"),
            ("ORDER_ACCEPTED","Order Accepted"),
            ("PROCESSING", "Processing/Packing"),
            ("SHIPPED", "Shipped"),
            ("IN_TRANSIT","In Transit"),
            ("DELIVERED", "Delivered"),
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
