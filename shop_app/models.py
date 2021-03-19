from django.contrib.auth.models import User
from django.db import models

# Create your models here.


RATING = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)

STATUS = (
    (0, "cancelled"),
    (1, "payment unconfirmed"),
    (2, "payment confirmed"),
    (3, "shipped"),
)


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unique = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)
    count = models.IntegerField


class Category(models.Model):
    name = models.CharField(max_length=64)
    products = models.ManyToManyField(Product)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)
    body = models.TextField


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=125)
    line2 = models.CharField(max_length=125)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=64)
    phone = models.IntegerField


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date = models.DateField
    status = models.IntegerField(choices=STATUS)
