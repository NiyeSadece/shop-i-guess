import pytest

from django.contrib.auth.models import User
from django.test import Client

from shop_app.models import Product, Category



@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    user = User.objects.create_user(
         username='test',
         password='test123'
     )
    return user


@pytest.fixture
def category():
    category = Category.objects.create(
        name='paintings',
        slug='paintings',
    )
    return category


@pytest.fixture
def product(category):
    product = Product.objects.create(
        name='simple painting',
        description='simple painting',
        price=20,
        category=category,
        slug='simple-painting',
    )
    return product

