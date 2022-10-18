from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=70, verbose_name="Название категории", blank=True)





    def __str__(self):
        return self.category



