from django.shortcuts import render
from django.views import View

from .forms import SignUpForm

# Create your views here.


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main.html")


class ShopView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shop.html")


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "about.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, "signup.html", {'form': form})

    def post(self, request, *args, **kwargs):
        return render(request, "orderhistory.html")


class OrderHistory(View):
    def get(self, request, *args, **kwargs):
        return render(request, "orderhistory.html")
