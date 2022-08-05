from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        

