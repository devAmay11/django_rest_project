from django.urls import path
from product.views import *
from core.views import *

urlpatterns = [
    path('people/',people),
    path('index/',index),
    path('hello_world/',hello_world),
    path('add_product/', add_product),
    path('product_list/', product_list),
    path('edit_product/<int:pk>/',edit_product),
    path('delete_product/<int:pk>/',delete_product),
]