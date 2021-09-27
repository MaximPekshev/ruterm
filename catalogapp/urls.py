from django.urls import path
from .views import show_category, show_product_detail
from baseapp.views import show_products


urlpatterns = [   
    path('', show_products, name='show_products'),
    path('category/<str:cpu_slug>/', show_category, name='show_category'),
    path('product/<str:cpu_slug>/', show_product_detail, name='show_product_detail'),
]

