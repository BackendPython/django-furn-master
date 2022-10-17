from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('carousel', carousel, name='carousel'),
    path('carousel-add', carousel_add, name='carousel_add'),
    path('carousel-<int:pk>', carousel_single, name='carousel_single'),
    path('carousel-edit/<int:pk>', carousel_single_edit, name='carousel_single_edit'),
    path('carousel-delete/<int:pk>', carousel_single_delete, name='carousel_single_delete'),
    
    path('arrival', arrival, name='arrival'),
    path('arrival-add', arrival_add, name='arrival_add'),
    path('arrival-<int:pk>', arrival_single, name='arrival_single'),
    path('arrival-edit/<int:pk>', arrival_single_edit, name='arrival_single_edit'),
    path('arrival-delete/<int:pk>', arrival_single_delete, name='arrival_single_delete'),
    
    path('product', product, name='product'),
    path('product-add', product_add, name='product_add'),
    path('product-<int:pk>', product_single, name='product_single'),
    path('product-edit/<int:pk>', product_single_edit, name='product_single_edit'),
    path('product-delete/<int:pk>', product_single_delete, name='product_single_delete'),

    path('blog', blog, name='blog'),
    path('blog-add', blog_add, name='blog_add'),
    path('blog-<int:pk>', blog_single, name='blog_single'),
    path('blog-edit/<int:pk>', blog_single_edit, name='blog_single_edit'),
    path('blog-delete/<int:pk>', blog_single_delete, name='blog_single_delete'),
    
    path('contact', contact, name='contact'),
    path('contact-add', contact_add, name='contact_add'),
    path('contact-<int:pk>', contact_single, name='contact_single'),
    path('contact-edit/<int:pk>', contact_single_edit, name='contact_single_edit'),
    path('contact-delete/<int:pk>', contact_single_delete, name='contact_single_delete'),
]