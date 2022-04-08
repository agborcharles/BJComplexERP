from django import forms
from .models import *


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"
        exclude = ('slug',)

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
        exclude = ('slug',)
