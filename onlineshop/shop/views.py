from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
        }
    
    return render(request,'shop/product_detail.html', context)