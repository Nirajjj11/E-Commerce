from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from .models import WishList, Cart
from product.models import Product



class UserDashboardView(LoginRequiredMixin, TemplateView):
      template_name = "dashboard.html"

class WishListView(LoginRequiredMixin, ListView):
      model = WishList
      template_name = "wishlist.html"
      context_object_name = "wishlist_items"

      def get_queryset(self):
            return WishList.objects.filter(
                  user=self.request.user
            ).select_related("product").order_by("-added_at")
      
# Add to wishlist
class AddToWishlistView(LoginRequiredMixin, View):
      def get(self, request,pk):
            product = get_object_or_404(Product, pk=pk)
            wishlist_item , created = WishList.objects.get_or_create(user = request.user, product = product)
            return redirect("wishlist")
      
# REMOVE FROM WISHLIST
class RemoveFromWishlistView(LoginRequiredMixin, View):
      def get(self, request, pk):
            wishlist_item = get_object_or_404( WishList,pk=pk, user=request.user
            )
            wishlist_item.delete()
            return redirect("wishlist")

# ADD TO CART
class AddToCartView(LoginRequiredMixin, View):
      def get(self, request, pk):
            product = get_object_or_404(Product, pk=pk)
            cart_item, created = Cart.objects.get_or_create( user=request.user, product=product)
            if not created:
                  cart_item.quantity += 1
                  cart_item.save()
            return redirect("cart")