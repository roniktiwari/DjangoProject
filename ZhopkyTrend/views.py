from django.http import HttpResponse
from django.shortcuts import render 
from store.models import Product
def home_view(request):

    products=Product.objects.all().filter(is_available=True)

    context={
        "products":products
    }
    return render(request,'home.html',context)
