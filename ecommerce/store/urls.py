from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.Store.as_view(), name='store'),
  path('cart/', views.Cart.as_view(), name='cart'),
  path('checkout/', views.Checkout.as_view(), name='checkout'),
  path('<slug:slug>', views.SingleItem.as_view(), name="item-detail-page")
]