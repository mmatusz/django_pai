#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portal-homepage'),
    path('about/', views.about, name='portal-about'),

    
]
