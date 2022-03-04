from .models import Req
from django.forms import *


class ReqForm(ModelForm):
    class Meta:
        model = Req
        fields = ["first_name", "last_name", "email", "gender", "course", "faculty"]
        widgets = {"first_name": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your name'}),
                   "last_name": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your surname'}),
                    "email": TextInput(attrs={
                     'class': 'form-control',
                     'placeholder': 'Enter your E-mail'})
                   }