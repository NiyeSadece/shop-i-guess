from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import CheckoutForm
from .models import Address, Product, ProductInCart, ShoppingCart


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class MainView(ListView):
    model = Product
    paginate_by = 12
    template_name = 'home.html'


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            order = ShoppingCart.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {'form': form, 'order': order}
            address_qs = Address.objects.filter(user=request.user, default=True)
            if address_qs.exists():
                context.update({'default_shipping_address': address_qs[0]})
            return render(request, 'checkout.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("checkout")

    def post(self, request, *args, **kwargs):
        form = CheckoutForm(request.POST or None)
        try:
            order = ShoppingCart.objects.get(user=request.user, ordered=False)
            if form.is_valid():
                use_default_shipping = form.cleaned_data.get('use_default_shipping')
                if use_default_shipping:
                    print("Using the default shipping address")
                    address_qs = Address.objects.filter(user=self.request.user, default=True)
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                        return redirect('checkout2')
                    else:
                        messages.info(request, "No default shipping address available")
                        return redirect('checkout')
                else:
                    print("User is entering a new shipping address")
                    name = form.cleaned_data.get('name')
                    street = form.cleaned_data.get('street')
                    apartment = form.cleaned_data.get('apartment')
                    country = form.cleaned_data.get('country')
                    zip = form.cleaned_data.get('zip')
                    city = form.cleaned_data.get('city')
                    if is_valid_form([name, street, country, zip, city]):
                        shipping_address = Address(
                            user=self.request.user,
                            name=name,
                            street=street,
                            apartment=apartment,
                            country=country,
                            zip=zip,
                            city=city,
                        )
                        shipping_address.save()
                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get('set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()
                        return redirect('checkout2')
                    else:
                        messages.info(self.request, "Please fill in the required shipping address fields")
                        return redirect('checkout')
                
        except ObjectDoesNotExist:
            messages.error(request, "You do not have an active order.")
            return redirect('order-summary')


class Checkout2View(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        order = ShoppingCart.objects.get(user=self.request.user, ordered=False)
        context = {'order': order}
        return render(request, 'checkout2.html', context)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            order = ShoppingCart.objects.get(user=request.user, ordered=False)
            context = {
                'object': order
            }
            return render(request, 'order-summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(request, "You do not have an active order")
            return redirect("/")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "about.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = ProductInCart.objects.get_or_create(
        product=item,
        user=request.user,
        ordered=False,
    )
    order_qs = ShoppingCart.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            order.products.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = ShoppingCart.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = ShoppingCart.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=item.slug).exists():
            order_item = ProductInCart.objects.filter(
                product=item,
                user=request.user,
                ordered=False,
            )[0]
            order.products.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = ShoppingCart.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=item.slug).exists():
            order_item = ProductInCart.objects.filter(
                product=item,
                user=request.user,
                ordered=False,
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.products.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)
