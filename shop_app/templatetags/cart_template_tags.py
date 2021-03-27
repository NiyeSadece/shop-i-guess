from django import template
from shop_app.models import ShoppingCart

register = template.Library()


@register.filter
def cart_item_count(user):
    """Displays number of items in the shopping cart.
        Currently shows only unique products."""
    if user.is_authenticated:
        qs = ShoppingCart.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].products.count()
    return 0
