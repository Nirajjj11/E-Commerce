from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class OrderListView(LoginRequiredMixin, ListView):
      model = Order
      template_name = 'orders.html'
      context_object_name = 'orders'
      
      def get_queryset(self):
            return Order.objects.filter(buyer = self.request.user).prefetch_related("items").order_by("-created_at")
      
class TrackOrderView(LoginRequiredMixin, DetailView):
      model = OrderItems
      template_name = "tracking.html"
      context_object_name = "item"
