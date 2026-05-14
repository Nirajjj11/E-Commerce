from django import forms
from .models import OrderItems


class OrderStatusUpdateForm(forms.ModelForm):

      notes = forms.CharField(required=False,
            widget=forms.Textarea(attrs={
                  "class": "form-control",
                  "rows": 3
            })
      )

      class Meta:
            model = OrderItems

            fields = ["status","tracking_id"]

            widgets = {
                  "status": forms.Select(attrs={
                        "class": "form-select"
                  }),

                  "tracking_id": forms.TextInput(attrs={
                        "class": "form-control"
                  }),
            }