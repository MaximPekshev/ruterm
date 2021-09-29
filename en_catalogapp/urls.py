from django.urls import path
from .views import en_show_category, en_show_product_detail
from en_baseapp.views import en_show_products

urlpatterns = [   
    path('', en_show_products, name='en_show_products'),
    path('category/<str:cpu_slug>/', en_show_category, name='en_show_category'),
    path('product/<str:cpu_slug>/', en_show_product_detail, name='en_show_product_detail'),
]

