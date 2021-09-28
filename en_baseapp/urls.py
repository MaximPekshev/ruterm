from django.urls import path
from .views import en_show_index
from .views import en_show_production

urlpatterns = [    
    path('', en_show_index, name='en_show_index'),
    path('production/', en_show_production, name='en_show_production'),

]