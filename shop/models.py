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
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    # image_product = models.ImageField()

    def __str__(self):
        return self.title


class Card(models.Model):
    number_card = models.CharField(max_length=16, verbose_name='Number card ', blank=True)
    mouth = models.CharField(max_length=2, verbose_name='Mouth', blank=True)
    yeat = models.CharField(max_length=2, verbose_name='Year', blank=True)
    cvc = models.CharField(max_length=3, verbose_name='CVC', blank=True)
    name = models.CharField(max_length=20, verbose_name='Write your name ')

    def __str__(self):
        return self.name
