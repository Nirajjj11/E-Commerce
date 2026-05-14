from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItems

from .forms import OrderStatusUpdateForm
from .models import OrderItemTracking

from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import DetailView
from .models import OrderItems


class OrderListView(LoginRequiredMixin, ListView):
      model = Order
      template_name = "orders.html"
      context_object_name = "orders"

      def get_queryset(self):

            # SELLER VIEW
            if self.request.user.is_approved_seller:

                  return Order.objects.filter(
                        items__product__seller=self.request.user
                  ).distinct().prefetch_related(
                        "items",
                        "items__product",
                        "items__product__seller"
                  ).order_by("-created_at")

            # BUYER VIEW
            return Order.objects.filter(
                  buyer=self.request.user
            ).prefetch_related(
                  "items",
                  "items__product",
                  "items__product__seller"
            ).order_by("-created_at")


class TrackOrderView(LoginRequiredMixin, DetailView):
      model = OrderItems
      template_name = "tracking.html"
      context_object_name = "item"

      def post(self, request, *args, **kwargs):

            self.object = self.get_object()

            # SELLER STATUS UPDATE
            if request.user.is_approved_seller:

                  status = request.POST.get("status")
                  notes = request.POST.get("notes")

                  OrderItemTracking.objects.create(
                        item=self.object,
                        status=status,
                        notes=notes
                  )

                  self.object.status = status
                  self.object.save()

                  messages.success(request, "Order status updated")

            # USER REVIEW
            else:

                  rating = request.POST.get("rating")
                  review = request.POST.get("review")

                  print(rating, review)

                  messages.success(request, "Review submitted")

            return redirect("tracking", pk=self.object.id)