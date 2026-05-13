from django.urls import path
from .views import *

urlpatterns = [

      path("", UserDashboardView.as_view(), name="user_dashboard"),
      path("wishlist/", WishListView.as_view(), name="wishlist"),
      path("wishlist/add/<int:pk>/", AddToWishlistView.as_view(),name="add_to_wishlist"),
      path("wishlist/remove/<int:pk>/",RemoveFromWishlistView.as_view(),name="remove_from_wishlist"),
      path("cart/add/<int:pk>/", AddToCartView.as_view(),name="add_to_cart"),

]