from django import forms
from .models import *

class Worker(forms.ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        exclude = ('slug',)


class Role(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"



class Department(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class Employee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
