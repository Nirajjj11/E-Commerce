from django.urls import path
from .views import *

urlpatterns = [
      path("", OrderListView.as_view(), name="orders"),
      path("tracking/<int:pk>/", TrackOrderView.as_view(), name="tracking"),
]