from django import forms
from .models import *

class Task(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        #exclude = ('slug',)
