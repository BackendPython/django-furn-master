from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.db.models import Q
from furn.models import *

User = get_user_model()

def dashboard_home(request):
    users = User.objects.count()
    blogs = Blog.objects.count()
    support = Contact.objects.count()
    new_products = Arrival.objects.count()
    products = Product.objects.count() + new_products
    contact_taklif = Contact.objects.filter(choices="Taklif").count()
    contact_support = Contact.objects.filter(choices="Support").count()
    # contact_last = 
    context = {
        "blogs":blogs,
        "users": users,
        "support": support,
        "products":products,
        "new_products": new_products,
        "contact_taklif": contact_taklif,
        "contact_support": contact_support,
    }
    return render(request, 'dashboard/pages/home.html', context)

def buttons(request):
    return render(request, 'dashboard/includes/buttons.html')

def cards(request):
    return render(request, 'dashboard/includes/cards.html')

def animation(request):
    return render(request, 'dashboard/includes/animation.html')

def colors(request):
    return render(request, 'dashboard/includes/colors.html')

def border(request):
    return render(request, 'dashboard/includes/border.html')

def other(request):
    return render(request, 'dashboard/includes/other.html')

def dashboard_login(request):
    return render(request, 'dashboard/registertration/login.html')

def forgot_password(request):
    return render(request, 'dashboard/includes/forgot-password.html')

def register(request):
    return render(request, 'dashboard/registertration/register.html')

def charts(request):
    return render(request, 'dashboard/includes/charts.html')

def tables(request):
    if 'search' in request.GET:
        search = request.GET['search']
        full_search = Q(Q(first_name__icontains=search) | Q(email__icontains=search))
        user_info = User.objects.filter(full_search)
        
    else:
        user_info = User.objects.all()
        
    context = {
        "user": user_info,
    }
    return render(request, 'dashboard/includes/tables.html', context)

def page_404(request):
    return render(request, 'dashboard/includes/404.html')

def blank(request):
    return render(request, 'dashboard/includes/blank.html')

