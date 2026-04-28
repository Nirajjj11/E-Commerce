from django.urls import path
from .views import SignUpView , SellerSignUpView
urlpatterns = [ 
      path('signup/', SignUpView.as_view(), name='signup'),
      path('signup/seller/', SellerSignUpView.as_view(), name='seller_signup'),
]