from django.urls import path
from shop.views import home_page, product_detail, product_delete, card_detail

urlpatterns=[
    path('home', home_page, name='home_page'),
    path('product detail/<int:product_pk>', product_detail, name='product_detail'),
    path('product delete/<int:product_pk>', product_delete, name='product_delete'),
    path('card delete/<int:card_pk>', card_detail, name='card_detail')
]