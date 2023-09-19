from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

class Store(ListView):
  model = Item
  template_name = "store/store.html"
  context_object_name = "all_items"

  def post(self, request):
    entered_email = request.POST.get('customer_posted', '').strip()

    if not entered_email:
        return HttpResponseRedirect("/")
    try:
        validate_email(entered_email)
    except ValidationError:
        return HttpResponseRedirect("/")

    if NewsletterUser.objects.filter(email=entered_email).exists():
        return HttpResponseRedirect("/")

    newsletteruser = NewsletterUser(email=entered_email)
    newsletteruser.save()

    return HttpResponseRedirect("/")

  
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
  
class Media(View):
    def get(self, request):
      return render(request, "store/media.html", {})

class Info(View):
    def get(self, request):
      return render(request, "store/info.html", {})
    
class Contact(View):
    def get(self, request):
      return render(request, "store/contact.html", {})
    
class Policy(View):
    def get(self, request):
      return render(request, "store/policy.html", {})