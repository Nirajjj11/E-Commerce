from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class OrderListView(LoginRequiredMixin, ListView):
      model = Order
      template_name = 'orders.html'
      context_object_name = 'order_list'
      
      def get_queryset(self):
            return Order.objects.filter(buyer = self.request.user).order_by("-created_at")
      
class CreateOrders(LoginRequiredMixin, View):

      def post(self, request):

            order = Order.objects.create(
                  buyer=request.user
            )

            return render(
                  request,
                  "success.html",
                  {"order": order}
            )