from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, SellerSignUpForm

class SignUpView(CreateView):
      form_class = CustomUserCreationForm
      success_url = reverse_lazy('login')
      template_name = 'registration/signup.html'

class SellerSignUpView(CreateView):
      form_class = SellerSignUpForm
      success_url = reverse_lazy('login')
      template_name = 'registration/seller_signup.html'

      def form_valid(self, form):
            # You can add logic here to notify the admin that a new seller applied
            return super().form_valid(form)