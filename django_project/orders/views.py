from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *

# Create your views here.
class Order(ListView):
      models = Order
      template_name = 'orders.html'
      