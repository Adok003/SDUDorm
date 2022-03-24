<<<<<<< HEAD
from .models import User, Room
=======
from .models import User
>>>>>>> a5e58c4b5ccea2fb0db983f5fdaee035bbadb3e6
from django.forms import *


class UserForm(ModelForm):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ["first_name", "last_name", "email", "gender", "course", "faculty", "room"]
=======
        fields = ["first_name", "last_name", "email", "gender", "course", "faculty"]
>>>>>>> a5e58c4b5ccea2fb0db983f5fdaee035bbadb3e6
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