from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields
from .models import Subscribe
from django import forms

User = Subscribe

class Followers(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
        )


class Register(UserCreationForm):
    class Meta:
        model = get_user_model( )
        fields = ("username",)
        field_classes = {"username":UsernameField}