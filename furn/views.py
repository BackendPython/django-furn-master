from django.shortcuts import render, redirect
from furn.models import *
from furn.form import Followers

def home(request):

    if request.method == "POST":
        form = Followers(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = Followers()

    base = Carousel.objects.all()
    arrivals = Arrival.objects.all()
    blog = Blog.objects.all()
    products = Product.objects.all()
    return render(request, 'pages/home.html', {"base": base, "arrivals":arrivals, "blog":blog, "products":products, "form":form})