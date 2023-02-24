from django.urls import path
from .views import home,carpinteria   

urlpatterns = [
    path('',home,name='home'),
    path('carpinteria/',carpinteria,name='carpinteria'),

]