from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Item
# Create your views here.

class Store(ListView):
  model = Item
  template_name = "store/store.html"
  context_object_name = "all_items"

  
class Cart(ListView):
  model = Item
  template_name = "store/cart.html"
  context_object_name = "item_in_car"


class Checkout(ListView):
  model = Item
  template_name = "store/checkout.html"
  context_object_name = "item_in_checkout"

class SingleItem(View):
  def get(self, request, slug):
    item=Item.objects.get(slug=slug)
    context={"item":item}
    return render(request, "store/item-detail.html", context)