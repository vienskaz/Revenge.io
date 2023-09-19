from django.db import models

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
  
