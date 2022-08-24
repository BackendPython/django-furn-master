from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from furn.models import Profile
from dataclasses import fields
from django import forms

User = get_user_model()

class UptadeUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
class UptadeProfileForm(forms.ModelForm):
    # image = forms.ImageField(
    #     required=True,
    #     widget=forms.FileInput(attrs={"class": "form-control-file"}))
    phone_number = forms.EmailField(
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control"}))
    class Meta:
        model = Profile
        fields = ['phone_number',]
        
class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2",]


        

