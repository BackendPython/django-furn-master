from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class Registertration(UserCreationForm):
    class Meta:
        model = User
        fields = ("username"),
        field_classes = {"username": UsernameField}

