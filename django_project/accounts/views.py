from django.urls import reverse_lazy
from django.views.generic import CreateView ,UpdateView,DeleteView
from .forms import CustomUserCreationForm, SellerSignUpForm

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser 


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
      
class ProfileView(LoginRequiredMixin, TemplateView):
      template_name = 'profile.html'

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # The 'user' is already available in the template via {{ user }} 
            # but you can add extra context here if needed.
            return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
      model = CustomUser
      fields = ['first_name', 'last_name', 'mobile_no', 'city_village', 'state', 'pincode', 'category', 'sub_category']
      template_name = 'profile_update.html'
      success_url = reverse_lazy('profile')

      def get_object(self, queryset=None):
            return self.request.user

      def get_form(self, form_class=None):
            form = super().get_form(form_class)
            # If the user is NOT a seller, remove those fields from the form validation
            if not self.request.user.category:
                  if 'category' in form.fields:
                        del form.fields['category']
                  if 'sub_category' in form.fields:
                        del form.fields['sub_category']
                  
            return form

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
      model = CustomUser
      template_name = 'profile_confirm_delete.html'
      success_url = reverse_lazy('signup')

      def get_object(self):
            return self.request.user
class PasswordChange(LoginRequiredMixin, UpdateView):
      model = CustomUser
      template_name = "password_change.html"