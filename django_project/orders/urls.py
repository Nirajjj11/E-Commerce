from django.urls import path
from .views import *

urlpatterns = [
      path("",OrderListView.as_view(), name='order'),
      
]