from .models import User, Room
from django.forms import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "gender", "course", "faculty", "room"]

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