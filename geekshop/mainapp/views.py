from unicodedata import category
from django.shortcuts import render
from django.utils import timezone
import random
from mainapp.models import ProductCategory
from mainapp.models import Product
# Create your views here.
MENU_LINKS = [
    {"url": "main", "name": "домой" },
    {"url": "products:products", "name": "продукты" },
    {"url": "contact", "name": "контакты" },
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
    products = [{
        "name": "Стул1 повышенного класса",
        "discrip": "Не оторваться прям.",
        "img":"/img/product-11.jpg"
    }, {
        "name": "Стул2 повышенного класса",
        "discrip": "Не оторваться.",
        "img":"/img/product-21.jpg"
    }, {
        "name": "Лампа повышенного класса",
        "discrip": "Не оторваться.",
        "img":"/img/product-31.jpg"
    }, ]
    return render(request, "mainapp/products.html", context={
        "title" : "Продукты",
        "menu_links": MENU_LINKS,
        "products": products,
        "categorys":categorys

    },)

def category(request, pk):
    return products(request) 


def contact(request):
    return render(request, "mainapp/contact.html", context={
        "title" : "Контакты",
        "menu_links": MENU_LINKS,
    },)
