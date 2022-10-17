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
]