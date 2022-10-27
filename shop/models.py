from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=70, verbose_name="Название категории", blank=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    published_date = models.DateTimeField(verbose_name='дата добавления', auto_now=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_name')

    # image_product = models.ImageField()

    def __str__(self):
        return self.title


class Card(models.Model):
    number_card = models.CharField(max_length=16, verbose_name='Number card ', blank=True)
    mouth = models.CharField(max_length=2, verbose_name='Mouth', blank=True)
    yeat = models.CharField(max_length=2, verbose_name='Year', blank=True)
    cvc = models.CharField(max_length=3, verbose_name='CVC', blank=True)
    name = models.CharField(max_length=20, verbose_name='Write your name ')
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='product_basket')

    def __str__(self):
        return f'{self.user}'


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.products}'