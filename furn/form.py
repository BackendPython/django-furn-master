from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from dataclasses import fields
from .models import MyUser
from django import forms

User = get_user_model()


class Registration(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            "first_name",
            "last_name",
            "email",
        )

# class Registertration(UserCreationForm):
#     first_name = forms.CharField(
#         max_length=100,
#         required = True,
#         widget = forms.TextInput(attrs={
#             "class" : "form-control",
#             "placeholder" : "Ismingizni kiriting"
#         })
#     )
#     last_name = forms.CharField(
#         max_length=100,
#         required = True,
#         widget = forms.TextInput(attrs={
#             "class" : "form-control",
#             "placeholder" : "Familiyangizni kiriting"
#         })
#     )
#     email = forms.EmailField(
#         max_length=100,
#         required = True,
#         widget = forms.TextInput(attrs={
#             "class" : "form-control",
#             "placeholder" : "Emailni kiriting"
#         })
#     )
#     password1 = forms.CharField(
#         max_length=100,
#         required = True,
#         widget = forms.TextInput(attrs={
#             "class" : "form-control",
#             "placeholder" : "Parolingizni kiriting"
#         })
#     )
#     password2 = forms.CharField(
#         max_length=100,
#         required = True,
#         widget = forms.TextInput(attrs={
#             "class" : "form-control",
#             "placeholder" : "Parolingizni qayta kiriting"
#         })
#     )

#     class Meta:
#         model = User
#         fields = (
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2"
#         )


