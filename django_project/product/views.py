from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView,UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Product, Order, OrderItems, OrderItemTracking
# Create your views here.
class ProductListView(ListView):
      model = Product
      template_name = 'product/product_list.html'
      context_object_name = "products"
      
      def get_queryset(self):
            return Product.objects.all().order_by('-created_at')