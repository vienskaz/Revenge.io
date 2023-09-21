from typing import Any
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Item(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=500)
  price = models.DecimalField(max_digits=8, decimal_places=2) 
  image=models.ImageField(upload_to="images", null=True,default="default.jpg")
  care_instructions=models.TextField(max_length=500)
  slug=models.SlugField(unique=True, db_index=True)

  def __str__(self):
    return f'{self.name} {self.price}' 
  

class NewsletterUser(models.Model):
  email=models.EmailField(unique=True)

  def __str__(self):
    return f'{self.email}' 


    
class Address(models.Model):
    first_name=models.CharField(max_length=50, null=False )
    last_name = models.CharField(max_length=50, null=False )
    company=models.CharField(max_length=50, blank=True, null=True)
    addres=models.CharField(max_length=50,null=False  )
    city=models.CharField(max_length=50,null=False  )
    apartment=models.IntegerField(blank=True, null=True)
    country=models.CharField(max_length=50, null=False )
    province=models.CharField(max_length=50,null=False )
    postal_code=models.CharField(max_length=50, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False )
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
      return self.addres
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Customer(models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address ,blank=True)
    email=models.EmailField(unique=True,default="", blank=True)
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="")
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)


    def get_short_name(self):
        return self.first_name or self.email.split("@")[0]
    
class Order(models.Model):
   customer= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
   date_ordered = models.DateTimeField(auto_now_add=True)
   complete =  models.BooleanField(default=False)
   transaction_id = models.CharField(max_length=100, null=True)

   def __str__(self):
      return str(self.id)
   
class OrderItem(models.Model):
   item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
   order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True, blank=True)
   quantity = models.IntegerField(default=0, null=True,blank=True)
   date_added = models.DateTimeField(auto_now_add=True)



def create_customer(sender,instance,created,**kwargs):
    if created:
        user_customer=Customer(user=instance)
        user_customer.save()

post_save.connect(create_customer,sender=User)
