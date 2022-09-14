from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from furn.models import Contact, Product, Profile
from django import forms

User = get_user_model()

class UptadeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
class UptadeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number']
        
class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2",]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'choices', 'mobile', 'text']

class Product_Rate_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['rate_1_choices', ]
        

