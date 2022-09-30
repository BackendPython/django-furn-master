from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Avg
from django.views import generic
from django.db.models import Q
from furn.models import *
from furn.form import *

def home(request):

    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)

    if 'search' in request.GET:
        search = request.GET['search']
        full_serach = Q(Q(title__icontains=search) | Q(price__icontains=search) )
        products = Product.objects.filter(full_serach)
    
    else:
        products = Product.objects.all()
        
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ContactForm()
    
    blog = Blog.objects.all()
    base = Carousel.objects.all()
    categories = Category.objects.all()
    return render(request, 'pages/home.html', {
         "blog":blog,
         "base": base,
         "form": form,
         "arrivals":arrivals,
         "products":products,
         "categories":categories,
        })
    
def arrivals_detail(request, pk):
    
    arrivals_details = Arrival.objects.get(id=pk)
    
    context = {
        "arrivals_details": arrivals_details,
    }
    return render(request, 'details/arrival_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = Registration()
        
    return render(request, 'registration/signup.html', {"form":form})

def logout_redirect(request):
    return render(request, 'registration/logout-redirect.html')

def profile(request):
    if request.method == 'POST':
        user_form = UptadeUserForm(request.POST, instance=request.user)
        profile_form = UptadeProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("furn:home")
    else:
        user_form = UptadeUserForm(instance=request.user)
        profile_form = UptadeProfileForm(instance=request.user.profile)
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    
    return render(request, 'pages/profile.html', context)

def rate_fun(request, pk):
    rate = Product.objects.get(id=pk)
    avg_rate = Product.objects.aggregate(Avg("rating"))
    if request.method == 'POST':
        rate_form = Product_Rate_Form(request.POST, instance=rate)
        if rate_form.is_valid():
            rate_form.save()
        return redirect('furn:home')
    else:
        rate_form = Product_Rate_Form(instance=rate)

    context = {
        "rate": rate,
        "avg_rate": avg_rate,
        "rate_form": rate_form,
    }
    return render(request, 'pages/rate.html', context)
