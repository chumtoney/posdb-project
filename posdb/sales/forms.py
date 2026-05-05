# sales/forms.py

from django import forms
from .models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model  = OrderItem
        fields = ['product', 'quantity']

    def clean_quantity(self):
        """Validation: quantity must be at least 1."""
        qty = self.cleaned_data.get('quantity') # ប្រើ .get() ដើម្បីសុវត្ថិភាព
        if qty is not None and qty < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        return qty