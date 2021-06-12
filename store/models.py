import category
from category.models import Category
from django.db import models
from category import models as m
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name =  models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    description =models.TextField(max_length=500,blank=True)
    price =models.IntegerField()
    images=models.ImageField(upload_to="photos/products")
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(m.Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now_add=True)

    
    def get_url(self):
        return reverse("product_details",args=[self.category.slug,self.slug])



    def  __str__(self):
        return self.product_name