from store.models import Product
from category import models


from django.contrib import admin
from . import models as m
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name","price","stock","category","created_date")
    prepopulated_fields={"slug":("product_name",)}

admin.site.register(m.Product,ProductAdmin)