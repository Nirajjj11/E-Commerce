from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Product, Order, OrderItems, OrderItemTracking

class ProductListView(ListView):
      model = Product
      template_name = 'product_list.html'
      context_object_name = "products"
      
      def get_queryset(self):
            return Product.objects.all().order_by('-created_at')
            
class ProductDetailView(DetailView):
      model = Product
      template_name = 'product_details.html'
      context_object_name = "product"

# --- SELLER PROTECTED VIEWS ---

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
      model = Product
      template_name = "product_form.html"
      fields = ['name','description','category','sub_category','stocks','image','marked_price','discounts']
      success_url = reverse_lazy('home')
      
      # Check if user is an approved seller
      def test_func(self):
            return self.request.user.is_approved_seller

      def handle_no_permission(self):
            messages.error(self.request, "You must be an approved seller to add products.")
            return redirect('home')

      def form_valid(self, form):
            form.instance.seller = self.request.user
            return super().form_valid(form)
      
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
      model = Product
      template_name = "product_update.html"
      fields = ['name', 'description', 'category', 'sub_category', 'stocks', 'image', 'marked_price', 'discounts']

      # Security check: Must be approved AND the owner
      def test_func(self):
            product = self.get_object()
            is_owner = self.request.user == product.seller
            return self.request.user.is_approved_seller and is_owner

      def handle_no_permission(self):
            messages.error(self.request, "You do not have permission to edit this product.")
            return redirect('home')

      def get_success_url(self):
            return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
      model = Product
      template_name = "product_delete.html"
      success_url = reverse_lazy('home')
      
      # Security check: Must be approved AND the owner
      def test_func(self):
            product = self.get_object()
            is_owner = self.request.user == product.seller
            return self.request.user.is_approved_seller and is_owner

      def handle_no_permission(self):
            messages.error(self.request, "You do not have permission to delete this product.")
            return redirect('home')