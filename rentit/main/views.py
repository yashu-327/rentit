from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Booking

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['description']
        price = request.POST['price']
        Product.objects.create(owner=request.user, name=name, description=desc, price_per_day=price)
        return redirect('home')
    return render(request, 'add_product.html')

@login_required
def book_product(request, pid):
    product = get_object_or_404(Product, id=pid)
    if request.method == "POST":
        days = request.POST['days']
        Booking.objects.create(user=request.user, product=product, days=days)
        return redirect('my_bookings')
    return render(request, 'book_product.html', {'product': product})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})