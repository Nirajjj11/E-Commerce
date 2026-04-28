from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView,UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Product, Order, OrderItems, OrderItemTracking
from django.urls import reverse_lazy, reverse

# Create your views here.
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
      
class ProductCreateView(LoginRequiredMixin,CreateView):
      model = Product
      template_name = "product_form.html"
      fields = ['name','description','category','sub_category','stocks','image','marked_price','discounts']
      success_url = reverse_lazy('home')
      
      def form_valid(self, form):
            form.instance.seller = self.request.user
            return super().form_valid(form)
      
class ProductUpdateView(LoginRequiredMixin, UpdateView):
      model = Product
      template_name = "product_update.html"
      fields = ['name', 'description', 'category', 'sub_category', 'stocks', 'image', 'marked_price', 'discounts']

      # Security check: Only the owner can edit
      def test_func(self):
            product = self.get_object()
            return self.request.user == product.seller

      def get_success_url(self):
            return reverse('product_detail', kwargs={'pk': self.object.pk})
      