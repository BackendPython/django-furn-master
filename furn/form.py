from django import forms
from dataclasses import fields
from .models import Subscribe

User = Subscribe

class Followers(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
        )
