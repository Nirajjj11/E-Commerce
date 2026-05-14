from django.views.generic import TemplateView
from product.models import Product
from django.contrib import messages
from product.models import Product
from orders.models import Order, OrderItems, OrderItemTracking
from django.contrib.auth.mixins import LoginRequiredMixin
from commerce.models import WishList, Cart

class DashboardView(LoginRequiredMixin, TemplateView):
      template_name = 'dashboard.html'

class UserDashboardView(LoginRequiredMixin, TemplateView):
      template_name = "main_content.html"
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user
            # -------------------------
            # SUPER ADMIN DASHBOARD
            # -------------------------
            if user.is_superuser:
                  context["total_users"] = user.__class__.objects.count()
                  context["total_products"] = Product.objects.count()
                  context["total_orders"] = Order.objects.count()
                  context["recent_orders"] = Order.objects.all().order_by("-created_at")[:10]
                  
            # -------------------------
            # SELLER DASHBOARD
            # -------------------------
            elif user.is_approved_seller:
                  seller_products = Product.objects.filter( seller=user )
                  seller_order_items = OrderItems.objects.filter( product__seller=user)
                  total_sales = 0

                  for item in seller_order_items:
                        total_sales += item.price_at_purchase * item.quantity

                  context["products"] = seller_products
                  context["orders"] = seller_order_items
                  context["total_sales"] = total_sales
                  context["total_products"] = seller_products.count()
                  context["pending_orders"] = seller_order_items.filter(status="PROCESSING").count()
                  context["delivered_orders"] = seller_order_items.filter(status="DELEVERED").count()

            # -------------------------
            # NORMAL USER DASHBOARD
            # -------------------------
            else:
                  context["wishlist"] = WishList.objects.filter(user=user)
                  context["cart"] = Cart.objects.filter(user=user)
                  context["orders"] = Order.objects.filter(buyer=user).order_by("-created_at")

            return context

