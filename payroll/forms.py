from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ('slug',)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Salaries
        fields = "__all__"
        exclude = ('slug',)
