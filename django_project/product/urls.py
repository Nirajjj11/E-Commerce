from django.urls import path
from .views import *

urlpatterns = [
      path("",ProductListView.as_view(), name='home'),
      path("product/<int:pk>", ProductDetailView.as_view(), name='product_detail'),
      path("product/new/",ProductCreateView.as_view(), name="product_create"),
      path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
      path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]