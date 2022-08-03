from django.shortcuts import render, redirect, reverse
from django.views import generic
from furn.models import *
from furn.form import *

def home(request):

    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)

    base = Carousel.objects.all()
    blog = Blog.objects.all()
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

class SignUp(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Registration
    def get_success_url(self):
        return reverse('furn:home')








# class Registration(generic.CreateView):
#     template_name = 'registration/signup.html'
#     form_class = Register
    
#     def get_success_url(self):
#         return redirect('furn:home')


