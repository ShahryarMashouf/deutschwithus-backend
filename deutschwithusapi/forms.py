from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    lase_name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password', 'password2']