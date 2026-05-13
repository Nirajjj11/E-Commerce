from django.urls import path
from .views import *

urlpatterns = [
      path("", UserDashboardView.as_view(), name="user_dashboard"),
]