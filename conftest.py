import pytest

from django.contrib.auth.models import User
from django.test import Client

from shop_app.models import Product, Category


@pytest.fixture
def client():
    return Client()


# @pytest.fixture
# def user():
#     return User.objects.create_user(
#         username='test',
#         password='test123'
#     )


@pytest.fixture
def addCategory():
    Category.objects.create(name='paintings', slug='paintings')
    Category.objects.create(name='seasonal', slug='seasonal')


@pytest.fixture
def addProduct():
    category = Category.objects.get(name='paintings')
    product = Product.objects.create(
        name='simple painting',
        description='simple painting',
        price=20,
        slug='simple-painting',
    )
    product.category.add(category)

    category = Category.objects.get(name='paintings')
    product = Product.objects.create(
        name='large painting',
        description='large painting',
        price=50,
        discount_price=45,
        slug='large-painting',
    )
    product.category.add(category)

    category = Category.objects.get(name='seasonal')
    product = Product.objects.create(
        name='crochet santa',
        description='crochet santa',
        price=5,
        discount_price=3,
        slug='crochet-santa',
    )
    product.category.add(category)
