from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a new form and inherit the UserCreationForm to add additional field
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']