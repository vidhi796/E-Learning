from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),  # Page 1: List of cards
    path('card/<slug:card_slug>/', views.topic_list, name='topic_list'),  # Page 2: Topics by card slug
    path('card/<slug:card_slug>/topic/<slug:topic_slug>/', views.topic_detail, name='topic_detail'), 
]
