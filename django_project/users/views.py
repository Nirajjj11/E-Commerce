from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserDashboardView(LoginRequiredMixin, TemplateView):
      template_name = "dashboard.html"