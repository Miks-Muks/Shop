from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product, Card


# Create your views here.
def home_page(requests):
    category = Category.objects.all()
    return render(requests, 'shop/home page.html', {'cat': category})


def product_detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    return render(request, 'shop/product detail.html', {'product': product})


def product_delete(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    product.delete()
    return redirect('home_page')


def card_detail(request, card_pk):
    card = Card.objects.get(pk=card_pk)
    return render(request, 'shop/card detail', { 'card': card})

