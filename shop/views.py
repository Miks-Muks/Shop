from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Category, Product, Card, Order, Basket


# Create your views here.
def home_page(requests):
    category = Category.objects.all()
    return render(requests, 'shop/base.html', {'cat': category})


def product_detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    return render(request, 'shop/product detail.html', {'product': product})


def product_delete(request, product_pk):
    basket = Basket.objects.filter(user=request.user).firts
    basket.product.remove(product_pk)
    return redirect('show_basket')


def product_delete_all(request):
    basket = Basket.objects.filter(user=request.user)
    basket.product.clear()
    return redirect('show_basket')


def card_detail(request, card_pk):
    card = Card.objects.get(pk=card_pk)
    return render(request, 'shop/card detail', { 'card': card})


def add_to_basket(request, product_pk):
    product = Product.objects.filter(pk=product_pk).firts()
    cart = Basket.objects.filter(user=request.user).firts()
    if cart == None:
        cart = Basket.objects.create(user=request.user)
        cart.product.add(product)
    else:
        cart.product.add(product)
    return redirect('product_detail', product_pk=product.pk)


def show_basket(request):
    user_basket = Basket.objects.filter(user=request.user).first()
    product = user_basket.product.all()
    return render(request, 'shop/show basket.html', {'user_basket': user_basket, 'product':product})


def order_add(request):
    basket = Basket.objects.filter(user=request.user).first()
    products = basket.product.all
    order = Order.objects.create(user=request.user)
    order.products.add(products)
    total_price = sum(basket.product.price)
    basket.product.clear()
    return render(request, 'shop/order.html', {'products': products, 'total':total_price})





