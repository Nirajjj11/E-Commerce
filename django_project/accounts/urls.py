from django.urls import path
from .views import SignUpView , SellerSignUpView, ProfileView, ProfileDeleteView, ProfileUpdateView
urlpatterns = [ 
      path('signup/', SignUpView.as_view(), name='signup'),
      path('signup/seller/', SellerSignUpView.as_view(), name='seller_signup'),
      path('profile/', ProfileView.as_view(), name='profile'), 
      path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
      path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]
