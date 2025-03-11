from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home, name='home'),
     path('Contact/', views.Contact, name='Contact'),
     path('about/', views.About, name='About'),
]
