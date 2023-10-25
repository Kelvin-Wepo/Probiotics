from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from products import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders') ),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('products/',include('products.urls',  namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('', views.home, name='home' ),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)