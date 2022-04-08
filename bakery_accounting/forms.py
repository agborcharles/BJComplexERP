from django import forms
from .models import *

class BakerySalesForm(forms.ModelForm):
    class Meta:
        model = BakerySales
        fields = "__all__"
        exclude = ('slug',)
