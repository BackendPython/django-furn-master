from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields
from django import forms

User = get_user_model()

class Registertration(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required = True,
        widget = forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Familiyangizni kiriting"
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required = True,
        widget = forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Familiyangizni kiriting"
        })
    )
    email = forms.EmailField(
        max_length=100,
        required = True,
        widget = forms.TextInput(attrs={
            "class" : "form-control",
            "placeholder" : "Familiyangizni kiriting"
        })
    )


