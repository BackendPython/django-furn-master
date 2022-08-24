from django.shortcuts import render, redirect
from django.views import generic
from furn.models import *
from furn.form import *

def home(request):

    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)

    blog = Blog.objects.all()
    base = Carousel.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'pages/home.html', {
        "base": base,
         "blog":blog,
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
    if request.method == 'post':
        user_form = UptadeUserForm(request.POST, instance=request.user)
        profile_form = UptadeProfileForm(request.POST, request.FILE, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to="profile")
    else:
        user_form = UptadeUserForm(instance=request.user)
        profile_form = UptadeProfileForm(instance=request.user.profile)
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    
    return render(request, 'pages/profile.html', context)

def uptadeProfileForm(request, pk):
    if request.method == 'post':
        user_form = UptadeUserForm(request.POST, instance=request.user)
        profile_form = UptadeProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to="profile")
    else:
        user_form = UptadeUserForm(instance=request.user)
        profile_form = UptadeProfileForm(instance=request.user.profile)
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    
    return render(request, 'pages/profile-edit.html', context)


