import pytest


@pytest.mark.django_db
def test_home_page_view(client):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_page_view(client):
    response = client.get('/order-summary/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_checkout_page_view(client):
    response = client.get('/checkout/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_checkout2_page_view(client):
    response = client.get('/checkout2/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_product_page_view(client, product):
    response = client.get(f'/product/{product.slug}')
    assert response.status_code == 301


@pytest.mark.django_db
def test_add_to_cart_view(client, user, product):
    client.force_login(user)
    response = client.get(f'/add-to-cart/{product.slug}')
    assert response.status_code == 301


@pytest.mark.django_db
def test_remove_from_cart_view(client, user, product):
    client.force_login(user)
    response = client.get(f'/remove-from-cart/{product.slug}')
    assert response.status_code == 301


@pytest.mark.django_db
def test_remove_item_from_cart_view(client, user, product):
    client.force_login(user)
    response = client.get(f'/remove-item-from-cart/{product.slug}')
    assert response.status_code == 301


@pytest.mark.django_db
def test_checkout_page_post(client, user):
    client.force_login(user)
    response = client.post('/checkout/', {
        'name': 'test_name',
        'street': 'test_street',
        'zip': 'test_zip',
        'city': 'test_city',
        'country': 'AZ',
        'default': False,
    })
    assert response.status_code == 302
