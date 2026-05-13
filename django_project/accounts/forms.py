from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
            model = CustomUser
            # We explicitly list the fields to ensure they are captured from the POST request
            fields = UserCreationForm.Meta.fields + (
                  'email', 'age', 'gender', 'mobile_no', 
                  'city_village', 'state', 'country', 'pincode',
            )

class CustomUserChangeForm(UserChangeForm): 
      class Meta: 
            model = CustomUser 
            fields = ('username', 'email', 'age', 'gender', 'mobile_no', 'city_village', 'state', 'country', 'pincode')
            
class SellerSignUpForm(UserCreationForm):
      category = forms.ChoiceField(
            choices=CustomUser.CATEGORY_CHOICES,
            widget=forms.Select(attrs={'class': 'form-select bg-light border-0', 'id': 'id_product_category'})
      )
      sub_category = forms.ChoiceField(
            choices=CustomUser.SUB_CATEGORY_CHOICES,
            widget=forms.Select(attrs={'class': 'form-select bg-light border-0', 'id': 'id_sub_category'})
      )
      class Meta(UserCreationForm.Meta):
            model = CustomUser
            fields = UserCreationForm.Meta.fields + (
                  'email', 'age', 'gender', 'mobile_no', 
                  'city_village', 'state', 'country', 'pincode',
                  'category', 'sub_category',
            )

class CustomPasswordChangeForm(PasswordChangeForm):
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field in self.fields.values():
                  field.widget.attrs.update({
                        "class": "form-control"
                  })