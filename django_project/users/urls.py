from django.urls import path
from .views import *

urlpatterns = [

      path("", UserDashboardView.as_view(), name="user_dashboard"),

      # path("wishlist/", WishlistView.as_view(), name="wishlist"),

      # path("cart/", CartView.as_view(), name="cart"),

      # path("orders/", OrderHistoryView.as_view(), name="order_history"),

      # path("tracking/<int:pk>/", OrderTrackingView.as_view(), name="tracking"),

]