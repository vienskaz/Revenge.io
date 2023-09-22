from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import JsonResponse
import json
import datetime

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

  
def cart(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items =order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0,}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

     
def checkout(request):
    if request.user.is_authenticated:
        customer =  request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items =order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0,}
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)



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
    
class Account(View):
    def get(self, request):
      return render(request, "store/account.html", {})
    


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
           username=request.POST['username']
           password=request.POST['password']
           user= authenticate(request, username=username, password=password)
           if user is not None:
              login(request, user)
              return redirect('account')
           else:
              return redirect('login')
        else:
            return render(request, "store/login.html", {}) 
    else:
       return render(request, "store/account.html", {}) 
    

def logout_user(request):
   logout(request)
   return redirect('login')

def register_view(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']


            customer, created = Customer.objects.get_or_create(user=user)
            customer.first_name = first_name
            customer.last_name = last_name
            customer.email = email
            customer.save()

            login(request, user)
            return redirect('account')
    else:
        form = CustomRegistrationForm()

    return render(request, 'store/register.html', {'form': form})


def updateItem(request):
    data=json.loads(request.body)
    itemId= data['itemId']
    action=data['action']
    print('Action:', action)
    print('itemId:', itemId)
    customer = request.user.customer
    item= Item.objects.get(id=itemId)
    order, created= Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created= OrderItem.objects.get_or_create(order=order,item=item)

    if action =='add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
       orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
       orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
      customer = request.user.customer
      order, created= Order.objects.get_or_create(customer=customer, complete=False)
      total= float(data['form']['total'])
      order.transaction_id = transaction_id

      if total==order.get_cart_total:
         order.complete=True
      order.save()

      Address.objects.create(
         customer=customer,
         order=order,
         address=data['shipping']['address'],
         city=data['shipping']['city'],
         state=data['shipping']['state'],
         zipcode=data['shipping']['zipcode'],
         country=data['shipping']['country']
      )
    
    else:
       print("user is not logged in")
      
    return JsonResponse('Payment complete', safe=False)
   