from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.Store.as_view(), name='store'),
  path('cart/', views.Cart.as_view(), name='cart'),
  path('checkout/', views.Checkout.as_view(), name='checkout'),
  path('<slug:slug>', views.SingleItem.as_view(), name="item-detail-page"),
  path('pages/lookbook/', views.Media.as_view(), name='media'),
  path('pages/info', views.Info.as_view(), name='info'),
  path('pages/contact', views.Contact.as_view(), name='contact'),
  path('policies/shipping-policy', views.Policy.as_view(), name='policy'),
  path('account/register', views.register_view, name="register"),
   path('account/login', views.login_view, name="login")
]