from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField


class User(AbstractUser):
    image = ImageField(upload_to='images/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)