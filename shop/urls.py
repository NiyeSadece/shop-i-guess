from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from shop import settings
from shop_app import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', shop_views.MainView.as_view(), name='home'),
    path('product/<slug>/', shop_views.ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', shop_views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', shop_views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', shop_views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('order-summary/', shop_views.OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', shop_views.CheckoutView.as_view(), name='checkout'),
    path('checkout2/', shop_views.Checkout2View.as_view(), name='checkout2'),
    path('contact/', shop_views.ContactView.as_view(), name='contact'),
    path('about-us/', shop_views.AboutUsView.as_view(), name='about-us'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
