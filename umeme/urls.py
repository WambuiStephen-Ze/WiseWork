from django.urls import path

from . import views

# app_name = 'umeme'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('starter/', views.starters, name='starter'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('insert/', views.insert, name='insert'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('product/', views.product, name='products'),
    path('team/', views.team, name='team'),
    path('register/', views.register, name='register'),



]