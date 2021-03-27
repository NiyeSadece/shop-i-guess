import pytest
from shop_app.models import Product


@pytest.mark.django_db
def test_home_page_view(client):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_product_page_view(client, product):
    response = client.get('/product/{product.slug}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_page_view(client):
    response = client.get('/order-summary/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_order_page_view2(client, user):
    client.force_login(user)
    response = client.get('/order-summary/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_checkout_page_view(client):
    response = client.get('/checkout/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_checout_page_view2(client, user):
    client.force_login(user)
    response = client.get('/checkout/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_checkout2_page_view(client):
    response = client.get('/checkout2/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_checkout2_page_view2(client, user):
    response = client.get('/checkout2/')
    client.force_login(user)
    assert response.status_code == 200

