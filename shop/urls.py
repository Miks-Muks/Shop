from django.urls import path
from shop.views import home_page, product_detail, product_delete, card_detail, add_to_basket, show_basket, order_add

urlpatterns=[
    path('', home_page, name='home_page'),
    path('product detail/<int:product_pk>', product_detail, name='product_detail'),
    path('product delete/<product_pk>', product_delete, name='product_delete'),
    path('card detail/<int:card_pk>', card_detail, name='card_detail'),
    path('basket/<int:product_pk>', add_to_basket, name='add_to_basket'),
    path('show_basket', show_basket, name='show_basket'),
    path('order', order_add, name='order_add'),
]
