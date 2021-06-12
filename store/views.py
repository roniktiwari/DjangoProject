import category
from os import cpu_count
from django.shortcuts import get_object_or_404, render
from category.models import Category
# Create your views here.
from .models import Product

def show_store(request,category_slug=None):

    products=None
    categories=None
   
    if category_slug !=None:
        categories=get_object_or_404(Category,slug=category_slug)
        print(type(categories))
        print("--->>>>>>>>>>>",categories)
        products=Product.objects.all().filter(category=categories,is_available=True)

    else:
       products = Product.objects.all().filter(is_available=True)
    
    product_count= products.count()

    context={
        "products":products,
        "product_count":product_count
    }

    return render(request,'store/store.html',context)


def product_detail(request,category_slug,product_slug):

    try:
        category=get_object_or_404(Category,slug=category_slug)
        single_product=Product.objects.get(category=category,slug=product_slug)
    except Exception as e:
        raise e
    context ={
        'product_details':single_product
    }
    
    return render(request,'store/product_detail.html',context)