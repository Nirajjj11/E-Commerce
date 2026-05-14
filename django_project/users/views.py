from django.views.generic import TemplateView
from product.models import Product
from django.contrib import messages
from product.models import Product
from orders.models import Order, OrderItems, OrderItemTracking
from django.contrib.auth.mixins import LoginRequiredMixin
from commerce.models import WishList, Cart

from django.db.models import F, Sum, DecimalField
from django.db.models.functions import Coalesce
from django.db.models import Value
from decimal import Decimal


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
                  platform_revenue = OrderItems.objects.filter(
                        status="DELIVERED"
                  ).aggregate(
                        total=Coalesce(
                              Sum("platform_earning"),
                              Decimal("0.00")
                        )
                  )["total"]
                  
                  context["total_users"] = user.__class__.objects.count()
                  context["total_products"] = Product.objects.count()
                  context["total_orders"] = Order.objects.count()
                  context['total_sellers'] = user.__class__.objects.filter(is_approved_seller=True).count()
                  context["platform_revenue"] = platform_revenue
                  context["recent_orders"] = Order.objects.all().order_by("-created_at")[:5]
                  
            # -------------------------
            # SELLER DASHBOARD
            # -------------------------
            elif user.is_approved_seller:
                  seller_products = Product.objects.filter( seller=user )
                  seller_order_items = OrderItems.objects.filter( product__seller=user).order_by("-last_update")
                  delivered_orders = seller_order_items.filter(status="DELIVERED")

                  total_sales = seller_order_items.aggregate(
                        total=Coalesce(
                              Sum(
                                    F("price_at_purchase") * F("quantity"),
                                    output_field=DecimalField(max_digits=12, decimal_places=2)
                              ),
                              Value(
                                    Decimal("0.00"),
                                    output_field=DecimalField(max_digits=12, decimal_places=2)
                              )
                        )
                  )["total"]
                              
                  low_stock_products = seller_products.filter(stocks__lt=10)
                  
                  context["products"] = seller_products
                  context["seller_orders"] = seller_order_items
                  context["total_sales"] = total_sales
                  context["total_products"] = seller_products.count()
                  context["pending_orders"] = seller_order_items.filter(product__seller=user, status="PROCESSING").count()
                  context["delivered_orders"] = seller_order_items.filter().count()
                  context["low_stock_products"] = low_stock_products.count()
                  
                  context["total_orders_received"] = seller_order_items.count()
                  context["pending_orders"] = seller_order_items.filter(status="PENDING").count()
                  context["processing_orders"] = seller_order_items.filter(status="PROCESSING").count()
                  context["shipped_orders"] = seller_order_items.filter(status="SHIPPED").count()
                  context["cancelled_orders"] = seller_order_items.filter(status="CANCELLED").count()
                  
            # -------------------------
            # NORMAL USER DASHBOARD
            # -------------------------
            else:
                  user_orders = Order.objects.filter(buyer=user, order_status="DELIVERED").order_by("-created_at")

                  total_spent = user_orders.aggregate(total=Sum("total_amount"))["total"] or 0

                  context["wishlist"] = WishList.objects.filter(user=user)
                  context["cart"] = Cart.objects.filter(user=user)
                  context["orders"] = user_orders
                  context["total_spent"] = total_spent

            return context

