from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from .models import WishList, Cart
from product.models import Product
from django.contrib import messages


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

# CART VIEWS
class CartView(LoginRequiredMixin, ListView):
      model = Cart
      template_name = "cart.html"
      context_object_name = "items"

      def get_queryset(self):
            return Cart.objects.filter(user=self.request.user).select_related("product").order_by("-added_at")

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            items = context["items"]
            subtotal = 0
            for item in items:
                  subtotal += item.product.actual_price * item.quantity

            context["subtotal"] = subtotal
            context["total"] = subtotal
            context["disc_amount"] = 0

            return context
      
# ADD TO CART
class AddToCartView(LoginRequiredMixin, View):
      def get(self, request, pk):
            product = get_object_or_404(Product, pk=pk)
            cart_item, created = Cart.objects.get_or_create( user=request.user, product=product)
            if not created:
                  cart_item.quantity += 1
                  cart_item.save()
            return redirect("cart")
      
# DELETE FROM CART
class RemoveFromCartView(LoginRequiredMixin, View):
      def get(self, request, pk):
            cart_item = get_object_or_404(Cart,pk=pk,user=request.user)
            cart_item.delete()
            return redirect("cart")

class IncreaseCartQuantityView(LoginRequiredMixin, View):
      def post(self, request, pk):
            cart_item = get_object_or_404(Cart,pk=pk,user=request.user)
            cart_item.quantity += 1
            cart_item.save()
            return redirect("cart")

class DecreaseCartQuantityView(LoginRequiredMixin, View):
      def post(self, request, pk):
            cart_item = get_object_or_404(Cart,pk=pk,user=request.user)

            if cart_item.quantity > 1:
                  cart_item.quantity -= 1
                  cart_item.save()
            else:
                  cart_item.delete()

            return redirect("cart")
# APPLY COUPEN
class ApplyCouponView(LoginRequiredMixin, View):
      def post(self, request):
            coupon_code = request.POST.get("coupon_code")
            # Example logic
            if coupon_code == "SAVE10":
                  request.session["discount"] = 10
                  messages.success(request, "Coupon Applied Successfully")
            else:
                  messages.error(request, "Invalid Coupon")

            return redirect("cart")

# CHECKOUT VIEWS
class CheckoutView(LoginRequiredMixin, View):
      template_name = "checkout.html"
      def get(self, request):
            cart_items = Cart.objects.filter(user=request.user)
            subtotal = sum(item.product.price * item.quantity for item in cart_items )

            # Charges
            delivery_charge = 0 if subtotal > 500 else 40
            platform_fee = 10

            # Membership logic
            is_member = False

            if is_member:
                  delivery_charge = 0
                  platform_fee = 0

            disc_amount = 0

            total = (
                  subtotal
                  + delivery_charge
                  + platform_fee
                  - disc_amount
            )

            context = {
                  "items": cart_items,
                  "subtotal": subtotal,
                  "delivery_charge": delivery_charge,
                  "platform_fee": platform_fee,
                  "disc_amount": disc_amount,
                  "total": total,
                  "is_member": is_member,
            }

            return render(
                  request,
                  self.template_name,
                  context
            )

      def post(self, request):
            payment_method = request.POST.get("payment_method")
            print(payment_method)
            # order creation logic here
            return render(request,self.template_name)