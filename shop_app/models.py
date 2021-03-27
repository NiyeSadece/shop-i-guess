from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    """Category model for Product model."""
    name = models.CharField(max_length=64)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    """Product model."""
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={'slug': self.slug})

    def get_to_cart_url(self):
        return reverse("add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={'slug': self.slug})


class Comment(models.Model):
    """Comment model yet to be implemented."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField()


class Address(models.Model):
    """Address model."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    street = models.CharField(max_length=125)
    apartment = models.CharField(max_length=125)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=64)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Addresses"


class ProductInCart(models.Model):
    """Products currently in the shopping cart."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    class Meta:
        verbose_name_plural = "ProductsInCarts"

    def get_total_price(self):
        """Get the not discounted price of the same products."""
        return self.quantity * self.product.price

    def get_total_discount_price(self):
        """Get the discounted price of the same products."""
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        """Get the amount saved on the same products."""
        return self.get_total_price() - self.get_total_discount_price()

    def get_final_price(self):
        """Get the final price of the same products."""
        if self.product.discount_price:
            return self.get_total_discount_price()
        return self.get_total_price()


class ShoppingCart(models.Model):
    """Shopping cart model."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductInCart)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        """Get the total price for the whole shopping cart."""
        total = 0
        for order_item in self.products.all():
            total += order_item.get_final_price()
        return total
