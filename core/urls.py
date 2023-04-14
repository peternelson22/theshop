from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('mens/',mens, name='mens'),
    path('womens/',womens, name='womens'),
    path('trending/',trending, name='trending'),
    path('add_item/',add_item, name='add_item'),
    path('add_women_item/',add_women_item, name='add_women_item'),
    path('delete_item/<int:id>/',delete_item, name='delete_item'),
    path('delete_women_item/<int:id>/',delete_women_item, name='delete_women_item'),
    path('update_item/<int:id>/',update_item, name='update_item'),    
    path('update_women_item/<int:id>/',update_women_item, name='update_women_item'),    
]