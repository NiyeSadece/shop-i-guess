"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from shop import settings
from shop_app import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', shop_views.MainView.as_view(), name='home'),
    path('shop/', shop_views.ShopView.as_view(), name='shop'),
    path('contact/', shop_views.ContactView.as_view(), name="contact"),
    path('about-us/', shop_views.AboutUsView.as_view(), name='about-us'),
    path('create-account/', shop_views.SignUpView.as_view(), name='sign-up'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
