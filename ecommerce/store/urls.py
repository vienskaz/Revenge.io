from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.Store.as_view(), name='store'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('<slug:slug>', views.SingleItem.as_view(), name="item-detail-page"),
  path('pages/lookbook/', views.Media.as_view(), name='media'),
  path('pages/info', views.Info.as_view(), name='info'),
  path('pages/contact', views.Contact.as_view(), name='contact'),
  path('policies/shipping-policy', views.Policy.as_view(), name='policy'),
  path('account/register', views.register_view, name="register"),
   path('account/login', views.login_view, name="login"),
   path('account/logout', views.logout_user, name="logout"),
   path('account/', views.Account.as_view(), name="account"),
   path('update_item/', views.updateItem, name='update_item'),
   path('process_order/', views.processOrder, name='process_order')

]