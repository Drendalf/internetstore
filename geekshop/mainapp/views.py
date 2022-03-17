from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
import random
from mainapp.models import ProductCategory
from mainapp.models import Product
# Create your views here.
MENU_LINKS = [
    {"url": "main", "active": ["main"], "name": "домой" },
    {"url": "products:all", "active": ["products:all", "products:category"], "name": "продукты" },
    {"url": "contact", "active": ["contact"], "name": "контакты" },
]

def index(request):
    products = Product.objects.all()
    
    return render(request, "mainapp/index.html", context={
        "title" : "Главная",
        "menu_links": MENU_LINKS,
        "variable": "Hello",
        "time": timezone.now(),
        "numbers":[random.randint(0, 100) for _ in range(0,5)],
        "products": products,

    }, )

def products(request):
    categorys=ProductCategory.objects.all()
    products = Product.objects.all()[:4]
 
    return render(request, "mainapp/products.html", context={
        "title" : "Продукты",
        "menu_links": MENU_LINKS,
        "products": products,
        "categorys":categorys

    },)

def category(request, pk):
    categorys=ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)

    return render(request, "mainapp/products.html", context={
        "title" : "Продукты",
        "menu_links": MENU_LINKS,
        "products": products,
        "categorys":categorys      

    },)


def contact(request):
    return render(request, "mainapp/contact.html", context={
        "title" : "Контакты",
        "menu_links": MENU_LINKS,
    },)
