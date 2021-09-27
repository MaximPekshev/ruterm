from django.urls import path
from .views import show_index
from .views import show_production
from .views import show_about_company
from .views import show_contacts


urlpatterns = [    
    path('', show_index, name='show_index'),
    path('about/', show_about_company, name='show_about_company'),
    path('production/', show_production, name='show_production'),
    path('contacts/', show_contacts, name='show_contacts'),
]
