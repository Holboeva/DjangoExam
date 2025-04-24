from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, Model, ForeignKey, CASCADE
from django.db.models.fields import CharField, DecimalField, TextField, DateTimeField, PositiveIntegerField


class User(AbstractUser):
    image = ImageField(upload_to='images/', null=True, blank=True)
    phone_number = CharField(max_length=20, null=True, blank=True)
    mobile_number = CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username


class Category(Model):
    name = CharField(max_length=100)


class Product(Model):
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField()
    category = ForeignKey(Category, on_delete=CASCADE, related_name='products')
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)


class ProductImage(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='images')
    image = ImageField(upload_to='images/', null=True, blank=True)


class Order(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='orders')
    status = CharField(max_length=20, default='yangi')
    created_at = DateTimeField(auto_now_add=True)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name='items')
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = PositiveIntegerField()
