from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        

