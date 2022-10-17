from dataclasses import fields
from rest_framework import serializers
from furn.models import *

class CarouselApi(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['title', 'aboute', 'price']

class ArrivalApi(serializers.ModelSerializer):
    class Meta:
        model = Arrival
        fields = ['arrivals_title', 'arrivals_price', 'arrivals_text', '']

class BlogApi(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'aboute']

class ProductApi(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['rating', 'price', 'title']
        
class ContactApi(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'mobile', 'text']




        
        