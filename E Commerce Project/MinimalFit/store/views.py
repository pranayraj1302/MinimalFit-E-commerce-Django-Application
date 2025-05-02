from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def home(request):
    # Show only products marked for homepage display
    products = Product.objects.filter(display_on_homepage=True)
    return render(request, 'store/index.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "store/product_detail.html", {"product": product})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    # Add product to cart logic here
    return redirect('cart_view')  # Redirect after adding


def contact_view(request):
    return render(request, 'store/contact.html')


def catalogue_view(request):
    # Show all products in the catalogue
    products = Product.objects.all()
    return render(request, 'store/catalogue.html', {'products': products})

def about(request):
    return render(request, 'store/about.html')

