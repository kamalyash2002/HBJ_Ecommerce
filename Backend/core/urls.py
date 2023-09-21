from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    # PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    Aboutview,
    Contactview,
    profile_view,
    contact_view,
    paymentnew,
    success

)
from . import views

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('about/', Aboutview.as_view(), name='about'),
    path('contact',Contactview.as_view(), name='contact'),
    path('profile/',views.profile_view, name = 'profile'),
    path('contact_view',views.contact_view, name ='contact_view'),
    path('paymenttest',views.paymentnew, name = 'paymenttest'),
    path('success',views.success, name = 'success')
    # path('account/login', views.login, name = "login"),
] 

