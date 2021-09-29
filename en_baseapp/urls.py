from django.urls import path
from .views import en_show_index
from .views import en_show_production
from .views import en_show_about
from .views import en_show_contact
from .views import en_show_products
from .views import en_show_documents

urlpatterns = [    
    path('', en_show_index, name='en_show_index'),
    path('production/', en_show_production, name='en_show_production'),
    path('about/', en_show_about, name='en_show_about'),
    path('contact/', en_show_contact, name='en_show_contact'),
    path('products/', en_show_products, name='en_show_products'),
    path('documents/', en_show_documents, name='en_show_documents'),

]