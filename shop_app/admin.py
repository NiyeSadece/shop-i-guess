from django.contrib import admin
from .models import Product, ProductInCart, ShoppingCart, Comment, Category, Address


admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(ShoppingCart)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Address)
