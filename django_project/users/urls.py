from django.urls import path
from .views import *

urlpatterns = [
      path("", UserDashboardView.as_view(), name="user_dashboard"),
      path("wishlist/", WishListView.as_view(), name="wishlist"),
      # path("wishlist/add/<int:pk>/", AddToWishlistView.as_view(),name="add_to_wishlist"),
      path("wishlist/toggle/<int:pk>/",ToggleWishlistView.as_view(),name="toggle_wishlist"),
      path("wishlist/remove/<int:pk>/",RemoveFromWishlistView.as_view(),name="remove_from_wishlist"),
      path("cart/", CartView.as_view(), name="cart"),
      path("cart/add/<int:pk>/", AddToCartView.as_view(),name="add_to_cart"),
      path("cart/remove/<int:pk>/",RemoveFromCartView.as_view(),name="remove_from_cart"),
      path("cart/increase/<int:pk>/",IncreaseCartQuantityView.as_view(),name="increase_cart_quantity"),
      path("cart/decrease/<int:pk>/",DecreaseCartQuantityView.as_view(),name="decrease_cart_quantity"),
      path("apply-coupon/",ApplyCouponView.as_view(),name="apply_coupon"),
      path("checkout/",CheckoutView.as_view(),name="checkout"),

]