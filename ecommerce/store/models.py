from django.db import models

# Create your models here.

class Item(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=300)
  price = models.FloatField()
  image=models.ImageField(upload_to="images", null=True,default="default.jpg")
  slug=models.SlugField(unique=True, db_index=True)

  def __str__(self):
    return f'{self.name} {self.price}' 
