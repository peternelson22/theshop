from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registernow, name='register'),
    path('login/',loginnow, name='login'),
    path('logout/',logoutnow,name ='logout'),
]