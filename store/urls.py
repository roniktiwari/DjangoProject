
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('',views.show_store,name='store'),
    path('<slug:category_slug>/',views.show_store,name="product_by_category"),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name="product_details")
] 